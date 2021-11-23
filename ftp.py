#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import datetime
from ftplib import FTP
import os
import socket
import json
import sys

class FTP_:
    def __init__(self, server, username, password):
        self.ftp = FTP(server,timeout=20)
        self.ftp.login(username, password)
        self.ftp.set_pasv(True) 
        #self.ftp.retrlines('LIST')
        while(self.internet_check() == False):
            print('waiting for internet connection...')
            time.sleep(1.0)
    def disconnect(self):
        self.ftp.quit()
        
    def internet_check(self, host="8.8.8.8", port=53, timeout=3):
        try:
            socket.setdefaulttimeout(timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
            print('conneceted to internet')
            return True
        except Exception as ex:
            print(ex.message)
            print('not connect to internet')
            return False

    def ftp_upload(self, src, dst):
        try:
            _file = open(src, 'rb')
            self.ftp.cwd('./')
            #basename = os.path.basename(src)
            basename_without_ext = os.path.splitext(os.path.basename(src))[0]
            now = datetime.datetime.now()
            fnow = '{0:%Y%m%d%H%M}'.format(now)
            fn = basename_without_ext + '_' + fnow + '.log'
            print(src + "->" + fn)
            self.ftp.storbinary('STOR ' + dst + fn, _file)
            _file.close()
            return 1
        except:
            return 0

def uploadFTP(server, username, password, src, dst):
    #アップロードするファイルの確認
    if(os.path.isfile(src) == False):
        print(src + " is not updated!")
        return 0
    ftp0 = FTP_(server, username, password)
    valid = ftp0.ftp_upload(src, dst)
    if(valid):#アップロードが完了したら、削除する。
        os.remove(src)
    return 1
    
if __name__ == '__main__':
    #Setting
    #jsonの読み込み。もしなければ終了
    if(os.path.isfile(sys.argv[1]) == False):
        print("Please set config.json as argv[1]")
        exit()
    f = open('config.json', 'r')
    json_data = json.load(f)
    #キーの有無を確認
    if('ftp' not in json_data):
        print("Please add ftp key in json file")
    if('server' not in json_data["ftp"]):
        print("Please add server key in ftp")
    if('name' not in json_data["ftp"]):
        print("Please add name key in ftp")
    if('password' not in json_data["ftp"]):
        print("Please add password key in ftp")
    if('src' not in json_data["ftp"]):
        print("Please add src key in ftp")
    if('dst' not in json_data["ftp"]):
        print("Please add dst key in ftp")
    server = json_data["ftp"]["server"]
    username = json_data["ftp"]["name"]
    password = json_data["ftp"]["password"]
    src = json_data["ftp"]["src"]
    dst = json_data["ftp"]["dst"]

    #alive.logのアップロード
    uploadFTP( server, username, password, src+"alive.log", dst)
    #water.logのアップロード
    uploadFTP( server, username, password, src+"water.log", dst)
    
    exit() 

