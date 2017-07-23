# -*- coding: utf-8 -*-
import scrapy
import requests
from scrapy import Selector
from lxml import etree
from ..items import DangdangItem
from scrapy_redis.spider import RedisSpider


class DangdnagSpider(RedisSpider):
    name = "dangdnagspider"
    redis_key = 'dangdangspider:urls'
    allowed_domains = ["dangdang.com"]
    start_urls = 'http://category.dangdang.com/cp01.00.00.00.00.00.00.html'
    
    def start_requests(self):
    	user_agent = ''
    	headers = {'User-Agent': user_agent}
    	yield scrapy.Request(url=self.start_urls, headers=headers, method='GET', callback=self.parse)

    def parse(self, response):
        user_agent = ''
        headers = {'User-Agent': user_agent}
        lists = response.body.decode('gbk')
        selector = etree.HTML(lists)
        goodslist = selector.xpath('//')
        for goods in goodslist:
        	try:
        		category_big = goods.xpath('').pop().replace(' ', '')
        		category_big_id = goods.xpath('').pop().split('.')[1]
        		category_big_url = "".\
        											format(str(category_big_id))
        		yield scrapy.Request(url=category_big_url, headers=headers, callback=self.detail_parse, meta={"ID1":category_big_id,"ID2":category_big})

        	except Exception:
        		pass

      def detail_parse(self, response):
        '''
        ID1:大种类ID   ID2:大种类名称   ID3:小种类ID  ID4:小种类名称
        '''
        url = ''.format(response.meta["ID1"])
        category_small = requests.get(url)
        contents = etree.HTML(category_small.content.decode('gbk'))
        goodslist = contents.xpath('')
        for goods in goodslist:
        	try:
        		category_small_name = goods.xpath('').pop().replace(" ", "").split('(')[0]
        		category_small_id = goods.xpath('').pop().split('.')[2]
        		category_small_url = "".format(str(response.meta["ID1"]),str(category_small_id))
        		yield scrapy.Request(url=category_small_url, callback=self.third_parse, meta={"ID1":response.meta["ID1"],"ID2":response.meta["ID2"],"ID3":category_small_id,"ID4":category_small_name})
        	except Exception:
        		pass

      def third_parse(self,response):
      	for i in range(1,101):
      		url = 'http://'.format(str(i), response.meta["ID1"],response.meta["ID3"])
      		try:
      			contents = requests.get(url)
      			contents = etree.HTML(contents.content.decode('gbk'))
      			goodslist = contents.xpath('')
      			for goods in goodslist:
      				item = DangdangItem()
      				try:
      					item['comments'] = goods.xpath('').pop()
      					item['title'] = goods.xpath('').pop()
      					item['time'] = goods.xpath('').pop()
      					item['price'] = goods.xpath('').pop()
      					item['discount'] = goods.xpath('').pop()
      					item['category1'] = response.meta["ID4"]
      					item['category2'] = response.meta["ID2"]
      				except Exception:
      					pass
      				yield item
      		except Exception:
      			pass
































