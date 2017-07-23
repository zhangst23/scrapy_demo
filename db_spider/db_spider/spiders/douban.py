# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from db_spider.items import DbSpiderItem


class DoubanSpider(CrawlSpider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://www.douban.com/tag/%E6%8E%A8%E7%90%86/book?start=0']

    rules = (
        Rule(LinkExtractor(allow=r'start=\d{1,3}$'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # i = DbSpiderItem()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i
        items = []
        book_list = response.css('div.mod.book-list dl')
        for book in book_list:
            item = DbSpiderItem()
            try:
                item['book_name'] = book.xpath('dd/a/text()').extract()[0]
                item['book_star'] = book.xpath('dd/div[1]/span[1]/@class').extract()[0][7:]
                item['book_rating'] = book.xpath('dd/div[1]/span[2]/text()').extract()[0]
                item['book_eval'] = book.xpath('dd/div[1]/span[3]/text()').extract()[0]
                desc = book.xpath('dd/div[2]/text()').extract()[0].strip().split('/')
                item['book_price'] = desc.pop()
                item['book_publish_date'] = desc.po()
                item['book_publish'] = desc.po()
                item['book_author'] = '/'.join(desc)
            except:
                pass
            items.append(item)
        return items


'''
class DoubanSpider(CrawlSpider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['']
    rules = (
        Rule(LinkExtractor(allow=r'start=\d{1,3}$'), callback='parse_item', follow=True),
    )
    def parse_item(self, response):
        items = []
        book_list = response.css('')
        for book in book_list:
            item = DbSpiderItem()
            try:
                item['book_name'] = book.xpath('').extract()[0]
                item['book_eval'] = book.xpath('').extract()[0]
                desc = book.xpath('').extract()[0].strip().split('/')
                item['book_price'] = desc.pop()
                item['book_publish'] = desc.po()
                item['book_author'] = '/'.join(desc)
            except:
                pass
            items.append(item)
        return items

'''























