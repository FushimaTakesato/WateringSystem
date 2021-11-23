# Name

自動水やりシステム

# DEMO

（デモ動画や図表）

# Features

（特徴、優れているところ）
* 1日に1回、ポンプを動かして水を流す。
* 5分に1回、動いているかログをとる
* 1日に1回、サーバーにアップロードする

# Requirement

* RPi.GPIO 0.7.0

# Installation

```bash
pip install RPi.GPIO
```

# Usage

* crontabで起動時間を設定する  
(例)午前10時にwater.pyを起動する。5分おきにalive.pyを起動する。12時にftp.pyを起動する。

```bash
$ crontab -e
# m h  dom mon dow   command
0 10 * * * python {path to this repository}/water.py >> {path to this repository}/log/water.log
0/5 * * * * python {path to this repository}/alive.py >> {path to this repository}/log/alive.log
```
* FTPの設定  
(例)

```bash
$ vi config.json
{
  "ftp":{
    "server": "IP or ***.com",
    "name": "username" ,
    "password": "password"
    "src": "~/workspace/WateringSystem/log/alive.log",
    "dst": "www/flower/log/" 
  }
}
```

# Note


 
# Author

* Fushima Takesato
* takenokonosato.f@gmail.com
 
# License

 
