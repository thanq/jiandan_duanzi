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


duanzi_more_than_100_zan_list_name = 'duanzi_more_than_100_zan_list'
duanzi_all_more_than_100_zan_hash_name = 'duanzi_all_more_than_100_zan_hash'
duanzi_every_day_more_than_100_zan_hash_name = 'duanzi_every_day_more_than_100_zan_hash'




if os.environ.get('REDIS_HOST') != "PRODUCTION":
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


