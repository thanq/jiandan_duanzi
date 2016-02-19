# -*- coding:utf-8 -*-

import redis
from config import redis_conf_dict

pool = redis.ConnectionPool(
    host=redis_conf_dict.get('host'),
    port=redis_conf_dict.get('port'),
    password=redis_conf_dict.get('password'),
    db=redis_conf_dict.get('db'),
    max_connections=redis_conf_dict.get('max_connections')
)
redis_clent = redis.StrictRedis(connection_pool=pool)

# print redis_clent.info()

r = redis.StrictRedis(connection_pool=pool)

def bgsave_reids():
    r.bgsave()

