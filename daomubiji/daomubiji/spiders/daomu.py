# coding:utf-8

import scrapy
from scrapy import Selector
from scrapy import Request
from daomubiji.items import ChapterItem


class DaoMu(scrapy.Spider):
	name = "daomu"
	host = "http://www.lread.net"
	start_urls = ["http://www.lread.net/read/70",]
	def parse(self, response):
		selector = Selector(response)
		content_list = selector.xpath('//dd/a')
		for content in content_list:
			title = content.xpath('@title').extract_first()
			url = self.host + content.xpath('@href').extract_first()
			item = ChapterItem()
			item['title'] = title
			item['url'] = url
			# scrapy会把这个item交给pipeline处理
			yield item


'''

class DaoMu(scrapy.Spider):
	name = "daomu"
	host = "http://www.qidian.com"
	start_urls = ["http://www.qidian.com/read/90"]

	def parse(self, response):
		item = ChapterItem()
		for content in response.xpath(''):
			item['title'] = content.xpath('').extract_first()
			item['url'] = self.host + content.xpath('@href').extract_first()
			yield item

'''



















