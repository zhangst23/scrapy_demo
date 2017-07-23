# -*- coding: utf-8 -*-
import scrapy
from hacknews.items import HacknewsItem

class HnSpider(scrapy.Spider):
    name = "hn"
    allowed_domains = ["news.ycombinator.com"]
    start_urls = (
        'http://www.news.ycombinator.com/',
    )

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//td[@class="title"]')
        for site in sites:
        	title = site.xpath('a/text()').extract()
        	link = site.xpath('a/@href').extract()
        	print title, link