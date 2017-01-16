from DealJsonFile import GetJsonInfo, SaveJsonInfo
import threading,time,os,re

class Search():
	def __init__(self):
		self.islock = True  # 锁住

	# 运行搜索函数
	def run(self,userInfo=None,mode=None,keyword=None):
		self.userInfo = userInfo
		self.dir = '/data/%s'%(self.userInfo['email'])
		# 获取当前文件的绝对路径
		abDir = os.path.abspath(os.path.join(os.path.dirname(__file__))).replace('\\','/')
		self.dir = abDir + self.dir
		print(self.dir)
		self.receiveJsonName = self.dir + '/receive.json'
		print(userInfo)
		print(mode)
		print(keyword)
		if mode == '主题':
			print('主题搜索')
			self.result = self.searchSubject(keyword)
			self.islock = False  # 解锁
		elif mode == '联系人':
			print('联系人搜索')
			self.result = self.searchName(keyword)
			self.islock = False  # 解锁
		elif mode == '时间':
			print('时间搜索')
			self.result = self.searchDate(keyword)
			self.islock = False  # 解锁
		elif mode == '邮件内容':
			print('邮件内容搜索')
			self.result = self.searchEmailContent(keyword)
			self.islock = False  # 解锁

	# 返回结果，用于给外部提供接口
	def getResult(self):
		# print("获取结果")
		while not self.islock:
			return self.result

	# 搜索主题
	def searchSubject(self,subject):
		dir = 'data/%s'%(self.userInfo['email'])
		contacts = GetJsonInfo(self.receiveJsonName)
		files = {}
		subject = subject.lower()
		if os.path.exists(dir):
			for file in os.listdir(dir):
				if os.path.isfile(os.path.join(dir, file)):
					if subject in file.lower():
						file = file.replace('.html','')
						if file in contacts:
							files[file] = contacts[file]
		return files

	# 搜索邮件内容
	def searchEmailContent(self,content):
		contacts = GetJsonInfo(self.receiveJsonName)
		files = {}
		# 遍历邮件文件夹
		if os.path.exists(self.dir):
			for file in os.listdir(self.dir):
				if file[-4:] == 'html':
					fileDir = "%s/%s"%(self.dir,file)
					with open(fileDir,'rb') as f:
						emailContent = f.read().decode('utf-8')

						if content in emailContent:
							subject = file.replace('.html','')
							files[subject] = contacts[subject]

		return files

	# 搜索邮件地址
	def searchEmailAddr(self,email):
		contacts = GetJsonInfo(self.receiveJsonName)
		files = {}
		temp = email.lower()
		for item in contacts:
			if temp in contacts[item]['fromAddr'].lower():
				files[item] = contacts[item]
		return files

	# 搜索联系人
	def searchName(self,name):
		contacts = GetJsonInfo(self.receiveJsonName)
		files = {}
		temp = name.lower()
		for item in contacts:
			if temp in contacts[item]['name'].lower():
				files[item] = contacts[item]
		return files

	# 搜索时间
	def searchDate(self,date):
		contacts = GetJsonInfo(self.receiveJsonName)
		files = {}
		temp = date.lower()
		for item in contacts:
			if temp in contacts[item]['date'].lower():
				files[item] = contacts[item]
		return files
