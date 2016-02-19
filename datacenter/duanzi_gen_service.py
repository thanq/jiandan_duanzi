# -*- coding:utf-8 -*-

from datetime import datetime
from util.jsonutil import json_to_dict, dict_to_json, list_to_json, json_to_list

from datacenter import redis_clent as r
from config import duanzi_floor_with_rank_top_list_name, duanzi_zan_floor_redis_sort_set_name, duanzi_floor_with_rank_for_web_top_list_name,\
    duanzi_all_more_than_100_zan_hash_name, duanzi_every_day_more_than_100_zan_hash_name , all_floor_duanzi_hash_name

def add_duanzi_json_to_all_duanzi_json_data(floor, json_str):
    r.hset(all_floor_duanzi_hash_name, floor, json_str)
    pass

def add_duanzi_zan_floor_redis_sort_set(zan, floor):
    r.zadd(duanzi_zan_floor_redis_sort_set_name, int(zan), int(floor))
    pass

def del_duanzi_redis_sort_set():
    r.delete(duanzi_zan_floor_redis_sort_set_name)

def gen_top_rank_duanzi_floor_list():
    l = r.zrangebyscore(name=duanzi_zan_floor_redis_sort_set_name, min=0, max=1000000, withscores=True, score_cast_func=int )
    top_list = l[::-1]
    r.delete(duanzi_floor_with_rank_top_list_name)
    for i in range(0, len(top_list)):
        r.rpush(duanzi_floor_with_rank_top_list_name, top_list[i][0])

def rename_top_list_name_for_web():
    if r.exists(duanzi_floor_with_rank_for_web_top_list_name):
        r.rename(duanzi_floor_with_rank_for_web_top_list_name, duanzi_floor_with_rank_for_web_top_list_name+"_bak")
    if r.exists(duanzi_floor_with_rank_top_list_name):
        r.rename(duanzi_floor_with_rank_top_list_name, duanzi_floor_with_rank_for_web_top_list_name)
    pass












def gen_today_top_duanzi_to_hash():
    today_str = datetime.now().strftime('%Y-%m-%d')
    del_today_top_duanzi_in_all_more_than_100_zan_hash(today_str)

    today_list = []
    l = r.zrangebyscore(name=duanzi_zan_floor_redis_sort_set_name, min=100, max=1000000, withscores=True, score_cast_func=int )
    old_top_dic = r.hgetall(duanzi_all_more_than_100_zan_hash_name)
    top_list = l[::-1]
    # if just_test(top_list):return
    for i in range(0, len(top_list)):
        dict_str =  top_list[i][0]
        item = json_to_dict(dict_str)
        floor = item.get('floor')
        if not old_top_dic.has_key(floor):
            #add to today list
            today_list.append(item)

    r.hset(duanzi_every_day_more_than_100_zan_hash_name, today_str, list_to_json(today_list))

def del_today_top_duanzi_in_all_more_than_100_zan_hash(day):
    if r.hexists(duanzi_every_day_more_than_100_zan_hash_name, day):
        today_duan_json = r.hget(duanzi_every_day_more_than_100_zan_hash_name, day)
        today_duan_list = json_to_list(today_duan_json)
        for duan_floor_dict in today_duan_list:
            floor = duan_floor_dict.get('floor')
            #删除今天的楼
            r.hdel(duanzi_all_more_than_100_zan_hash_name, floor)
            pass


def duanzi_top_list_gen_fail():
    return r.llen(duanzi_floor_with_rank_top_list_name) < 10000

def gen_toplist():
    pass

def get_key_when_no_today_key():
    return r.hkeys(duanzi_every_day_more_than_100_zan_hash_name)[0]

def get_oneday_100zan_req(day):
    return r.hget(duanzi_every_day_more_than_100_zan_hash_name,day)


