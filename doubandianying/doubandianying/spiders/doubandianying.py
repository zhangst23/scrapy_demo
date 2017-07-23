import scrapy
import sys
from doubandianying.items import DoubandianyingItem
reload(sys)
sys.setdefaultencoding('utf-8')

class doubandianying(scrapy.Spider):
	name = 'doubandianying'
	allowed_domains = ["douban.com"]
	start_urls = ["http://movie.douban.com/top250"]

	def parse(self, response):
		item = DoubandianyingItem()
		infos = response.xpath('//div[@class="item"]')

		for info in infos:
			title = info.xpath('div[@class="pic"]/a/img/@alt').extract()
			link = info.xpath('div[@class="pic"]/a/@href').extract()
			star = info.xpath('div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()
			quote = info.xpath('div[@class="info"]/div[@class="bd"]/p[@class="quote"]/span/text()').extract()
			item['title']=title
			item['link']=link
			item['star']=star
			item['quote']=quote
			yield item

			next_page = response.xpath('//span[@class="next"]/a/@href')

			if next_page:
				url = response.urljoin(next_page[0].extract())
				yield scrapy.Request(url, self.parse)



'''
class doubandianying(scrapy.Spider):
	name = ''
	allowed_domains = [""]
	start_urls = [""]

	def parse(self, response):
		item = DoubandianyingItem()
		infos = response.xpath('//')
		for info in infos:
			item['title'] = info.xpath('').extract()
			item['link'] = info.xpath('').extract()
			item['star'] = info.xpath('').extract()
			item['quote'] = info.xpath('').extract()
			yield item

			next_page = response.xpath('')

			if next_page:
				url = response.urljoin(next_page[0].extract())
				yield scrapy.Request(url, self.parse)

'''

















