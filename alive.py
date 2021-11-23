#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import sys
import ftp

if __name__ == '__main__':
    now = datetime.datetime.now()
    fnow = '{0:%Y%m%d%H%M}'.format(now)
    print("ALIVE " + fnow)
    path = sys.argv[1]
    server, username, password, src, dst = ftp.importConfig(path)
    ftp.uploadFTP( server, username, password, src+"alive.log", dst)
