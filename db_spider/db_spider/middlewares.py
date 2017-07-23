# import random
# import base64
# from settings import PROXIES

# class RandomUserAgent(object):
# 	def __init__(self, agent):
# 		self.agents = agents

# 	@classmethod
# 	def from_crawler(cls, crawler):
# 		return cls(crawler.settings.getlist('USER_AGENTS'))

# 	def process_request(self, request, spider):
# 		request.headers.setdefault('User-Agent', random.choice(self.agents))

# class ProxyMiddleware(object):
# 	def process_request(self, request, spider):
# 		proxy = random.choice(PROXIES)
# 		if proxy['user_pass'] is not None:
# 			retuest.meta['proxy'] = "http://%s" % proxy['ip_port']
# 			