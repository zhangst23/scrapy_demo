class UserAgentMiddleware(object):
	def process_request(self, request, spider):
		request.headers["User-Agent"] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36 QQBrowser/4.1.4656.400'





		