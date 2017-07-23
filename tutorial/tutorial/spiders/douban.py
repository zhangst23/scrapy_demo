# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from ..items import TutorialItem


class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["douban.com"]
    start_urls = (
        'https://book.douban.com/tag/%E6%BC%AB%E7%94%BB?start=0&type=T',
    )

    def parse(self, response):
        item = TutorialItem()
        for sel in response.css('#subject_list > ul > li > div.info'):
        	item['title'] = sel.css('h2 > a::text').extract_first()
        	item['link'] = sel.css('h2 > a::attr(href)').extract_first()
        	item['info'] = sel.css('div.pub::text').extract_first()
        	item['desc'] = sel.css('p::text').extract_first()
        	yield item
