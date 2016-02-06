# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request,FormRequest
from scrapy.selector import Selector
from util.dateutil import date_str_now_ymd
from jiandan_duanzi.settings import HEADER, COOKIES
from jiandan_duanzi.items import DuanziItem, JiandanDuanziPageItem
from util.fileutil import save_json_list_str
from util.configutil import get_current_download_page_num, set_current_download_page_num



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
            yield FormRequest(url,
                              # meta = {'cookiejar': i},
                              headers = HEADER,
                              # cookies = COOKIES,
                              callback = self.parse_item)

    def gen_next_request(self, url):
        return FormRequest(url,  headers=HEADER, callback=self.parse_item)

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



