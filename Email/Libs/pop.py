#coding=utf-8
import poplib
import time
import email
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr, parsedate
from email.parser import BytesParser
from DealJsonFile import GetJsonInfo, SaveJsonInfo
from locker import encrypt, decrypt
import os



class ReceiveMail():
	def __init__(self, parent=None):
		self.emailInfo = GetJsonInfo('conf.json')
		# 密码解码
		self.password = decrypt(self.emailInfo["pwd"])

		# 邮件数量
		self.index = 0

		# 线程锁
		self.isLock = 0

	# 建立连接
	def connect(self):
		self.server = poplib.POP3_SSL(self.emailInfo["pop3_server"])

		# 身份认证:
		self.server.user(self.emailInfo["email"])
		self.server.pass_(self.password)
		return self.server

	# 关闭连接
	def quit(self):
		self.server.quit()

	# 删除邮件
	def delete(self,i):
		self.server.dele(i)

	# 获取邮件数量
	def GetEmailNum(self):
		# list()返回所有邮件的编号:
		# resp: 状态码
		# mails：邮件
		# 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
		resp, mails, octets = self.server.list()

		# 获取邮件数量, 注意索引号从1开始:
		self.emailNum = len(mails)
		return self.emailNum

	# 解析邮件基本信息
	def parseEmailInfo(self,msg):
		global subject
		my_info = {}
		my_emailInfos = {}

		subject = msg.get('Subject', '')
		if subject:
			subject = self.decode_str(subject)
			# 对主题做处理
			specialChar = ['\\', '/', ':', '|', '>', '<', '*', '"']
			for x in specialChar:
				subject = subject.replace(x, '_')
			my_info['subject'] = subject


		fromAddr = msg.get('From', '')
		if fromAddr:
			hdr, addr = parseaddr(fromAddr)
			name = self.decode_str(hdr)
			if name:
				my_info["name"] = name
			else:
				my_info["name"] = addr
			my_info["fromAddr"] = addr

		date = msg.get('Date', '')
		if date:
			date = self.decode_str(date)
			date = parsedate(date)
			date = list(date)
			for i in range(len(date)):
				if len(str(date[i])) == 1:
					date[i] = '0' + str(date[i])
			date = str(date[0]) + '.' + str(date[1]) + '.' + str(date[2]) + ' ' + str(date[3]) + ':' + str(
				date[4]) + ':' + str(date[5])
			my_info['date'] = date

		if len(subject) > 30:
			my_emailInfos[subject[:30]] = my_info
		else:
			my_emailInfos[subject] = my_info

		dir = '/data/%s/receive.json' % (self.emailInfo['email'])
		# 获取当前文件的绝对路径
		abDir = os.path.abspath(os.path.join(os.path.dirname(__file__))).replace('\\', '/')
		dir = ("%s/%s") % (abDir, dir)

		my_oringinInfo = GetJsonInfo(dir)
		my_oringinInfo.update(my_emailInfos)
		SaveJsonInfo(dir, my_oringinInfo)
		return my_emailInfos

	# 解析邮件内容
	def parseEmailContent(self,msg):
		if (msg.is_multipart()):
			parts = msg.get_payload()
			for n, part in enumerate(parts):
				self.parseEmailContent(part)

		else:
			content_type = msg.get_content_type()
			if content_type == 'text/html':
				content = msg.get_payload(decode=True)
				charset = self.guess_charset(msg)
				if charset:
					try:
						content = content.decode('utf-8')
					except Exception as e:
						print(str(e))
						content = content.decode(charset)

				content = '<meta charset="utf-8">' + content + '<meta charset="utf-8">'

				# 保存为文件形式
				if len(subject) > 30:
					emailname = subject[:30]
				else:
					emailname = subject

				# 用户存储目录，用于存储邮件html文件
				dir = "data/%s" % self.emailInfo['email']

				if not os.path.exists(dir):
					os.makedirs(dir)
					dir = dir + "/%s.html" % emailname
					with open(dir, 'wb') as f:
						f.write(content.encode('utf-8'))
				else:
					dir = dir + "/%s.html" % emailname
					with open(dir, 'wb') as f:
						f.write(content.encode('utf-8'))


			else:
				dir = "data/%s" % self.emailInfo['email']
				if len(subject) > 30:
					emailname = subject[:30]
				else:
					emailname = subject

				# 对附件夹路径名做处理
				specialChar = ['\\', '/', ':', '|', '>', '<', '*', '"']
				for x in specialChar:
					emailname = emailname.replace(x, '_')

				# 获取附件名，若有附件则以邮件名创建附件文件夹
				sonDir = dir + "/%s"%emailname
				filename = msg.get_filename()
				if filename:
					# h = email.Header.Header(filename)
					dh = decode_header(filename)
					fname = dh[0][0]
					charset = dh[0][1]

					try:
						fname = fname.decode(charset)
						print('有附件啦1',fname)
					except Exception as e:
						print(str(e))
						fname = dh[0][0]
						print('有附件啦2',fname)
					data = msg.get_payload(decode=True)

					# 对附件夹路径名做处理
					specialChar = ['\\', '/', ':', '|', '>', '<', '*', '"']
					for x in specialChar:
						fname = fname.replace(x, '_')

					if not os.path.exists(sonDir):
						os.makedirs(sonDir)
						sonDir = sonDir + "/%s" % fname
						with open(sonDir, 'wb') as f:
							f.write(data)
					else:
						sonDir = sonDir + "/%s" % fname
						print(sonDir)
						with open(sonDir, 'wb') as f:
							f.write(data)
				else:
					print("附件没名字？？")


	# 获取邮件编码
	def guess_charset(self, msg):
		charset = msg.get_charset()
		if charset is None:
			content_type = msg.get('Content-Type', '').lower()
			pos = content_type.find('charset=')
			if pos >= 0:
				charset = content_type[pos + 8:].strip()
		return charset


	# 邮件解码
	def decode_str(self, s):
		value, charset = decode_header(s)[0]
		if charset:
			value = value.decode(charset)
		return value
