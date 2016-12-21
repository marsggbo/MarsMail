# -*- coding: utf-8 -*-

"""
Module implementing WriteEmailDialog.
"""

from PyQt4 import QtCore
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QDialog,QMessageBox

from Ui_writemail import Ui_WriteEmailDialog
from smtp import SendMail
from DealJsonFile import GetJsonInfo, SaveJsonInfo
import time,os

def GetEmailText(filename):
	f = open(filename,'r',encoding='utf-8')
	s = f.read()
	f.close()
	return s

class WriteEmailDialog(QDialog, Ui_WriteEmailDialog):

	# isForward用于判断是否是转发,默认不是转发,text是转发内容
	def __init__(self, parent=None,isForwad=False,ForwardInfo=None,url=None,isReply=False,replyInfo=None):
		super(WriteEmailDialog, self).__init__(parent)
		self.setupUi(self)
		self.emailInfo = GetJsonInfo('conf.json')
		self.email = SendMail()
		self.isForwad = isForwad
		self.isReply = isReply


		self.page = self.richEmailEdit.page()
		self.frame = self.page.mainFrame()

		# 数据结构文件路径
		abDir = os.path.abspath(os.path.join(os.path.dirname(__file__))).replace('\\','/')
		self.dir = "%s/data/%s/"%(abDir,self.emailInfo['email'])
		self.sendJsonName = self.dir + "send.json"
		self.deleteJsonName = self.dir + "delete.json"
		self.draftJsonName = self.dir + "draft.json"

		# 富文本编辑器html文件路径
		self.richEditDir = r'''%s\kindeditor-4.1.7\examples\default.html'''%abDir
		self.richEditDir = self.richEditDir.replace('\\','/')

		# self.info = info  # info是要转发的用户信息，用元组表示
		# 转发
		if self.isForwad:
			# 获取原编辑器页面html内容
			with open(self.richEditDir,'rb') as f:
				originHtml = f.read()

			self.emailText = GetEmailText(url)
			self.formatText = '''\n\n\n\n- 发送自XYZ邮箱 -\n-------- 转发的邮件 --------\n发件人: "%s" %s\n日期: %s\n主题: %s\n'''%(ForwardInfo['email'],ForwardInfo['name'],ForwardInfo['time'],ForwardInfo['subject'])
			polishHtml = originHtml.decode('utf-8')
			polishHtml = polishHtml.replace("请输入邮件信息", self.formatText)


			# 将转发信息插入到编辑器中
			with open(self.richEditDir,'wb') as f:
				polishHtml = polishHtml.replace("\n",'<br>')
				f.write(polishHtml.encode('utf-8'))
			self.richEmailEdit.setUrl(QtCore.QUrl("file:///" + self.richEditDir))

			# 还原编辑器文件
			with open(self.richEditDir,'wb') as f:
				f.write(originHtml)

			# 将转发信息格式化
			str1 = self.formatText.split('-\n')
			str2 = str1[2].split('\n')
			str3 = (str1[0],str1[1],str2[0],str2[1],str2[2])
			self.formatText = '<div>%s<br>%s<br>%s<br>%s<br>%s<br><div></div><div style="clear:both;"></div>'% str3

		# 回复
		if self.isReply:
			with open(self.richEditDir,'rb') as f:
				originHtml = f.read()
			self.emailText = GetEmailText(url)
			self.formatText = '''\n\n\n\n- 发送自XYZ邮箱 -\n-------- 转发的邮件 --------\n发件人: "%s" %s\n日期: %s\n主题: %s\n''' % (
				ForwardInfo['email'], ForwardInfo['name'], ForwardInfo['time'], ForwardInfo['subject'])

			polishHtml = originHtml.decode('utf-8')
			polishHtml = polishHtml.replace("请输入邮件信息", self.formatText)

			# 将转发信息插入到编辑器中
			with open(self.richEditDir, 'wb') as f:
				polishHtml = polishHtml.replace("\n",'<br>')
				f.write(polishHtml.encode('utf-8'))
			self.richEmailEdit.setUrl(QtCore.QUrl("file:///" + self.richEditDir))

			# 还原编辑器文件
			with open(self.richEditDir, 'wb') as f:
				f.write(originHtml)

			# 将转发信息格式化
			str1 = self.formatText.split('-\n')
			str2 = str1[2].split('\n')
			str3 = (str1[0], str1[1], str2[0], str2[1], str2[2])
			self.formatText = '<div>%s<br>%s<br>%s<br>%s<br>%s<br><div></div><div style="clear:both;"></div>' % str3
			self.receiverEdit.setText(replyInfo['reply_addr'])
			self.subjectEdit.setText(replyInfo['reply_subject'])

	@pyqtSlot()
	def on_send_clicked(self):
		try:
			print("send!")
			receivers = self.receiverEdit.text()
			subject = self.subjectEdit.text()
			receivers = receivers.split(',')
			for receiver in receivers:
				if receiver and subject:
					self.email.emailInfo["to_addr"] = receiver
					self.email.emailInfo["subject"] = subject
					self.email.emailInfo["plain"] = self.emailContent.toPlainText()

					emailHtml = self.GetEmailHtml()

					if self.isForwad:
						my_addText = emailHtml.split('- 发送自XYZ')[0] # 添加的转发信息
						if my_addText.strip():
							self.email.emailInfo["html"] = my_addText + '<br><br>' + self.formatText + self.emailText
						else:
							self.email.emailInfo['html'] = self.formatText + self.emailText
					else:
						self.email.emailInfo["html"] = emailHtml

					self.email.Send()
					alert = QMessageBox.warning(self, '发送邮件', u'发送成功！')
					self.close()
				else:
					alert = QMessageBox.warning(self,'发送邮件提示','请将信息填写完整!')
			
		except Exception as e:
			print(str(e))
			a = str(e)
			alert = QMessageBox.warning(self, '发送失败', u'出错啦')

	# 将邮件内容存入草稿箱,并返回邮件内容html格式
	@pyqtSlot()
	def on_save_clicked(self):
		self.frame.evaluateJavaScript('''document.getElementById('emailHtml').innerHTML = editor.html();''')
		html = self.frame.toHtml()
		emailName = self.dir + self.subjectEdit.text()
		emailHtml = html.split('<textarea name="emailHtml" id="emailHtml" cols="30" rows="10">')[1].split("</textarea>")[0]
		emailHtml = emailHtml.replace('&lt;', '<').replace('&gt;', '>')
		with open('%s.html'%emailName,'wb') as f:
			f.write(emailHtml.encode('utf-8'))

		draft = GetJsonInfo(self.draftJsonName)
		temp = {}
		receivers = self.receiverEdit.text()
		subject = self.subjectEdit.text()
		receivers = receivers.split(',')
		date = self.parseDate(time.ctime())
		for receiver in receivers:
			temp[subject] ={"name": receiver, "fromAddr": receiver, "subject": subject, "date": date}
			draft.update(temp)
		SaveJsonInfo(self.draftJsonName,draft)
		alert = QMessageBox.warning(self, '保存草稿', u'保存成功')


	def GetEmailHtml(self):
		self.frame.evaluateJavaScript('''document.getElementById('emailHtml').innerHTML = editor.html();''')
		html = self.frame.toHtml()
		emailName = self.dir + self.subjectEdit.text()
		emailHtml = html.split('<textarea name="emailHtml" id="emailHtml" cols="30" rows="10">')[1].split("</textarea>")[0]
		emailHtml = emailHtml.replace('&lt;', '<').replace('&gt;', '>')
		return emailHtml

	# 处理时间
	def parseDate(self,date):
		import time
		from email.utils import parsedate
		if date:
			date = parsedate(date)
			date = list(date)
			for i in range(len(date)):
				if len(str(date[i])) == 1:
					date[i] = '0' + str(date[i])
			date = str(date[0]) + '.' + str(date[1]) + '.' + str(date[2]) + ' ' + str(date[3]) + ':' + str(date[4]) + ':' + str(date[5])
			return date

	@pyqtSlot()
	def on_accessory_clicked(self):
		print("Fujian")