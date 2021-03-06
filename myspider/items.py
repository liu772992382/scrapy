# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()

class DoubanItem(scrapy.Item):
    info = scrapy.Field()
    title = scrapy.Field()
    rating_nums = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()


class DoubanMovieItem(scrapy.Item):
    name = scrapy.Field()
    rating_nums = scrapy.Field()
    url = scrapy.Field()


class ZhihuItem(scrapy.Item):
    followers = scrapy.Field()
    followees = scrapy.Field()
