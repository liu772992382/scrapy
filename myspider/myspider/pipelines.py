# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from model import *



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
        print 'session commit finished'
        return item
