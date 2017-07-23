# -*- coding: utf-8 -*-
import scrapy
from demo.items import DemoItem()

class YunyingxSpider(scrapy.Spider):
    name = "yunyingx"
    allowed_domains = ["yunyingx.com"]
    start_urls = (
        'http://www.yunyingx.com/',
    )

    def parse(self, response):
        
        for sel in response.xpath(''):
	        item = DemoItem()

	        item['link'] = sel.xpath('')[0].extract()
	        url = response.urljoin(item['link'])
	        yield scrapy.Request(url, callback=self.parse_article)

    def parse_article(self, response):

        sel = respons.xpath('')
        item = DemoItem()
        item['title'] = sel.xpath('').extract()
        item['tags'] = sel.xpath('').extract()
        item['content'] = sel.xpath('').extract()
        print(item['title'],item['link'],item['content'])
        yield item









