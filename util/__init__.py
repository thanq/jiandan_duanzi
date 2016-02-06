# -*- coding:utf-8 -*-

def get_dict_from_module(t):
    # import my_jd.settings as t
    _d = {}
    for i in  dir(t):
        if not i.startswith("_"):
            _d[i] = getattr(t, i)
    return _d

