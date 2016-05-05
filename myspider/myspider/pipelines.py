# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from model import *
import scrapy
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem


class DoubanPipeline(object):

    def __init__(self):
        self.session = DBSession()

    def process_item(self, item, spider):
        for i in range(len(item['title'])):
            book = douban_book()
            book.info = item['info'][i]#.encode('utf-8')
            book.title = item['title'][i]#.encode('utf-8')
            book.rating_nums = item['rating_nums'][i]#.encode('utf-8')
            self.session.add(book)
        self.session.commit()
        self.session.close()
        return item




class MyImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item
