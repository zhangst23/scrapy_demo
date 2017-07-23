# coding:utf-8
import scrapy
from topgoods.items import TopgoodsItem

class TmGoodsSpider(scrapy.Spider):
	name = 'tm_goods'
	allowed_domains = ["http://www.tmall.com"]
	start_urls = (
		'https://list.tmall.com/search_product.htm?q=%C3%AB%BD%ED&type=p&vmarket=&spm=a221t.1476805.a2227oh.d100&xl=m_1&from=nvzhuang..pc_1_suggest'
	)

	# 记录处理的页数
	count = 0

	def parse(self, response):
		TmGoodsSpider.count += 1
		divs = response.xpant("")
		if not divs:
			self.log("List Page error -- %s"%response.url)

		for div in divs:
			item = TopgoodsItem()
			item['GOODS_PRICE'] = div.xpath()[0].extract()
			item['GOODS_NAME'] = div.xpath()[0].extract()
			pre_goods_url = div.xpath()[0].extract()
			# item["GOODS_URL"] = pre_goods_url if "http: in pre_goods_url else ()"
			yield scrapy.Response(url=item["GOODS_URL"],meta={'item':item}, callback=self.parse_detail)




	def parse_detail(self, response):
		div = response.xpath('')
		if not div:
			self.log("Detail Page error--%s"%response.url)
		item = response.meta['item']
		div=div[0]
		item["SHOP_NAME"] = div.xpath()[0].extract()
		item["SHOP_URL"] = div.xpath()[0].extract()
		item["COMPANY_NAME"] = div.xpath()[0].extract()
		item["COMPANY_ADDRESS"] = div.xpath()[0].extract()

		yield item














