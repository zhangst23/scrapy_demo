# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DbSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book_name = scrapy.Field()
    book_star = scrapy.Field()
    book_rating = scrapy.Field()
    book_eval = scrapy.Field()
    book_author = scrapy.Field()
    book_publish = scrapy.Field()
    book_price = scrapy.Field()
