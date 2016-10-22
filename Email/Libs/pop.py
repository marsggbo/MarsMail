import poplib
import json
import time, threading
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

email = "1435679023@qq.com"
password = "19960229hexinABC"
pop3_server = 'pop.qq.com'

def GetJsonInfo(file):
	f = open(file,'r',encoding='utf-8')
	s = json.load(f)
	f.close()
	return s

def SaveJsonInfo(file,data):
	f = open(file,"w",encoding='utf-8')
	f.write(json.dumps(data))
	f.close()


def guess_charset(msg):
	charset = msg.get_charset()
	if charset is None:
		content_type = msg.get('Content-Type', '').lower()
		pos = content_type.find('charset=')
		if pos >= 0:
			charset = content_type[pos + 8:].strip()
	return charset

def decode_str(s):
	value, charset = decode_header(s)[0]
	if charset:
		value = value.decode(charset)
	return value


def print_info(msg, indent=0):
	if indent == 0:
		global subject
		my_info = {}
		my_emailInfos = {}

		subject = msg.get('Subject', '')
		if subject:
			subject = decode_str(subject)
			my_info['subject'] = subject

		fromAddr = msg.get('From', '')
		if fromAddr:
			hdr, addr = parseaddr(fromAddr)
			name = decode_str(hdr)
			my_info["name"] = name
			my_info["fromAddr"] = addr

		date = msg.get('Date', '')
		if date:
			date = decode_str(date)
			my_info['date'] = date

		if len(subject)>30:
			my_emailInfos[subject[:30]] = my_info
		else:
			my_emailInfos[subject] = my_info

		my_oringinInfo = GetJsonInfo('contacts.json')
		my_oringinInfo.update(my_emailInfos)
		SaveJsonInfo('contacts.json', my_oringinInfo)

	if (msg.is_multipart()):
		parts = msg.get_payload()
		for n, part in enumerate(parts):
			# print('%s--------------------' % ('  ' * indent))
			print_info(part, indent + 1)
	else:
		content_type = msg.get_content_type()
		if content_type=='text/plain' or content_type=='text/html':
			content = msg.get_payload(decode=True)
			charset = guess_charset(msg)
			if charset:
				content = content.decode(charset)
			# print('%sText: %s' % ('  ' * indent, content + '...'))

			# 保存为文件形式
			if len(subject) > 30:
				f = open('../data/%s.html'%subject[:30],'wb')
				f.write(content.encode('utf-8'))
				f.close()
			else:
				f = open('../data/%s.html'%subject ,'wb')
				f.write(content.encode('utf-8'))
				f.close()

		else:
			# print('%sAttachment: %s' % ('  ' * indent, content_type))
			f = open('../data/Attachment.html','wb')
			f.write(content_type.encode('utf-8'))
			f.close()

class ReceiveMail():
	def __init__(self, parent=None):
		# super(SendMail, self).__init__(parent)
		# self.__init__()
		self.emailInfo = {
		"email":"1435679023@qq.com",
		"pwd":"19960229hexinABC",
		"to_addr":"",
		"pop3_server":"pop.qq.com",
		"subject":"",
		"html":"",
		"plain":"",
		}
		self.index = 0

	def GetEmailNum(self):
		# 建立连接
		self.server = poplib.POP3_SSL(self.emailInfo["pop3_server"])
		print(type(self.server))
		# 身份认证:
		self.server.user(self.emailInfo["email"])
		self.server.pass_(self.emailInfo["pwd"])

		# list()返回所有邮件的编号:
		# resp: 状态码
		# mails：邮件
		# 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
		resp, mails, octets = self.server.list()

		# 获取邮件数量, 注意索引号从1开始:
		self.index = len(mails)
		return self.index

	def Receive(self,index):
		self.server = poplib.POP3_SSL(self.emailInfo["pop3_server"])
		# 身份认证:
		self.server.user(self.emailInfo["email"])
		self.server.pass_(self.emailInfo["pwd"])
		if index > 6:
			for i in range(index,index-6,-1):
				msg_content = ''
				resp, lines, octets = self.server.retr(i)

				# lines存储了邮件的原始文本的每一行,
				# 可以获得整个邮件的原始文本:
				msg_content = b'\r\n'.join(lines).decode('utf-8')

				# # 稍后解析出邮件:
				msg = Parser().parsestr(msg_content)
				print_info(msg)

				# 可以根据邮件索引号直接从服务器删除邮件:
				# server.dele(i)
				# 关闭连接:
		self.server.quit()
