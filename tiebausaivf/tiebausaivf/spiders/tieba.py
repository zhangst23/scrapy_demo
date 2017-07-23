# -*- coding: utf-8 -*-
import scrapy
from tiebausaivf.items import TiebausaivfItem


class TiebaSpider(scrapy.Spider):
    name = "tieba"
    allowed_domains = ["tieba.baidu.com"]
    start_urls = (
        'https://tieba.baidu.com/f?kw=%E7%BE%8E%E5%9B%BD%E8%AF%95%E7%AE%A1%E5%A9%B4%E5%84%BF&ie=utf-8&pn=50',
    )
    def parse(self, response):

			for sel in response.xpath('//*[@id="thread_list"]/li[7]/div'):
				item = TiebausaivfItem()
				item['title'] = sel.xpath('/div[2]/div[1]/div[1]/a/text()').extract()
				item['desc'] = sel.xpath().extract()
				item['comment_num'] = sel.xpath('/div[1]/span').extract()
				item['author'] = sel.xpath('/div[2]/div[1]/div[2]/span[1]/span[1]/a').extract()
				item['time'] = sel.xpath('/div[2]/div[2]/div[1]/div').extract()
				yield item
