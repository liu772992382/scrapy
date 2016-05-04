#coding=utf-8
import scrapy

class DmozSpider(scrapy.Spider):
    name = "first_spider"
    start_urls = ['http://www.imgru.site']

    def parse(self, response):
        filename = 'imgru'
        with open(filename, 'wb') as f:
            f.write(response.body)
