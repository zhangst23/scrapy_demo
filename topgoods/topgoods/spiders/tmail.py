# -*- coding: utf-8 -*-
import scrapy


class TmailSpider(scrapy.Spider):
    name = "tmail"
    allowed_domains = ["tmail.com"]
    start_urls = (
        'http://www.tmail.com/',
    )

    def parse(self, response):
        pass
