# -*- coding:utf-8 -*-

from datetime import datetime

def date_str_now():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def date_str_now_ymd():
    return datetime.now().strftime('%Y_%m_%d')

