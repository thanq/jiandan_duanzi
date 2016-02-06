# -*- coding:utf-8 -*-

import os
from util.jsonutil import list_to_json_with_format, json_to_list

#得到当前python的目录(结尾不带 '/')  os.sep
def get_current_python_file_path(__file__):
    return os.path.split(os.path.realpath(__file__))[0]

_file_util_path = get_current_python_file_path(__file__)

page_date_file_path = _file_util_path + "/../page_data_file/"

#命令是从那个目录开始的(结尾不带 '/')
def get_cmd_path():
    return os.getcwd()

#得到入口python文件的目录(结尾不带 '/')
def get_begin_python_file_path():
    import sys
    return sys.path[0]


def save_json_list_str(page_num, crawl_time, duan_list):
    file_name = page_date_file_path + "page" + page_num + "_" + crawl_time
    with open(file_name, 'w') as f:
        f.write(list_to_json_with_format(duan_list).encode('utf8'))
    pass

def get_small_page_num(dir):
    files = os.listdir(dir)
    pass


if __name__ == '__main__':
    print page_date_file_path


