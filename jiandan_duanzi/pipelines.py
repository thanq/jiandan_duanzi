# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from datacenter.duanzi_gen_service import check_and_save_morethan100zan_duanzi, r


class JiandanDuanziPipeline(object):
    def process_item(self, item, spider):
        pass


class NewJiandanDuanziPipeline(object):
    def process_item(self, item, spider):

        zan =  int(item['zan'])
        floor = int(item['floor'])

        if zan >= 120 :
            check_and_save_morethan100zan_duanzi(floor, item['content'])

        return item




for i in r.lrange('duanzi_more_than_100_zan_list_2016-04-22', 0, 100):
    print i
    print