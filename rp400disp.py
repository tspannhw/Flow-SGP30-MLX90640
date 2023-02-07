from PIL import Image, ImageDraw, ImageFont
import time
import ST7735 as ST7735
from datetime import datetime, timezone
from sgp30 import SGP30
import logging
import sys
import subprocess
import os
import traceback
import math
import base64
import json
from time import gmtime, strftime
import random, string
import psutil
import uuid
from time import sleep
from math import isnan
from subprocess import PIPE, Popen
import socket
import argparse
import os.path
import re
import sys
import os
from time import gmtime, strftime

# IP Address
def IP_address():
        try:
            s = socket.socket(socket_family, socket.SOCK_DGRAM)
            s.connect(external_IP_and_port)
            answer = s.getsockname()
            s.close()
            return answer[0] if answer else None
        except socket.error:
            return None

# Get MAC address of a local interfaces
def psutil_iface(iface):
    # type: (str) -> Optional[str]
    import psutil
    nics = psutil.net_if_addrs()
    if iface in nics:
        nic = nics[iface]
        for i in nic:
            if i.family == psutil.AF_LINK:
                return i.address
# Random Word
def randomword(length):
 return ''.join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()) for i in range(length))

# Get the temperature of the CPU for compensation
def get_cpu_temperature():
    process = Popen(['vcgencmd', 'measure_temp'], stdout=PIPE, universal_newlines=True)
    output, _error = process.communicate()
    return float(output[output.index('=') + 1:output.rindex("'")])

external_IP_and_port = ('198.41.0.4', 53)  # a.root-servers.net
socket_family = socket.AF_INET
# Timer
packet_size=3000

# Tuning factor for compensation. Decrease this number to adjust the
# temperature down, and increase to adjust up
factor = 2.25

host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
ipaddress = IP_address()


disp = ST7735.ST7735(
    port=0,
    cs=1,
    dc=9,
    backlight=12,
    rotation=270,
    spi_speed_hz=10000000
)
disp.begin()
# Width and height to calculate text position.
WIDTH = disp.width
HEIGHT = disp.height

img = Image.new('RGB', (WIDTH, HEIGHT), color=(0, 0, 0))
draw = ImageDraw.Draw(img)
rect_colour = (0, 180, 180)
draw.rectangle((0, 0, 160, 80), rect_colour)

try:
    sgp30 = SGP30()
    sgp30.start_measurement()

    while True:
        currenttime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        starttime = datetime.now().strftime('%m/%d/%Y %H:%M:%S')
        start = time.time()

        # Create unique id
        uniqueid = 'sploot_{0}_{1}'.format(randomword(3),strftime("%Y%m%d%H%M%S",gmtime()))
        uuid2 = '{0}_{1}'.format(strftime("%Y%m%d%H%M%S",gmtime()),uuid.uuid4())

        # CPU Temp
        f = open("/sys/devices/virtual/thermal/thermal_zone0/temp","r")
        cputemp = str( f.readline() )
        cputemp = cputemp.replace('\n','')
        cputemp = cputemp.strip()
        cputemp = str(round(float(cputemp)) / 1000)
        cputempf = str(round(9.0/5.0 * float(cputemp) + 32))
        f.close()

        usage = psutil.disk_usage("/")
        end = time.time()

        result = sgp30.get_air_quality()
        row = {}
        row['uuid'] = uniqueid
        row['ipaddress'] = ipaddress
        row['cputempf'] = int(cputempf)
        row['runtime'] =  int(round(end - start))
        row['host'] = os.uname()[1]
        row['hostname'] = host_name
        row['macaddress'] = psutil_iface('wlan0')
        row['endtime'] = '{0}'.format( str(end ))
        row['te'] = '{0}'.format(str(end-start))
        row['cpu'] = psutil.cpu_percent(interval=1)
        row['diskusage'] = "{:.1f} MB".format(float(usage.free) / 1024 / 1024)
        row['memory'] = psutil.virtual_memory().percent
        row['rowid'] = str(uuid2)
        row['systemtime'] = datetime.now().strftime('%m/%d/%Y %H:%M:%S')
        row['ts'] =  int( time.time() )
        row['starttime'] = str(starttime)
        row['equivalentco2ppm'] = float('{:5d}'.format( (result.equivalent_co2)))
        row['totalvocppb'] = float('{0:3d}'.format(result.total_voc))
        json_string = json.dumps(row) 
        print(json_string)
        time.sleep(0.5)
        font_size = 20
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
        colour = (0, 0, 0)
        disText = "VoC: {}".format(str(row['totalvocppb'])) 
        disText2 = "Co2PPM: {}".format( str(row['equivalentco2ppm']))
        draw.text((0, 0), disText, font=font, fill=colour)
        #draw.text((0, 40), disText, font=font, fill=colour)
        disp.display(img)
        time.sleep(0.5)

except KeyboardInterrupt:
    pass
