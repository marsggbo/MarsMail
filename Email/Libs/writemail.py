# -*- coding: utf-8 -*-

"""
Module implementing WriteEmailDialog.
"""

from PyQt4 import QtCore, QtGui

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from email.mime.base import MIMEBase
from email.header import Header
from email import encoders
from email.encoders import encode_base64

from Ui_writemail import Ui_WriteEmailDialog
from smtp import SendMail
from DealJsonFile import GetJsonInfo, SaveJsonInfo
import time,os,threading

from loading import Loadgif

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
		self.fileName = []


		self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)

		self.attachShowBox.hide()


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

		# 获取原编辑器页面html内容
		with open(self.richEditDir,'rb') as f:
			self.originHtml = f.read()

		# 转发
		if self.isForwad:
			self.emailText = GetEmailText(url)
			self.formatText = '''\n\n\n\n- 发送自M@RS Mail邮箱 -\n-------- 转发的邮件 --------\n发件人: "%s" %s\n日期: %s\n主题: %s\n'''%(ForwardInfo['email'],ForwardInfo['name'],ForwardInfo['time'],ForwardInfo['subject'])
			polishHtml = self.originHtml.decode('utf-8')
			polishHtml = polishHtml.replace("请输入邮件信息", self.formatText.replace("\n",'<br>'))

			# "%s/data/%s/csd_gvd" % (abDir, self.emailInfo['email'])
			# 转发附件
			attachDir = self.dir + ForwardInfo['subject']
			if os.path.exists(attachDir):
				self.attachShowBox.show()
				for fileName in os.listdir(attachDir):
					with open(attachDir+'/'+fileName, 'rb') as f:
						self.fileName.append(attachDir+'/'+fileName)
						msg_attach = MIMEBase('application', 'octet-stream', filename = fileName)
						msg_attach.set_payload(f.read())
						encoders.encode_base64(msg_attach)

						msg_attach.add_header('Content-Disposition', 'attachment', filename = fileName)
						self.email.msg.attach(msg_attach)
						self.attachList.addItem(fileName)


			# 将转发信息插入到编辑器中
			with open(self.richEditDir,'wb') as f:
				f.write(polishHtml.encode('utf-8'))
			self.richEmailEdit.setUrl(QtCore.QUrl("file:///" + self.richEditDir))

			# 将转发信息格式化
			str1 = self.formatText.split('-\n')
			str2 = str1[2].split('\n')
			str3 = (str1[0],str1[1],str2[0],str2[1],str2[2])
			self.formatText = '<div>%s<br>%s<br>%s<br>%s<br>%s<br><div></div><div style="clear:both;"></div>'% str3

		# 回复
		elif self.isReply:
			self.emailText = GetEmailText(url)
			self.formatText = '''\n\n\n\n- 发送自M@RS Mail邮箱 -\n-------- 转发的邮件 --------\n发件人: "%s" %s\n日期: %s\n主题: %s\n''' % (
				ForwardInfo['email'], ForwardInfo['name'], ForwardInfo['time'], ForwardInfo['subject'])

			polishHtml = self.originHtml.decode('utf-8')
			polishHtml = polishHtml.replace("请输入邮件信息", self.formatText.replace("\n",'<br>'))

			# 转发附件
			attachDir = self.dir + ForwardInfo['subject']
			if os.path.exists(attachDir):
				self.attachShowBox.show()
				for fileName in os.listdir(attachDir):
					with open(attachDir+'/'+fileName, 'rb') as f:
						self.fileName.append(attachDir+'/'+fileName)
						msg_attach = MIMEBase('application', 'octet-stream', filename = fileName)
						msg_attach.set_payload(f.read())
						encoders.encode_base64(msg_attach)

						msg_attach.add_header('Content-Disposition', 'attachment', filename = fileName)
						self.email.msg.attach(msg_attach)
						self.attachList.addItem(fileName)

			# 将原信息插入到编辑器中
			with open(self.richEditDir, 'wb') as f:
				f.write(polishHtml.encode('utf-8'))
			self.richEmailEdit.setUrl(QtCore.QUrl("file:///" + self.richEditDir))

			# 将转发信息格式化
			str1 = self.formatText.split('-\n')
			str2 = str1[2].split('\n')
			str3 = (str1[0], str1[1], str2[0], str2[1], str2[2])
			self.formatText = '<div>%s<br>%s<br>%s<br>%s<br>%s<br><div></div><div style="clear:both;"></div>' % str3
			self.receiverEdit.setText(replyInfo['reply_addr'])
			self.subjectEdit.setText(replyInfo['reply_subject'])

		else:
			self.richEmailEdit.setUrl(QtCore.QUrl("file:///" + self.richEditDir))

	# 无边框设计
	def mousePressEvent(self, event):
		if event.button() == Qt.LeftButton:
			self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
			QApplication.postEvent(self, QEvent(174))
			event.accept()

	def mouseMoveEvent(self, event):
		if event.buttons() == Qt.LeftButton:
			self.move(event.globalPos() - self.dragPosition)
			event.accept()


	@pyqtSlot()
	def on_send_clicked(self):
		receivers = self.receiverEdit.text()
		subject = self.subjectEdit.text()

		movie = QMovie("souce/sendBuffer.gif")
		movie.setScaledSize(QSize(200, 200))
		self.loading.setMovie(movie)
		movie.start()

		if subject and len(receivers):
			try:
				print("send!")
				# 对附件夹路径名做处理
				specialChar = ['\\', '/', ':', '|', '>', '<', '*', '"']
				for x in specialChar:
					subject = subject.replace(x, '_')

				# 获取邮件内容
				emailHtml = self.GetEmailHtml()
				emailHtml = '<meta charset="utf-8">' + emailHtml + '<meta charset="utf-8">'

				receivers = receivers.split(',')

				if len(receivers) and subject:
					for receiver in receivers:
						self.email.emailInfo["to_addr"] = receiver
						self.email.emailInfo["subject"] = subject
						self.email.emailInfo["plain"] = self.emailContent.toPlainText()

						if self.isForwad:
							my_addText = emailHtml.split('- 发送自M@RS Mail')[0] # 添加的转发信息
							if my_addText.strip():
								self.email.emailInfo["html"] = my_addText + '<br><br>' + self.formatText + self.emailText
							else:
								self.email.emailInfo['html'] = self.formatText + self.emailText
						else:
							self.email.emailInfo["html"] = emailHtml

						t = threading.Thread(target=self.email.Send)
						t.start()
					self.loading.hide()
						# t.join()
				else:
					alert = QMessageBox.warning(self,'发送邮件提示','请将信息填写完整!')

				# time.sleep(5)
				# alert = QMessageBox.warning(self, '发送邮件', u'发送成功！')

				# self.close()
				sent = GetJsonInfo(self.sendJsonName)
				temp = {}
				date = self.parseDate(time.ctime())
				for receiver in receivers:
					temp[subject] = {"name": receiver, "fromAddr": receiver, "subject": subject, "date": date}
					sent.update(temp)
				SaveJsonInfo(self.sendJsonName, sent)

				# 将已发邮件存至指定目录
				# C:/Users/14356/Desktop/XYZMail/Email/Libs/data/110@qq.com/
				sendDir = self.dir + 'send/' + subject
				with open('%s.html' % sendDir, 'wb') as f:
					f.write(emailHtml.encode('utf-8'))

				# 若有附件，则将附件也保存到对应路径
				if len(self.fileName):
					for file in self.fileName:
						with open(file, 'rb') as f1:
							attachData = f1.read()
							attachDir = '%s/%s' % (sendDir, file.split('/')[-1])
							if not os.path.exists(sendDir):
								os.mkdir(sendDir)
							with open(attachDir, 'wb') as f2:
								f2.write(attachData)

				# 还原编辑器文件
				with open(self.richEditDir, 'wb') as f:
					f.write(self.originHtml)

			except Exception as e:
				print(str(e))
				alert = QMessageBox.warning(self, '发送失败', u'出错啦')
		else:
			alert = QMessageBox.warning(self, '发送失败', u'请将收件人和主题信息补充完整')


	# 将邮件内容存入草稿箱,并返回邮件内容html格式
	@pyqtSlot()
	def on_save_clicked(self):
		subject = self.subjectEdit.text()
		if subject:
			self.frame.evaluateJavaScript('''document.getElementById('emailHtml').innerHTML = editor.html();''')
			html = self.frame.toHtml()

			# 对附件夹路径名做处理
			specialChar = ['\\', '/', ':', '|', '>', '<', '*', '"']
			for x in specialChar:
				subject = subject.replace(x, '_')

			emailName = self.dir + self.subjectEdit.text()
			emailHtml = html.split('<textarea name="emailHtml" id="emailHtml" cols="30" rows="10">')[1].split("</textarea>")[0]
			emailHtml = emailHtml.replace('&lt;', '<').replace('&gt;', '>')
			emailHtml = '<meta charset="utf-8">' + emailHtml + '<meta charset="utf-8">'

			# 生成草稿文件路径
			draftDir = self.dir + 'draft/' + subject

			# 将草稿邮件存至指定目录
			with open('%s.html'%draftDir,'wb') as f:
				f.write(emailHtml.encode('utf-8'))

			# 若有附件，则将附件也保存到对应路径
			if len(self.fileName):
				for file in self.fileName:
					with open(file,'rb') as f1:
						attachData = f1.read()
						attachDir = '%s/%s'%(draftDir,file.split('/')[-1])
						if not os.path.exists(draftDir):
							os.mkdir(draftDir)
						with open(attachDir,'wb') as f2:
							f2.write(attachData)

			draft = GetJsonInfo(self.draftJsonName)
			temp = {}
			receivers = self.receiverEdit.text()
			receivers = receivers.split(',')
			date = self.parseDate(time.ctime())
			for receiver in receivers:
				temp[subject] ={"name": receiver, "fromAddr": receiver, "subject": subject, "date": date}
				draft.update(temp)
			SaveJsonInfo(self.draftJsonName,draft)
			alert = QMessageBox.warning(self, '保存草稿', u'保存成功')

			# 还原编辑器文件
			with open(self.richEditDir, 'wb') as f:
				f.write(self.originHtml)
		else:
			alert = QMessageBox.warning(self, '保存草稿', u'请将收件人和主题信息补充完整')

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

	# 添加附件
	@pyqtSlot()
	def on_accessory_clicked(self):
		try:
			options = QtGui.QFileDialog.Options()
			fileName = QtGui.QFileDialog.getOpenFileName(parent = self,
						caption = "please select your files",
						filter = "All Files (*)",
						options = options).replace('\\', '/')
			if fileName:
				with open(fileName, 'rb') as f:
					msg_attach = MIMEBase('application', 'octet-stream', filename = fileName)
					msg_attach.set_payload(f.read())
					encoders.encode_base64(msg_attach)

					msg_attach.add_header('Content-Disposition', 'attachment', filename = fileName.split('/')[-1])
					self.email.msg.attach(msg_attach)

					# 将要发送的附件复制到对应邮件附件文件夹中
					# 首先要正确填写主题和收件人
					subject = self.subjectEdit.text()

					# 对附件夹路径名做处理
					specialChar = ['\\', '/', ':', '|', '>', '<', '*', '"']
					for x in specialChar:
						subject = subject.replace(x, '_')

					self.fileName.append(fileName)

				self.attachShowBox.show()
				self.attachList.addItem(fileName.split('/')[-1])

		except Exception as e:
			alert = QMessageBox.warning(self, '添加附件', u'添加附件失败'+str(e))

	@pyqtSlot()
	def on_writeClose_clicked(self):
		self.close()

	@pyqtSlot()
	def on_writeMin_clicked(self):
		self.showMinimized()