# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from daomubiji.items import ChapterItem
# import csv
from scrapy.conf import settings
import pymongo


class DaomubijiPipeline(object):
    # def process_item(self, item, spider):
    # 	if isinstance(item, ChapterItem):
    # 		csvfile = open('result.csv', 'ab')
    # 		data = [item['title'].encode('utf8'), item['url']]
    # 		writer = csv.writer(csvfile)
    # 		writer.writerow(data)
    # 		csvfile.close()
    #   return item


    def process_item(self, item, spider):
    	connection = pymongo.MongoClient(settings['MONGODB_HOST'], settings['MONGODB_PORT'])
    	db = connection[settings['MONGODB_DB']]
    	collection = db[settings['MONGODB_COLLECTION']]
    	item['title'] = item['title'].encode('utf8')
    	collection.insert(dict(item))
    	return item









