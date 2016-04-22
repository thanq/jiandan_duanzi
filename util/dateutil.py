# -*- coding:utf-8 -*-

from datetime import datetime as ddt
import time

date_format_str = '%Y-%m-%d %H:%M:%S'

def date_str_now(date_format_str=date_format_str):
    return ddt.now().strftime(date_format_str)

def date_str_now_ymd():
    return ddt.now().strftime('%Y-%m-%d')

def msvalue_to_date_str(msvalue, date_format_str=date_format_str):
    return time.strftime(date_format_str, time.localtime( float(msvalue) / 1000) )


if __name__ == '__main__':
    import datetime
    theday = datetime.datetime.strptime("2015-12-01",'%Y-%m-%d')
    day28 = datetime.timedelta(days=28)
    _next_10_days = [(theday + day28 * i).strftime('%Y-%m-%d') for i in range(1, 10)]
    for i in _next_10_days : print(i)

    print date_str_now_ymd()