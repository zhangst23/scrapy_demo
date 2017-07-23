# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings
from .items import DangdangItem, PicItem


class DangdangPipeline(object):
		def __init__(self):
			host = setting['MONGODB_HOST']
			port = setting['MONGODB_PORT']
			db_name = settings['MONGODB_DANAME']
			client = pymongo.MongoClient(host=host,port=port)
			tdb = client[db_name]
			self.post = tdb[settings['MONGODB_DOCNAME']]


    def process_item(self, item, spider):
        # 先判断item类型，再放入相应数据库
        if isinstance(item, DangdangItem):
        	try:
        		book_info = dict(item)
        		if self.port.insert(book_info):
        			print('sssss')
        	except Exception:
        		pass

        return item
















