# -*- coding:utf-8 -*-
# import ConfigParser

import os


# config=ConfigParser.ConfigParser()
# with open(os.path.split(os.path.realpath(__file__))[0] + "/config.cfg","r") as cfgfile:
#     config.readfp(cfgfile)
#     host=config.get("redis","host")
#     password=config.get("redis","password")
#     port=config.getint("redis","port")
#     db=config.getint("redis","db")
#     max_connections=config.getint("redis","max_connections")
#     TEST= config.getboolean("test","test")

duanzi_zan_floor_redis_sort_set_name = 'duanzi_zan_floor_redis_sort_set'
duanzi_floor_with_rank_top_list_name = 'duanzi_floor_with_rank_top_list'
duanzi_floor_with_rank_for_web_top_list_name = 'duanzi_floor_with_rank_for_web_top_list'
all_floor_duanzi_hash_name = 'all_floor_duanzi_hash'



#每日新段子(新增的破百段子)
'''
1, 维护一个所有破百段子的列表
2, 判断是否在已经存在的破百段子列表里存在, 如果不存在, 加入破百段子列表, 然后在加入到今日新破百段子列表

结构: 全量破百段子列表 <段子floor - 日期>
     今日段子列表 <日期 - 段子floor数组>

新段子
    一个记录所有 破白段子(floor)的 hash
    一个按日期, 记录所有新段子的 list : date <-> json[]
    抓取数据: 该批次内破百段子
        --> 是否在存量破百段子中
            --> 如果不在, 加入

'''

#所有百赞段子 floor
duanzi_more_than_100_zan_floor_hash = 'duanzi_more_than_100_zan_floor_hash'
#某天新段list
duanzi_more_than_100_zan_list_pre = 'duanzi_more_than_100_zan_list_'




if os.environ.get('PRODUCTION') != "PRODUCTION":
     redis_conf_dict = {
        'host':'localhost',
        'port':6379,
        'password':None,
        'db':0,
        'max_connections':10
     }
else:
    redis_conf_dict = {
        'host':os.environ.get('REDIS_HOST'),
        'port':int(os.environ.get('REDIS_PORT')),
        'password':os.environ.get('REDIS_PASSWORD'),
        'db':int(os.environ.get('REDIS_DB')),
        'max_connections':int(os.environ.get('REDIS_MAX_CONNECTIONS'))
    }


