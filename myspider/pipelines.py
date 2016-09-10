# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from model import *
import scrapy
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
import hashlib

class DoubanPipeline(object):

    def __init__(self):
        self.session = DBSession()

    def process_item(self, item, spider):
        # for i in range(len(item['title'])):
        book = douban_book()
        book.info = item['info']#.encode('utf-8')
        book.title = item['title']#.encode('utf-8')
        if item['rating_nums'] == []:
            book.rating_nums = 0
        else:
            book.rating_nums = book.rating_nums = item['rating_nums'][0]
        # book.img_id = hashlib.sha1(item['image_urls'][0]).hexdigest()
        self.session.add(book)
        self.session.commit()
        self.session.close()
        return item




class MyImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)

    # def item_completed(self, results, item, info):
    #     image_paths = [x['path'] for ok, x in results if ok]
    #     if not image_paths:
    #         raise DropItem("Item contains no images")
    #     item['image_paths'] = image_paths
    #     return item



#class ZhihuPipeline(object):

    #def __intit__
