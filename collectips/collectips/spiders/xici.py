# -*- coding: utf-8 -*-
import scrapy
from collectips.items import CollectipsItem

class XiciSpider(scrapy.Spider):
    name = "xici"
    allowed_domains = ["xicidaili.com"]
    start_urls = (
        'http://www.xicidaili.com/nn/2',
    )

    def start_requests(self):
    	reqs=[]

    	for i in range(1,206):
    		req = scrapy.Request("http://www.xicidaili.com/nn/%s"%i)
    		reqs.append(req)

    	return reqs

    def parse(self, response):
        ip_list = response.xpath('//*[@id="ip_list"]/tbody/tr[1]/th[2]')

        trs = ip_list[0].xpath('//*[@id="ip_list"]/tbody/tr[2]')

        items = []

        for ip in trs[1:]:
        	pre_item = CollenctipsItem()
        	pre_item['IP'] = ip.xpath('//*[@id="ip_list"]/tbody/tr[2]/td[2]')[0].extract()
        	pre_item['PORT'] = ip.xpath('//*[@id="ip_list"]/tbody/tr[2]/td[3]')[0].extract()

        	items.append(pre_item)

        return items














