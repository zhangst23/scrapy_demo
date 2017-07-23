from lxml import etree
import requests 
import time

def spider(url):
	html = requests.get(url)
	selector = etree.HTML(html.text)
	img_urls = selector.xpath('//*[@class="BDE_Image"]/@src')
	for url in img_urls:
		img = requests.get(url)
		with open('%s.jpg'%time.time(), 'wb') as file:
			file.write(img.content)
			print "Download %s.jpg successfully."%time.time()