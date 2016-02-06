# -*- coding:utf-8 -*-

import json


def json_to_dict(jstr):
    return json.loads(jstr, encoding='utf8')
    pass

def json_to_list(jstr):
    return json.loads(jstr, encoding='utf8')
    pass

def dict_to_json(dic):
    return json.dumps(dic, encoding='utf8', ensure_ascii=False)
    pass

def list_to_json(li):
    return json.dumps(li, encoding='utf8', ensure_ascii=False)
    pass

def list_to_json_with_format(li):
    return json.dumps(li, encoding='utf8', ensure_ascii=False, indent=2)
    pass


