#coding=utf-8

import smtplib
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr, formatdate
from DealJsonFile import GetJsonInfo, SaveJsonInfo
from locker import decrypt

class SendMail():
	def __init__(self, parent=None):
		self.emailInfo = GetJsonInfo('conf.json')
		self.msg = MIMEMultipart('alternative')

	def Send(self):
		try:
			# 带附件邮件
			# 指定subtype为alternative，同时支持html和plain格式
			# 邮件正文为MIMEText
			plain = self.emailInfo["plain"]
			self.msg.attach(MIMEText(plain, 'plain', 'utf-8'))       # 纯文本
			# html = '<html><body><h1>Hello</h1><p><img src="cid:0"></p></body></html>'
			html = self.emailInfo["html"]
			self.msg.attach(MIMEText(html, 'html', 'utf-8'))

			# 未指定用户别名，则客户端会自动提取邮件地址中的名称作为邮件的用户别名
			self.msg['From'] = Header(self.emailInfo["email"])
			self.msg['To'] = Header(self.emailInfo["to_addr"])
			self.msg['Subject'] = Header(self.emailInfo["subject"], 'utf-8').encode()

			server = smtplib.SMTP_SSL(self.emailInfo["smtp_server"],465)

			server.set_debuglevel(1)
			password = decrypt(self.emailInfo['pwd'])
			server.login(self.emailInfo["email"],password)
			server.sendmail(self.emailInfo["email"],self.emailInfo["to_addr"],self.msg.as_string())
			server.quit()

		except Exception as e:
			raise e