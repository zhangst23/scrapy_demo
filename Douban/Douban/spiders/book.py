# -*- coding: utf-8 -*-
import scrapy
from Douban.items import DoubanItem

class BookSpider(scrapy.Spider):
    name = "book"
    allowed_domains = ["book.douban.com"]
    start_urls = (
        'https://book.douban.com/top250',
    )

    def parse_next(self, response):

        for item in response.xpath('//tr[@class="item"]'):
        	book = DoubanItem()
        	book['title'] = item.xpath('td[2]/div[1]/a/@title').extract_first()
        	book['info'] = item.xpath('td[2]/p/text()').extract_first()
        	book['rank'] = item.xpath('td[2]/div[2]/span[2]/text()').extract_first()
        	book['intro'] = item.xpath('td[2]/p/span[1]/text()').extract_first()
        	print book


    def parse(self,response):
    	yield Request(response.url, callback=self.parse_next)
    	for page in response.xpath('//div[@class="paginator"]/a'):
    		link = page.xpath('@href').extract_first()
    		yield Request(link, callback=self.parse_next)













