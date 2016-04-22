# -*- coding:utf-8 -*-

from datetime import datetime
from util.jsonutil import json_to_dict, dict_to_json, list_to_json, json_to_list

from datacenter import redis_clent as r
from config import duanzi_floor_with_rank_top_list_name, duanzi_floor_with_rank_for_web_top_list_name,\
    duanzi_more_than_100_zan_floor_hash, all_floor_duanzi_hash_name


def total_counts():
    return r.llen(duanzi_floor_with_rank_for_web_top_list_name)

# for web
def get_duanzi_by_page(page, page_size):
    floors =   r.lrange(duanzi_floor_with_rank_for_web_top_list_name,
                                              (page -1)*page_size,
                                              (page*page_size - 1))
    if floors != []:
        req =  [ json_to_dict(jsonstr) for jsonstr in  r.hmget(all_floor_duanzi_hash_name, floors)]
        rank = (page -1)*page_size
        for i in req:
            i['rank'] = rank + 1
            rank = rank + 1
        return req
    else:
        return []


# def del_duanzi_redis_sort_set():
#     r.delete(duanzi_redis_sort_set_name)

#
# def del_today_top_duanzi_in_all_more_than_100_zan_hash(day):
#     if r.hexists(duanzi_every_day_more_than_100_zan_hash_name, day):
#         today_duan_json = r.hget(duanzi_every_day_more_than_100_zan_hash_name, day)
#         today_duan_list = json_to_list(today_duan_json)
#         for duan_floor_dict in today_duan_list:
#             floor = duan_floor_dict.get('floor')
#             #删除今天的楼
#             r.hdel(duanzi_all_more_than_100_zan_hash_name, floor)
#             pass


def rename_top_list_name_for_web():
    if r.exists(duanzi_floor_with_rank_for_web_top_list_name):
        r.rename(duanzi_floor_with_rank_for_web_top_list_name, duanzi_floor_with_rank_for_web_top_list_name+"_bak")
    if r.exists(duanzi_floor_with_rank_top_list_name):
        r.rename(duanzi_floor_with_rank_top_list_name, duanzi_floor_with_rank_for_web_top_list_name)
    pass

def duanzi_top_list_gen_fail():
    return r.llen(duanzi_floor_with_rank_top_list_name) < 10000

def gen_toplist():
    pass
#
# def get_key_when_no_today_key():
#     return r.hkeys(duanzi_every_day_more_than_100_zan_hash_name)[0]
#
# def get_oneday_100zan_req(day):
#     return r.hget(duanzi_every_day_more_than_100_zan_hash_name,day)
#

