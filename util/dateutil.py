# -*- coding:utf-8 -*-

from datetime import datetime
import time

date_format_str = '%Y-%m-%d %H:%M:%S'

def date_str_now(date_format_str=date_format_str):
    return datetime.now().strftime(date_format_str)

def date_str_now_ymd():
    return datetime.now().strftime('%Y_%m_%d')

def msvalue_to_date_str(msvalue, date_format_str=date_format_str):
    return time.strftime(date_format_str, time.localtime( float(msvalue) / 1000) )
