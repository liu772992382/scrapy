#coding=utf-8
import scrapy
import re
from myspider.items import MyspiderItem
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

class ImgruSpider(scrapy.Spider):
    name = "imgru"
    start_urls = ['http://www.imgru.site']

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

    rules = (Rule(LinkExtractor(allow=()),callback='parse_item'),)

    def parse_item(self,response):
        self.logger.info('This is an item page! %s',response.url)

        item = MyspiderItem()
        item['title'] = response.xpath('//li[@class="active"]/a/text()')
        return item
