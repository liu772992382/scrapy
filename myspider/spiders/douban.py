#coding=utf-8
import scrapy
import re
from myspider.items import *
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from scrapy.crawler import CrawlerProcess
import cookielib

class Douban(CrawlSpider):
    name = 'Douban_movie'
    start_urls = ['https://movie.douban.com/tag/']
    process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})
    rules = (Rule(LinkExtractor(allow=(r'http.:\/\/movie.douban.com\/subject.*'),deny=(r'http.:\/\/movie.douban.com\/subject\/\d*\/cinema.*')),callback='parse_item'),
    Rule(LinkExtractor(allow=(r'http.:\/\/movie.douban.com.*'),deny=(r'http.:\/\/movie.douban.com\/review.*',r'http.:\/\/movie.douban.com\/subject\/\d*\/cinema.*')),follow = True))



    def parse_item(self,response):
        self.logger.info('This is an item page! %s',response.url)

        item = DoubanItem()
        item['title'] = response.xpath('//span[@property="v:itemreviewed"]/text()').extract()[0]
        item['info'] = response.xpath('//div[@id="info"]/span/span[@class="attrs"]/a/text()').extract()[0]
        item['rating_nums'] = response.xpath('//strong[@property="v:average"]/text()').extract()
        # item['image_urls'] = response.xpath('//img[@rel="v:image"]/@src').extract()
        return item
