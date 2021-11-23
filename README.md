# Name

自動水やりシステム

# DEMO

（デモ動画や図表）

# Features

* 1日に1回、ポンプを動かして水を流す。
* 5分に1回、動いているかログをとる。
* 各処理の後、サーバーにアップロードする。

# Requirement

* RPi.GPIO 0.7.0

# Installation

```bash
pip install RPi.GPIO
```

# Usage

* crontabで起動時間を設定する  
(例)午前10時にwater.pyを起動する。5分おきにalive.pyを起動する。

```bash
$ git fetch
$ git pull
$ crontab -e
# m h  dom mon dow   command
0 10 * * * python {path to this repository}/water.py  [path to config.json]/config.json > {path to this repository}/log/water.log
*/1 * * * * python {path to this repository}/alive.py  [path to config.json]/config.json > {path to this repository}/log/alive.log
```
* FTPの設定  
config.jsonを下記のように作成し、ソースコードと同じフォルダに保存する。  

```bash
$ vi config.json
{
  "ftp":{
    "server": "IP or ***.com",
    "name": "username" ,
    "password": "password",
    "src": "~/workspace/WateringSystem/log/",
    "dst": "www/flower/log/" 
  }
}
```

# Note


 
# Author

* Fushima Takesato
* takenokonosato.f@gmail.com
 
# License

 
