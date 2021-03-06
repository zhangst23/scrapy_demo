# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DangdangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    _id = scrapy.Field()
    title = scrapy.Field()
    comments = scrapy.Field()
    time = scrapy.Field()
    press = scrapy.Field()
    price = scrapy.Field()
    discount = scrapy.Field()
    category1 = scrapy.Field()
    category2 = scrapy.Field()
