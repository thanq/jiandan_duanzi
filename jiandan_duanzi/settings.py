# -*- coding: utf-8 -*-

# Scrapy settings for jiandan_duanzi project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'jiandan_duanzi'

SPIDER_MODULES = ['jiandan_duanzi.spiders']
NEWSPIDER_MODULE = 'jiandan_duanzi.spiders'


DOWNLOAD_DELAY = 1
CONCURRENT_REQUESTS = 1 #Scrapy downloader 并发请求(concurrent requests)的最大值
CONCURRENT_REQUESTS_PER_DOMAIN = 1

CONCURRENT_ITEMS = 1 #同时处理(每个response的)item的最大值

COOKIES_ENABLED = False
COOKIES_DEBUG = True

RETRY_ENABLED = False

# REDIRECT_ENABLED = False
DEPTH_LIMIT = 10000 #爬取深度


ITEM_PIPELINES = {
    # 'jiandan_duanzi.pipelines.JiandanDuanziPipeline':100 #100 为运行顺序
}


# LOG_FILE='scrapy.log'

HEADER={
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"Accept-Encoding":"gzip, deflate, sdch",
"Accept-Language":"zh-CN,zh;q=0.8",
"Cache-Control":"no-cache",
"Connection":"keep-alive",
"Cookie":"469981701=1; Hm_lvt_fd93b7fb546adcfbcf80c4fc2b54da2c=1455790786; Hm_lpvt_fd93b7fb546adcfbcf80c4fc2b54da2c=1455790786; _ga=GA1.2.1070108839.1455790786; _gat=1",
"Host":"jandan.net",
"Pragma":"no-cache",
"Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.103 Safari/537.36"
}

DEFAULT_REQUEST_HEADERS = HEADER

COOKIES={
    "1353482284":"13",
    # "comment_author_596e6fb28c1bb47f949e65e1ae03f7f5":"thanq",
    # "comment_author_email_596e6fb28c1bb47f949e65e1ae03f7f5":"thanq%40126.com",
    "_gat":"1",
    "1353482284":"15",
    "Hm_lvt_fd93b7fb546adcfbcf80c4fc2b54da2c":"1449491580",
    "Hm_lpvt_fd93b7fb546adcfbcf80c4fc2b54da2c":"1450668744",
    "_ga":"GA1.2.1939959636.1436526292"

}





# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'jiandan_duanzi (+http://www.yourdomain.com)'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS=32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY=3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN=16
#CONCURRENT_REQUESTS_PER_IP=16

# Disable cookies (enabled by default)
#COOKIES_ENABLED=False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED=False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'jiandan_duanzi.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'jiandan_duanzi.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'jiandan_duanzi.pipelines.SomePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# NOTE: AutoThrottle will honour the standard settings for concurrency and delay
#AUTOTHROTTLE_ENABLED=True
# The initial download delay
#AUTOTHROTTLE_START_DELAY=5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY=60
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG=False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED=True
#HTTPCACHE_EXPIRATION_SECS=0
#HTTPCACHE_DIR='httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES=[]
#HTTPCACHE_STORAGE='scrapy.extensions.httpcache.FilesystemCacheStorage'
