# Flow-SGP30-MLX90640
Pimoroni Breakout Garden - SGP30 - MLX90650 - RP400 - NiFi - Kafka - Pulsar - Flink - Spark - Iceberg



### Example Data

```

{"uuid": "thrml_hal_20230207194000", "ipaddress": "192.168.1.84", "cputempf": 92, "runtime": 0, "host": "sploot", "hostname": "sploot", "macaddress": "e4:5f:01:f5:6c:e4", "endtime": "1675798800.2332714", "te": "0.00035572052001953125", "cpu": 0.0, "diskusage": "52971.2 MB", "memory": 5.4, "rowid": "20230207194000_cddd4812-5e1b-418c-b460-2916495bced2", "systemtime": "02/07/2023 14:40:01", "ts": 1675798801, "starttime": "02/07/2023 14:40:00", "equivalentco2ppm": 409.0, "totalvocppb": 5.0}

```

## See the Application Running

https://youtube.com/shorts/Bgd0jfXuoXQ?feature=share

![screen](https://raw.githubusercontent.com/tspannhw/Flow-SGP30-MLX90640/main/2023-02-07_12-56-52_981.jpeg)
![screen](https://raw.githubusercontent.com/tspannhw/Flow-SGP30-MLX90640/main/2023-02-07_12-56-54_589.jpeg)
![screen](https://raw.githubusercontent.com/tspannhw/Flow-SGP30-MLX90640/main/2023-02-07_12-56-58_310.jpeg)
![screen](https://raw.githubusercontent.com/tspannhw/Flow-SGP30-MLX90640/main/2023-02-07_15-49-41_193.jpeg)
![screen](https://raw.githubusercontent.com/tspannhw/Flow-SGP30-MLX90640/main/2023-02-07_15-49-46_973.jpeg)

## ImgUr Setup

![imgur](https://raw.githubusercontent.com/tspannhw/Flow-SGP30-MLX90640/main/images/imgurapi.jpg)

Create an imgur account and a client id.

## NiFi flow file

[https://github.com/tspannhw/Flow-SGP30-MLX90640/blob/main/flowfiles/MLX.json](https://github.com/tspannhw/Flow-SGP30-MLX90640/blob/main/flowfiles/MLX.json)





### See

https://www.catscloudsanddata.com/cats


### Talk

** It's Getting Hot in Here!

At last year's current event I monitored the temperature and other attributes at the conference. We'll do that as well and stream it through NiFi and Kafka. But, we'll scan anyone who wants to be thermal scanned during the talk live. I will bring a Raspberry Pi with a MLX90640 Thermal Camera that will capture thermal images of whoever wants, then sends the GIF to a local website (or IMGUR) for your download. I will generate a unique code along with some metadata that get's sent through Kafka and displayed on a real-time dashboard. Come and get your scan.

Everyone looks cool in thermal pixels, you can be next. This talk can be 10 minutes, 45 minutes or put me in the corner somewhere and I'll run this for a an hour or two.


#### Upload to imgur

https://apidocs.imgur.com/


#### Output Images

![img4](https://i.imgur.com/mHBeA0Z.gif)
![img3](https://i.imgur.com/qt8NEGe.gif)
![img2](https://i.imgur.com/MIzf4kP.gif)
![img1](https://i.imgur.com/TAQDvh8.gif)
![img5](https://i.imgur.com/IEl9RKy.gif)
![img6](https://i.imgur.com/mHlyKZ3.gif)
![img7](https://i.imgur.com/40E2HgJ.gif)
![img8](https://i.imgur.com/zMQSiLU.gif)
![img9](https://i.imgur.com/jXE56Qd.gif)

#### Output NiFi Attributes

```

Attribute Values
QueryRecord.Route
all
file.group
0
file.lastModifiedTime
2023-02-08T00:26:06+0000
file.owner
0
file.permissions
rw-r--r--
file.size
681219
filename
mlx90640-2023-02-07-19-26-05.gif
link
https://i.imgur.com/TAQDvh8.gif
mime.type
application/json
path
/opt/demo/images
post.header
{X-Cache=[MISS], Server=[cat factory 1.0], Access-Control-Allow-Origin=[*], Connection=[keep-alive], X-Ratelimit-Userlimit=[500], X-Post-Rate-Limit-Reset=[3130], X-Ratelimit-Clientreset=[86341], X-Ratelimit-Userreset=[3047], Date=[Wed, 08 Feb 2023 00:27:17 GMT], access-control-allow-methods=[GET, PUT, POST, PATCH, DELETE, OPTIONS], Access-Control-Allow-Headers=[Authorization, Content-Type, Accept, X-Mashape-Authorization, IMGURPLATFORM, IMGURUIDJAFO, sessionCount, IMGURMWBETA, IMGURMWBETAOPTIN, X-xfer2, X-Imgur-Defender-Bypass], X-Timer=[S1675816036.117081,VS0,VE1344], Accept-Ranges=[bytes], X-Frame-Options=[DENY], X-Ratelimit-Userremaining=[496], X-Post-Rate-Limit-Remaining=[1246], X-Served-By=[cache-ewr18160-EWR], Access-Control-Allow-Credentials=[true], X-Ratelimit-Clientlimit=[12500], Vary=[Accept-Encoding], X-Post-Rate-Limit-Limit=[1250], X-Cache-Hits=[0], X-Ratelimit-Clientremaining=[12497], Content-Type=[application/json; charset=utf-8]}
post.results
{"data":{"in_most_viral":false,"ad_type":null,"link":"https://i.imgur.com/TAQDvh8.gif","description":null,"section":null,"title":null,"type":"image/gif","deletehash":"g","datetime":1675816037,"has_sound":false,"id":"TAQDvh8","in_gallery":false,"vote":null,"views":0,"height":320,"bandwidth":0,"is_ad":false,"nsfw":null,"ad_url":null,"hls":"","tags":[],"mp4":"","account_id":null,"size":156602,"account_url":null,"name":"","width":240,"animated":false,"favorite":false},"success":true,"status":200}
post.status
OK
post.statuscode
200
record.count
1
sftp.listing.user
tspann
sftp.remote.filename
/opt/demo/images/mlx90640-2023-02-07-19-26-05.gif
sftp.remote.host
192.168.1.84
sftp.remote.port
22
uuid
fb7866a8-a764-4070-b27f-3f6ff02c8eb6


```

### ImgUr Post Results JSON Record

```
[{"filename":"mlx90640-2023-02-07-20-58-26.gif","file.lastModifiedTime":"2023-02-08T01:58:26+0000","link":"https://i.imgur.com/IEl9RKy.gif","uuid":"7af855a4-f482-45b1-ae00-42b464b24d46"}]

```

### Results All Attributes

```
{"flowfile.replay.timestamp":"Wed Feb 08 02:06:51 UTC 2023","postresults":"{\"data\":{\"in_most_viral\":false,\"ad_type\":null,\"link\":\"https://i.imgur.com/IEl9RKy.gif\",\"description\":null,\"section\":null,\"title\":null,\"type\":\"image/gif\",\"deletehash\":\"dhash\",\"datetime\":1675821563,\"has_sound\":false,\"id\":\"IEl9RKy\",\"in_gallery\":false,\"vote\":null,\"views\":0,\"height\":320,\"bandwidth\":0,\"is_ad\":false,\"nsfw\":null,\"ad_url\":null,\"hls\":\"\",\"tags\":[],\"mp4\":\"\",\"account_id\":null,\"size\":157816,\"account_url\":null,\"name\":\"\",\"width\":240,\"animated\":false,\"favorite\":false},\"success\":true,\"status\":200}","sftp.listing.user":"tspann","post.header":"{X-Cache=[MISS], Server=[cat factory 1.0], Access-Control-Allow-Origin=[*], Connection=[keep-alive], X-Ratelimit-Userlimit=[500], X-Post-Rate-Limit-Reset=[3538], X-Ratelimit-Clientreset=[80816], X-Ratelimit-Userreset=[3540], Date=[Wed, 08 Feb 2023 01:59:23 GMT], access-control-allow-methods=[GET, PUT, POST, PATCH, DELETE, OPTIONS], Access-Control-Allow-Headers=[Authorization, Content-Type, Accept, X-Mashape-Authorization, IMGURPLATFORM, IMGURUIDJAFO, sessionCount, IMGURMWBETA, IMGURMWBETAOPTIN, X-expD, X-Imgur-Defender-Bypass], X-Timer=[S1675821562.055686,VS0,VE1421], Accept-Ranges=[bytes], X-Frame-Options=[DENY], X-Ratelimit-Userremaining=[495], X-Post-Rate-Limit-Remaining=[1246], X-Served-By=[cache-nyc-kteb1890043-NYC], Access-Control-Allow-Credentials=[true], X-Ratelimit-Clientlimit=[12500], Vary=[Accept-Encoding], X-Post-Rate-Limit-Limit=[1250], X-Cache-Hits=[0], X-Ratelimit-Clientremaining=[12491], Content-Type=[application/json; charset=utf-8]}","file.group":"0","file.lastModifiedTime":"2023-02-08T01:58:26+0000","post.statuscode":"200","sftp.remote.filename":"/opt/demo/images/mlx90640-2023-02-07-20-58-26.gif","link":"https://i.imgur.com/IEl9RKy.gif","file.size":"671198","post.results":"{\"data\":{\"in_most_viral\":false,\"ad_type\":null,\"link\":\"https://i.imgur.com/IEl9RKy.gif\",\"description\":null,\"section\":null,\"title\":null,\"type\":\"image/gif\",\"deletehash\":\"DsQ0D65paRdWnVu\",\"datetime\":1675821563,\"has_sound\":false,\"id\":\"IEl9RKy\",\"in_gallery\":false,\"vote\":null,\"views\":0,\"height\":320,\"bandwidth\":0,\"is_ad\":false,\"nsfw\":null,\"ad_url\":null,\"hls\":\"\",\"tags\":[],\"mp4\":\"\",\"account_id\":null,\"size\":157816,\"account_url\":null,\"name\":\"\",\"width\":240,\"animated\":false,\"favorite\":false},\"success\":true,\"status\":200}","flowfile.replay":"true","file.permissions":"rw-r--r--","uuid":"6c0ea379-a548-45f8-9889-dcbf4ac7bb9a","path":"/opt/demo/images","filename":"mlx90640-2023-02-07-20-58-26.gif","post.status":"OK","file.owner":"0","sftp.remote.port":"22","sftp.remote.host":"192.168.1.84"}
```

#### Resources:

* https://raw.githubusercontent.com/tspannhw/minifi-gasthermal/master/mlx90640-2020-01-05-20-52-14.gif
* https://www.datainmotion.dev/2020/01/analyzing-wood-burning-stoves-with.html
* https://www.datainmotion.dev/2020/01/cloudera-edge2ai-minifi-java-agent-with.html
* https://www.datainmotion.dev/2019/03/posting-images-to-imgur-via-apache-nifi.html
* [https://github.com/tspannhw/nifi-postimage-processor](https://github.com/tspannhw/nifi-postimage-processor)
* [http://jsonpath.com/](http://jsonpath.com/)
* [https://www.catscloudsanddata.com/](https://www.catscloudsanddata.com/)
