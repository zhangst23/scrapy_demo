# coding:utf-8

import scrapy
from scrapy.selector import Selector 
from scrapy import Request
from douban_movies.items import Tutorial2Item
import urllib.request 
import re
import json

class doubanSpider(scrapy.Spider):
	name = 'douban'
	allowed_domains = ['douban.com']
	start_list = []
	for i in range(1,14):
		url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=' + str(i*20)
		start_list.append(url)
	start_urls = start_list


	def start_requests(self):
		user_agent = ''
		headers = {'User-Agent': user_agent}
		for url in self.start_urls:
			yield scrapy.Request(url=url, headers=headers, method='GET', callback=self.parse)

	def parse(self, response):
		hxs = response.body.decode('utf-8')
		hjson = json.loads(hxs)
		for lis in hjson['subjects']:
			item = Tutorial2Item()
      item["info"] = lis['url']
      item["pic"] = lis['cover']
      item["score"] = lis['rate']
      item["title"] = lis['title']
      filename = item["title"] + '_' + item["score"] + '分' + '.jpg'
      urllib.request.urlretrieve(item["pic"], filename)
      yield item



















