# -*- coding:utf-8 -*-
from scrapy.crawler import CrawlerProcess
import time

from util import get_dict_from_module
from  jiandan_duanzi.spiders.newduan_everyday import NewDuanziSpider


def main():
    crawl_duanzi()


'''
一会儿执行一次
新段子
一个记录所有 破白段子(floor)的 map
一个按日期, 记录所有新段子的 list : date <-> json[]
抓取数据: 该批次内破百段子
    --> 是否在存量破百段子中
        --> 如果不在, 加入


'''

def crawl_duanzi():
    #爬虫开始
    import jiandan_duanzi.settings as s
    s.ITEM_PIPELINES = {'jiandan_duanzi.pipelines.NewJiandanDuanziPipeline':100}
    setting_dict = get_dict_from_module(s)
    setting_dict['is_full_amount_spider'] = True
    setting_dict['DEPTH_LIMIT'] = 10

    process = CrawlerProcess(setting_dict)
    process.crawl(NewDuanziSpider)
    process.start() # the script will block here until the crawling is finished

    print '@'*100
    pass


if __name__ == '__main__':
    main()


'''
使用user agent池，轮流选择之一来作为user agent。池中包含常见的浏览器的user agent(google一下一大堆)
禁止cookies(参考 COOKIES_ENABLED)，有些站点会使用cookies来发现爬虫的轨迹。
设置下载延迟(2或更高)。参考 DOWNLOAD_DELAY 设置。
如果可行，使用 Google cache 来爬取数据，而不是直接访问站点。
使用IP池。例如免费的 Tor项目 或付费服务(ProxyMesh)。
使用高度分布式的下载器(downloader)来绕过禁止(ban)，您就只需要专注分析处理页面。这样的例子有: Crawlera
'''




