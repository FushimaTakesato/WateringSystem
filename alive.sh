#!/bin/bash
cd /home/pi/workspace/WateringSystem
python alive.py config.json > ./log/alive.log
python ftp.py config.json alive.log
