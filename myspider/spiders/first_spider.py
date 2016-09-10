#coding=utf-8
import scrapy
import re
from myspider.items import *
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from scrapy.crawler import CrawlerProcess
# from auth import islogin,Logging
import cookielib

class ImgruSpider(scrapy.Spider):
    name = "imgru"
    start_urls = ['http://www.imgru.site']
    allowed_domins = ["douban.com"]
    def parse(self, response):
        filename = 'imgru_header'
        titles = re.findall(r'<h[0-9]+.*>',response.body)
        print titles
        with open(filename, 'wb') as f:
            for title in titles:
                yield MyspiderItem(title=title)
                f.write(title+'\n')

class MyCrawlSpider(CrawlSpider):
    name = 'MyCrawlSpider'
    start_urls = ['http://www.imgru.site']

    rules = (Rule(LinkExtractor(deny=(r'(.*login)')),callback='parse_item'),)

    def parse_item(self,response):
        self.logger.info('This is an item page! %s',response.url)

        item = MyspiderItem()
        item['title'] = response.xpath('//li[@class="active"]/a/text()').extract()
        return item


class Douban(CrawlSpider):
    name = 'Douban_book'
    start_urls = ['https://book.douban.com/top250']
    process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})
    rules = (Rule(LinkExtractor(allow=(r'.*start=.*')),callback='parse_item'),)



    def parse_item(self,response):
        self.logger.info('This is an item page! %s',response.url)

        item = DoubanItem()
        item['title'] = response.xpath('//div[@class="pl2"]//a/@title').extract()
        item['info'] = response.xpath('//td[@valign="top"]/p/text()').extract()
        item['rating_nums'] = response.xpath('//div/span[@class="rating_nums"]/text()').extract()
        item['image_urls'] = response.xpath('//a[@class="nbg"]/img/@src').extract()
        return item


class Zhihu(CrawlSpider):
    name = 'Zhihu'
    allower_domains = ['www.zhihu.com']
    start_urls = ['https://www.zhihu.com/people/liu-xiao-yu-5-83-32']
    process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

    rules = (Rule(LinkExtractor( allow = (r'\/people.*followees')), callback = 'followee_parse'),
            Rule(LinkExtractor( allow = (r'\/people.*followers')),callback = 'follower_parse'))

    def start_requests(self):
        # requests = requests.Session()
        # requests.cookies = cookielib.LWPCookieJar('cookies')
        #
        # # requests.cookies
        # try:
        #     requests.cookies.load(ignore_discard=True)
        # except:
        #     Logging.error(u"你还没有登录知乎哦 ...")
        #     Logging.info(u"执行 `python auth.py` 即可以完成登录。")
        #     raise Exception("无权限(403)")
        cookie_jar = cookielib.LWPCookieJar('cookies')
        print '\n\n\n'
        yield scrapy.Request(url = 'https://www.zhihu.com/people/liu-xiao-yu-5-83-32',cookies = cookie_jar,callback = None)#self.after_login)


    #def after_login(self,response)


    def followee_parse(self,response):
        self.logger.info('Followee : %s',response.url)

        item = ZhihuItem()
        item['followees'] = response.xpath('//a[@class="zg-link"]/@href').extract()
        return item


    def follower_parse(self,response):
        self.logger.info('Follower : %s',response.url)

        item = ZhihuItem()
        item['followers'] = response.xpath('//a[@class="zg-link"]/@href').extract()
        return item
