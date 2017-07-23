# 1.0 PyMongo
pip install pymongo==3.4.0


# 2.0 建立连接
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
# 或者使用MongoURI格式
# client = MongoClient('mongodb://localhost:27017')



# 3.0 访问数据库
db = client.pymongo_test
# 或者字典形式访问
db = client['pymongo_test']



# 4.0 插入文档
posts = db.posts
post_data = {
	'title': 'Python and MongoDB',
	'content': 'PyMongo is fun, you guys',
	'author': 'Scott'
}
result = posts.insert_one(post_data)
print('One post: {0}'.format(result.inserted_id))


###################### MongoEngine  ###########################

'''
虽然PyMongo是非常容易使用，总体上是一个伟大的轮子，但是许多项目使用它都可能太低水平。
简而言之，你必须编写很多自己的代码来持续地保存，检索和删除对象。PyMongo之上提供了一个
更高的抽象一个库是MongoEngine。MongoEngine是一个对象文档映射器（ODM），它大致相当于
一个基于SQL的对象关系映射器（ORM）。MongoEngine提供的抽象是基于类的，所以你创建的所有模型都是类。
虽然有相当多的Python的库可以帮助您使用MongoDB，MongoEngine是一个更好的，因为它有一个很好的组合的功能，
灵活性和社区支持。
'''

pip install mongoengine==0.10.7

# 连接
from mongoengine import *
connect('mongoengine_test', host='localhost', port=27017)

# 定义文档
import datetime

class Post(Document):
	title = StringField(required=True, max_length=200)
	content = StringField(required=True)
	author = StringField(required=True, max_length=50)
	published = DateTimeField(default=datetime.datetime.now)




















