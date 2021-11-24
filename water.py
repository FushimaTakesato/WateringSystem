#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import datetime
def giveWater():
    try:
        GPIO.setmode(GPIO.BOARD)
        RELAY = 11
        GPIO.setup(RELAY, GPIO.OUT)
        GPIO.output(RELAY, True)
        time.sleep(2.0)
        GPIO.output(RELAY, False)
        GPIO.cleanup(RELAY)
        return 1
    except:
        return 0
if __name__ == '__main__':
    flag = giveWater()
    now = datetime.datetime.now()
    fnow = '{0:%Y%m%d%H%M}'.format(now)
    if(flag):
        print(fnow)
