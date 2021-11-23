#!/bin/bash
cd /home/pi/workspace/WateringSystem
python water.py config.json > ./log/water.log
python ftp.py config.json water.log
