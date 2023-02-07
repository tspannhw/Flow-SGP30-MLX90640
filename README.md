# Flow-SGP30-MLX90640
Pimoroni Breakout Garden - SGP30 - MLX90650 - RP400 - NiFi - Kafka - Pulsar - Flink - Spark - Iceberg



### Example Data

```

{"uuid": "thrml_hal_20230207194000", "ipaddress": "192.168.1.84", "cputempf": 92, "runtime": 0, "host": "sploot", "hostname": "sploot", "macaddress": "e4:5f:01:f5:6c:e4", "endtime": "1675798800.2332714", "te": "0.00035572052001953125", "cpu": 0.0, "diskusage": "52971.2 MB", "memory": 5.4, "rowid": "20230207194000_cddd4812-5e1b-418c-b460-2916495bced2", "systemtime": "02/07/2023 14:40:01", "ts": 1675798801, "starttime": "02/07/2023 14:40:00", "equivalentco2ppm": 409.0, "totalvocppb": 5.0}

```

https://youtube.com/shorts/Bgd0jfXuoXQ?feature=share




### See

https://www.catscloudsanddata.com/cats


### Talk

** It's Getting Hot in Here!

At last year's current event I monitored the temperature and other attributes at the conference. We'll do that as well and stream it through NiFi and Kafka. But, we'll scan anyone who wants to be thermal scanned during the talk live. I will bring a Raspberry Pi with a MLX90640 Thermal Camera that will capture thermal images of whoever wants, then sends the GIF to a local website (or IMGUR) for your download. I will generate a unique code along with some metadata that get's sent through Kafka and displayed on a real-time dashboard. Come and get your scan.

Everyone looks cool in thermal pixels, you can be next. This talk can be 10 minutes, 45 minutes or put me in the corner somewhere and I'll run this for a an hour or two.

#### Resources:

* https://raw.githubusercontent.com/tspannhw/minifi-gasthermal/master/mlx90640-2020-01-05-20-52-14.gif
* https://www.datainmotion.dev/2020/01/analyzing-wood-burning-stoves-with.html
* https://www.datainmotion.dev/2020/01/cloudera-edge2ai-minifi-java-agent-with.html
* https://www.datainmotion.dev/2019/03/posting-images-to-imgur-via-apache-nifi.html
* https://www.datainmotion.dev/2019/03/posting-images-to-imgur-via-apache-nifi.html
