# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from util.jsonutil import dict_to_json


class JiandanDuanziPageItem(scrapy.Item):
    duanzi_list_json = scrapy.Field()
    page_num = scrapy.Field()
    crawl_time = scrapy.Field()
    pass

    def tojson(self):
        return dict_to_json(dict(self))


class DuanziItem(scrapy.Item):
    auther = scrapy.Field()
    content = scrapy.Field()
    floor = scrapy.Field()
    url = scrapy.Field()
    zan = scrapy.Field()
    against = scrapy.Field()
    publish_time = scrapy.Field()
    # crawl_time = scrapy.Field()

    def tojson(self):
        return dict_to_json(dict(self))

    def __repr__(self):
        return self.tojson()

