#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
if __name__ == '__main__':
    now = datetime.datetime.now()
    fnow = '{0:%Y%m%d%H%M}'.format(now)
    print("ALIVE " + fnow)
