# -*- coding: utf-8 -*-
import scrapy
from doubanmovie.items import DoubanmovieItem






class MovieSpider(scrapy.Spider):
    name = "movie"
    allowed_domains = ["movie.douban.com"]
    start_urls = (
        'http://www.movie.douban.com/top250',
    )


    def parse(self, response):
        # for info in response.xpath('//div[@class="item"]'):
	        # item = DoubanmovieItem()
	        # item['rank'] = info.xpath('div[@class="pic"]/em/text()').extract()
	        # item['title'] = info.xpath('div[@class="pic"]/a/img/@alt').extract()
	        # item['link'] = info.xpath('div[@class="pic"]/a/@href').extract()
	        # item['star'] = info.xpath('div[@class="info"]/div[@class="bd"]/div[@class="star"]/span/em/text()').extract()
	        # item['rate'] = info.xpath('div[@class="info"]/div[@class="bd"]/div[@class="star"]/span/text()').extract()
	        # item['quote'] = info.xpath('div[@class="info"]/div[@class="bd"]/p[@class="quote"]/span/text()').extract()
	        # yield item

	        item = DoubanmovieItem()
	        item['rank'] = response.xpath('//*[@id="content"]/div/div[1]/ol/li[1]/div/div[1]/em').extract()
	        item['title'] = response.xpath('//*[@id="content"]/div/div[1]/ol/li[1]/div/div[1]/a/img').extract()
	        item['link'] = response.xpath('//*[@id="content"]/div/div[1]/ol/li[1]/div/div[1]/a').extract()
	        item['star'] = response.xpath('//*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[2]/div/span[2]').extract()
	        item['rate'] = response.xpath('div[@class="info"]/div[@class="bd"]/div[@class="star"]/span/text()').extract()
	        item['quote'] = response.xpath('//*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[2]/p[2]/span').extract()
	        yield item














