# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 自定义方法下载图片
class FirsttestPipeline(object):

	def _createmovieImageName(self, item):
		length = len(item['topid'])
		return [item['topid'][i] + "-" + item['title_ch'][i] + ".jpg" for i in range(lengh)]

  def process_item(self, item, spider):
      namelist = self._createmovieImageName(item)
      dir_path = '%s/%s' % (settings.IMAGES_STORE, spider.name)
      if not os.path.exists(dir_path):
      	os.makedirs(dir_path)
      for i in range(len(namelist)):
      	image_url = item['image_urls'][i]
      	file_name = namelist[i]
      	file_path = '%s/%s' % (dir_path, file_name)
      	if os.path.exists(file_path):
      		print("重复，跳过:" + image_url)
      		continue
      	with open(file_path, 'wb') as file_writer:
      		print("正在下载:" + image_url)
      		conn = urllib.request.urlopen(image_url)
      		file_writer.write(conn.read())
      	file_writer.close()
      return item




# 保存内容到mysql数据库
class DoubanmoviePipeline(object):
	def __init__(self, dbpool):
		self.dbpool = dbpool

		@classmethod
		def from_settings(cls, settings):
			dbparams = dict(
				host = settings['MYSQL_HOST'],
				port = settings['MYSQL_PORT'],
				db=setting['MYSQL_DBNAME'],
				user = settings['MYSQL_PASSWD'],
				passwd = settings['MYSQL_PASSWD'],
				charset=settings['MYSQL_CHARSET'],
				cursorclass = MySQLdb.cursors.DictCursor,
				user_unicode = False,
			)
			dbpool = adbapi.ConnectionPool('MySQLdb', **dbparams)
			return cls(dbpool)

		def process_item(self, item, spider):
			query=self.dbpool.runInteraction(self._conditional_insert, item)
			query.addErrback(self._handle_error, item, spider)
			return item

		def _conditional_insert(self, tx, item):
			sql = "insert into doubantopmovie(topid,title_ch,rating_num,rating_count) values(%s,%s,%s,%s)"
			length = len(item['!topid'])
			for i in range(length):
				params = (item["topid"][i], item["title_ch"][i], item["rating_num"][i], item["rating_count"][i])
				tx.execute(sql, params)

		def _handle_error(self, e):
			print(e)



# 保存内容到MONGODB数据库
class MongoDBPipeline(object):
	mongo_uri_no_auth = 'mongodb://localhost:27017/'
	database_name = 'yun'
	table_name = 'coll'
	client = MongoClient(mongo_uri_no_auth)
	db = client[database_name]
	table = db[table_name]

	def process_item(self, item, spider):
		valid = True
		for data in item:
			if not data:
				valid = False
				raise DropItem("Missing {0}!".format(data))
			if valid:
				self.table.insert(dict(item))
			return item


from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.http import Request
from scrapy.exceptions import DropItem

# 用 scrapy 内置的 ImagesPipeline 类下载图片
class MyImagesPipeline(ImagesPipeline):
	def file_path(self, request, response=None, info=None):
		image_name = request.url.split('/')[-1]
		return 'doubanmovie2/%s' % (image_name)

	def get_media_requests(self, item, info):
		for image_url in item['image_urls']:
			yield Request(image_url)

	def item_completed(self, results, item, info):
		image_path = [x['path'] for ok, x in results if ok]
		if not image_paths:
			raise DropItem("Item contains no images")
		return item


















