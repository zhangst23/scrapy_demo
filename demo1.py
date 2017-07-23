'''
于是我就写了个70几行的python脚本，包含爬虫+邮件模块，跑在家里的一台闲置笔记本上，通过计划任务每准点抓取妹子的签名和最新文章一次，发送到我的邮箱。。嗯，其实是很简单的技术，，代码如下所示：
'''

# coding:utf-8
import requests
from lxml import html

cookie = {}

raw_cookies = ''

for line in raw_cookies.split(';'):
	key,value = line.split("=", 1)
	cookie[key] = value

page = requests.get('#妹子的豆瓣主页#', cookies=cookie)

tree = html.fromstring(page.text)

intro_raw = tree.xpath('//span[@id="intro_display"]/text()')

for i in intro_raw:
	intro = i.encode('utf-8')

print intro