# -*- coding:utf-8 -*-
import os

root_path = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    PAGE_SIZE = 25
    '''
    生成 secret_key 的方式 :
    import os
    print os.urandom(24)
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    # SECRET_KEY = '\x11\xcaF\xfc6\xe8/\xf7\xeey\xdc\x97|:\xf3\x9c\\I\x9dl=\xc8\x00>'
    # SQLALCHEMY_DATABASE_URI = 'mysql://scott:tiger@localhost/mydatabase'
    LOG_FILE = '/tmp/jd_web.log'


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    # DEBUG = False
    DEBUG = True



class TestingConfig(Config):
    TESTING = True
