#!/usr/bin/python
# -*- coding: utf-8 -*-

import smtplib
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr, formatdate


# email = {
# 	"from_addr":"1435679023@qq.com",
# 	"password":"19960229hexinABC",
# 	"to_addr":"",
# 	"smtp_server":"smtp.qq.com",
# }
# return Alias_name <xxxx@example.com>
# def _format_addr(s):
#     name, addr = parseaddr(s)
#     return formataddr((Header(name, 'utf-8').encode(), addr))

class SendMail():
	def __init__(self, parent=None):
		# super(SendMail, self).__init__(parent)
		# self.__init__()
		self.emailInfo = {
		"from_addr":"1435679023@qq.com",
		"password":"19960229hexinABC",
		"to_addr":"",
		"smtp_server":"smtp.qq.com",
		"subject":"",
		"html":"",
		"plain":"",
		}


	def Send(self):
		try:
			# 带附件邮件
			# 指定subtype为alternative，同时支持html和plain格式
			msg = MIMEMultipart('alternative')  #
			# 邮件正文为MIMEText
			msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))
			# 邮件正文中显示图片，同时附件的图片将不再显示
			plain = self.emailInfo["plain"]
			msg.attach(MIMEText(plain, 'plain', 'utf-8'))       # 纯文本
			# html = '<html><body><h1>Hello</h1><p><img src="cid:0"></p></body></html>'
			html = '<html>hello world!</html>'
			msg.attach(MIMEText(html, 'html', 'utf-8'))   

			# 未指定用户别名，则客户端会自动提取邮件地址中的名称作为邮件的用户别名
			msg['From'] = Header(self.emailInfo["from_addr"])
			msg['To'] = Header(self.emailInfo["to_addr"])
			msg['Subject'] = Header('Getting started with Python', 'utf-8').encode()

			server = smtplib.SMTP_SSL(self.emailInfo["smtp_server"],465)

			server.set_debuglevel(1)
			server.login(self.emailInfo["from_addr"],self.emailInfo["password"])
			server.sendmail(self.emailInfo["from_addr"],self.emailInfo["to_addr"],msg.as_string())
			server.quit()

		except Exception as e:
			raise e
