# -*- coding: utf-8 -*-

import random
import scrapy
from scrapy.http import Request,FormRequest
from scrapy.selector import Selector
from util.dateutil import date_str_now_ymd
from jiandan_duanzi.settings import HEADER, COOKIES
from jiandan_duanzi.items import DuanziItem, JiandanDuanziPageItem
from util.fileutil import save_json_list_str
from util.configutil import get_current_download_page_num, set_current_download_page_num


def get_header():

    _header = HEADER.copy()

    # _header['Cookie'] = "Cookie:469981701=2; comment_author_596e6fb28c1bb47f949e65e1ae03f7f5=thanq; comment_author_email_596e6fb28c1bb47f949e65e1ae03f7f5=thanq%40126.com; human1353482284=1; voted_comments_3065075=1; 469981701=2; _ga=GA1.2.1939959636.1436526292; _gat=1; Hm_lvt_fd93b7fb546adcfbcf80c4fc2b54da2c=1455016396; Hm_lpvt_fd93b7fb546adcfbcf80c4fc2b54da2c=1455790356"
    _header['Cookie'] = "4699817" + str(random.randint(12, 90))+ "=4; Hm_lvt_fd93b7fb546adcfbcf80c4fc2b54da2c=1455790786; Hm_lpvt_fd93b7fb546adcfbcf80c4fc2b54da2c=1455790786; _ga=GA1.2.1070108839.1455790786; _gat=1"
    _header['User-Agent'] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/"+ str(random.randint(120, 550)) + "." + str(random.randint(12, 90)) + " (KHTML, like Gecko) Chrome/48.0.2564." + str(random.randint(420, 750))  + " Safari/537.36"

    return _header

class DuanziSpider(scrapy.Spider):

    name = "duanzi"
    allowed_domains = ["jandan.net"]
    start_urls = []

    handle_httpstatus_list = [403] #遇到403不要直接返回错误
    download_delay = 0.5#下载延迟 单位s

    def start_requests(self):
        '''
        通过该方法得到初始的request
        如果未指定callback, 会以parse为回调函数生成Request
        '''
        is_full_amount_spider = self.settings.get("is_full_amount_spider")

        current_num = get_current_download_page_num()

        if not is_full_amount_spider or current_num == 0:
            self.start_urls = ["http://jandan.net/duan/"]
        else:
            self.start_urls = ["http://jandan.net/duan/page-" + str(current_num) + "#comments"]
            pass

        for i, url in enumerate(self.start_urls):

            header = get_header()

            yield FormRequest(url,
                              # meta = {'cookiejar': i},
                              headers = get_header(),
                              # cookies = COOKIES,
                              callback = self.parse_item)

    def gen_next_request(self, url):
        return FormRequest(url,  headers=get_header(), callback=self.parse_item)

    def gen_duanzi_item_by_selector(self, dz_selector):
        #作者
        auther = ''.join( dz_selector.xpath("//div[@class='author']/strong/text()").extract() )
        #楼层
        floor = ''.join( dz_selector.xpath("//div[@class='text']/span[@class='righttext']/a/text()").extract() )
        #链接
        url = ''.join( dz_selector.xpath("//div[@class='text']/span[@class='righttext']/a/@href").extract() )
        # 内容
        content = ''.join( dz_selector.xpath("//div[@class='text']/p/text()").extract() )
        #赞/反对
        zan, against =  dz_selector.xpath("//div[@class='text']/div/span/text()").extract()
        #发布时间
        publish_time = ''.join( dz_selector.xpath("//div[@class='author']/small/a/text()").extract() )

        publish_time = publish_time.upper()

        if publish_time.find('HOURS')  != -1  or publish_time.find('MINS') != -1:
            publish_time = '@IN ONE DAY'

        return {"auther":auther, "content":content, "floor":floor, "url":url,
                         "zan":zan, "against":against, "publish_time":publish_time}

    def parse_item(self, response):

        page_num = self.get_page_num_from_url(response.url)
        crawl_time = date_str_now_ymd() #当前时间

        if response.status != 200:
            print '#' * 100
            print str(response.status)
            print '#' * 100
            print str(response.body)
            print '#' * 100
            #todo yield handle_captcha(self, response)

        selector = Selector(response)

        duan_list = []

        for dz_selector in selector.xpath("//div[@class='row']"):
            dz_selector = Selector(text=dz_selector.extract())
            duan_list.append( self.gen_duanzi_item_by_selector(dz_selector) )

        #将段子的json保存到文件
        save_json_list_str(page_num, crawl_time, duan_list)

        if page_num == '1':
            page_num = '0'

        set_current_download_page_num(page_num)

        next_url = "".join(selector.xpath(
            "/html/body/div[@id='wrapper']/div[@id='body']/div[@id='content']/div[@id='comments']/div[@class='comments'][1]/div[@class='cp-pagenavi']/a[@class='previous-comment-page']/@href"
        ).extract())


        if next_url:
            yield self.gen_next_request(next_url)
        print 50*'*'
        pass

    def parse(self, response):
        '''
        返回 Item 对象、dict、 Request 或者一个包括他们的可迭代容器
        分析返回的response内容
        当response没有指定回调函数时，该方法是Scrapy处理下载的response的默认方法。
        '''
        pass


    def get_page_num_from_url(self, url):
        import re
        pagenum_arr = re.findall('\d+', url)
        if len(pagenum_arr) == 0:
            return '0'
        return pagenum_arr[0]



