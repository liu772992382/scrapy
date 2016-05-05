#coding=utf-8
import scrapy
import re
from myspider.items import *
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from scrapy.crawler import CrawlerProcess

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
    name = 'Douban'
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
