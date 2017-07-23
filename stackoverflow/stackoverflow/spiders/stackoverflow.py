# coding:utf8
import scrapy

class StackoverflowSpider(scrapy.Spider):
	name = 'stackoverflow'
	start_urls = ['http://stackoverflow.com/question?sort=votes']

	def parse(self, response):
		for href in response.css('.question-summary h3 a::attr(href)'):
			full_url = response.urljoin(href.extract())
			yield scrapy.Request(full_url, call_back=self.parse_question)

	def parse_question(self, response):
		yield{
			'title': response.css('h1 a::text').extract()[0],
			'votes': response.css('.question .vote-count-post::text').extract()[0],
			'body': response.css('.question .post-text').extract()[0],
			'tags': response.css('.question .post-tag::text').extract(),
			'link': response.url,
		}