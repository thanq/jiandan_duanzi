# -*- coding:utf-8 -*-

import os
import ConfigParser
from fileutil import get_current_python_file_path

cfg_file_path = get_current_python_file_path(__file__) + "/../config.cfg"

def get_current_download_page_num():
    config=ConfigParser.ConfigParser()
    with open(cfg_file_path, "r") as cfgfile:
        config.readfp(cfgfile)
        current_page_num = config.getint("current", "pagenum")
        return current_page_num


def set_current_download_page_num(num):
    config=ConfigParser.ConfigParser()
    with open(cfg_file_path, "r") as cfgfile:
        config.readfp(cfgfile)
    with open(cfg_file_path, "w") as cfgfile:
        config.set("current", "pagenum", str(num))
        config.write(cfgfile)


if __name__ == '__main__':

    set_current_download_page_num(1)

    pass
