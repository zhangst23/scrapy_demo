# coding:utf-8
import requests
from lxml import etree
import pymongo


client = pymongo.MongoClient('localhost', 27017)
test = client['test']
xiaozhu = test['xiaozhu']

headers = {
	'User-Agent':''
}


urls = ['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(str(i)) for i in range(1,14)]

def get_info(url):
	html = requests.get(url, headers=headers)
	selector = etree.HTML(html.text)
	commoditys = selector.xpath('//')

	for commodity in commoditys:
		address = commodity.xpath('')[0]
		price = commodity.xpath('')[0]
		lease_type = commodity.xpath('')[0].split('/')[0].strip()
		bed_amount = commodity.xpath('')[0].split('/')[1].strip()
		suggestion = commodity.xpath('')[0].split('/')[2].strip()
		infos = commodity.xpath('')[0].strip
		comment_star = infos.split('/')[0] if '/' in infos else ' 无'
		comment_amount = infos.split('/')[1] if '/' in infos else infos

		content = {
			'address':address,
			'price':price,
			'lease_type':lease_type,
			'bed_amount':bed_amount,
			'suggestion':suggestion,
			'comment_star':comment_star,
			'comment_amount':comment_amount
		}
		xiaozhu.insert_one(content)

for url in urls:
	get_info(url)



'''
上次许多人问我，数据图是用什么做的，在这里给大家说一下：是用个人BDP做的，很简单，但个人版连接数据只支持csv和excel格式的数据，所以我的做法是：先导入mongodb，然后通过mongodb的导出功能导出为CSV的数据进行分析，导出csv格式的代码：

mongoexport -d test -c xiaozhu --csv -f address,price,lease_type,bed_amount,suggestion,comment_star,comment_amount -o xiaozhu.csv
1 -d数据库
2 -c表数据
3 -f表示要导出的字段

作者：罗罗攀
链接：http://www.jianshu.com/p/afc57a0e3a2f
來源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''


