# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubantopmoviesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title_ch = scrapy.Field()
    rating_num = scrapy.Field()
    rating_count = scrapy.Field()
    image_urls = scrapy.Field()
    topid = scrapy.Field()
