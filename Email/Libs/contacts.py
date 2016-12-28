# -*- coding: utf-8 -*-

"""
Module implementing contacts.
"""

from PyQt4 import QtCore,  QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QDialog

from Ui_contacts import Ui_contacts
from writemail import WriteEmailDialog
from DealJsonFile import GetJsonInfo,SaveJsonInfo

import os,random

class contacts(QDialog, Ui_contacts):
	"""
	Class documentation goes here.
	"""
	def __init__(self, parent=None):
		super(contacts, self).__init__(parent)
		self.setupUi(self)
		self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
		self.createAlert.hide()
		self.must1.hide()
		self.must2.hide()

		self.emailInfo = GetJsonInfo('conf.json')
		self.contUserMail.setText(self.emailInfo["email"])
		num = self.generateNum(self.emailInfo["email"])
		self.contUserLogo.setStyleSheet("border-image: url(:/avatar/Avatars/%d.jpg);"%num)

		abDir = os.path.abspath(os.path.join(os.path.dirname(__file__))).replace('\\','/')
		dir = "%s/data/%s/"%(abDir,self.emailInfo['email'])
		self.contactsJsonName = dir+'contacts.json'
		self.receiveJsonName = dir + "receive.json"
		# 若不存在联系人数据文件则新建文件
		if not os.path.exists(self.contactsJsonName):
			self.contacts = {}
			self.receive = GetJsonInfo(self.receiveJsonName)
			for item in self.receive:
				if self.receive[item]['fromAddr'] not in self.contacts:
					emailAddr = self.receive[item]['fromAddr']
					temp = {
						emailAddr:{
							'fromAddr':emailAddr,
							'name':self.receive[item]['name']
						}
					}
					self.contacts.update(temp)
			SaveJsonInfo(self.contactsJsonName,self.contacts)
		else:
			# 联系人数据结构
			#{
			# 	'emailAddr':{
			# 	    'fromAddr':'', 'name':'', 'qq':'', 'weChat':'', 'phone':'', 'remark':''
			#   }
			# }
			self.contacts = GetJsonInfo(self.contactsJsonName)

		for x in self.contacts:
			if x != self.emailInfo["email"]:
				item = QtGui.QListWidgetItem()
				item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignVCenter)
				icon3 = QtGui.QIcon()
				num = self.generateNum(x)
				icon3.addPixmap(QtGui.QPixmap(":/avatar/Avatars/%d.jpg"%num), QtGui.QIcon.Normal, QtGui.QIcon.Off)
				item.setIcon(icon3)

				my_contact = self.contacts[x]['name'] + '\n' + self.contacts[x]['fromAddr']
				item.setText(my_contact)
				self.contactsList.addItem(item)

		# 绑定QListWidget
		self.connect(self.contactsList, SIGNAL('itemClicked(QListWidgetItem *)'), self.itemClicked)

	# 伪随机数
	def generateNum(self,string):
		try:
			num = ord(string[0])
			num = int(num % 30)
			print(num)
			return num
		except Exception as e:
			print(str(e))
			return 1

	@pyqtSlot()
	def itemClicked(self):
		my_currentItem = self.contactsList.currentItem()
		my_text = my_currentItem.text().split('\n')
		name = my_text[0]
		email = my_text[1]
		self.contacts = GetJsonInfo(self.contactsJsonName)

		qq = self.contacts[email].get('qq', '')
		remark = self.contacts[email].get('remark', '')
		weChat = self.contacts[email].get('weChat', '')
		phone = self.contacts[email].get('phone', '')

		self.contName.setText(name)
		self.contEmail.setText(email)
		self.contRemarkName.setText(remark)
		self.contPhone.setText(phone)
		self.contQQ.setText(qq)
		self.contWechat.setText(weChat)
		num = self.generateNum(email)
		self.contLogo.setStyleSheet("border-image: url(:/avatar/Avatars/%d.jpg);"%num)
		print(self.contName.text())


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
	def on_contClose_clicked(self):
		self.close()

	@pyqtSlot()
	def on_contMin_clicked(self):
		self.showMinimized()

	@pyqtSlot()
	def on_contWriteLetter_clicked(self):
		my_writemail  = WriteEmailDialog()
		my_writemail.exec_()

	@pyqtSlot()
	def on_delContact_clicked(self):
		# 获取邮箱地址
		contEmail = self.contEmail.text()
		if contEmail:
			isDel = QMessageBox.information(self, '删除联系人', u'确定要删除该联系人？', 'Yes', 'Cancel')
			if not isDel:
				# 获取邮箱地址
				contEmail = self.contEmail.text()
				# 获取联系人数据
				self.contacts = GetJsonInfo(self.contactsJsonName)
				self.contacts.pop(contEmail)

				# 联系人数据回写
				SaveJsonInfo(self.contactsJsonName,self.contacts)

				self.contName.setText('')
				self.contEmail.setText('')
				self.contLogo.setStyleSheet("")
				self.contRemarkName.setText('')
				self.contPhone.setText('')
				self.contQQ.setText('')
				self.contWechat.setText('')

				self.contactsList.takeItem(self.contactsList.currentRow())
		else:
			QMessageBox.information(self, '删除联系人', u'请先选择要删除的联系人', 'ok')

	@pyqtSlot()
	def on_contReset_clicked(self):
		self.contRemarkName.setText('')
		self.contPhone.setText('')
		self.contQQ.setText('')
		self.contWechat.setText('')

	@pyqtSlot()
	def on_contSave_clicked(self):
		email = self.contEmail.text()
		name = self.contName.text()
		if email and name:
			remark = self.contRemarkName.text()
			phone = self.contPhone.text()
			qq = self.contQQ.text()
			weChat = self.contWechat.text()
			self.contacts = GetJsonInfo(self.contactsJsonName)
			temp = {
				email:{
					'name':name,
					'fromAddr':email,
					'remark':remark,
					'phone':phone,
					'qq':qq,
					'weChat':weChat
				}
			}
			self.contacts.update(temp)
			SaveJsonInfo(self.contactsJsonName,self.contacts)
			self.createAlert.hide()
			self.must1.hide()
			self.must2.hide()
			QMessageBox.information(self, '保存联系人', u'保存成功', 'ok')
		else:
			QMessageBox.information(self, '保存联系人', u'用户名和邮箱不能为空！', 'ok')


	@pyqtSlot()
	def on_createContact_clicked(self):
		self.contLogo.setStyleSheet("")
		self.contName.setText('')
		self.contEmail.setText('')
		self.contRemarkName.setText('')
		self.contPhone.setText('')
		self.contQQ.setText('')
		self.contWechat.setText('')
		self.createAlert.show()
		self.must1.show()
		self.must2.show()

	@pyqtSlot()
	def on_sync_clicked(self):
		self.receive = GetJsonInfo(self.receiveJsonName)
		self.contacts = GetJsonInfo(self.contactsJsonName)
		for item in self.receive:
			if self.receive[item]['fromAddr'] not in self.contacts:
				emailAddr = self.receive[item]['fromAddr']
				temp = {
					emailAddr: {
						'fromAddr': emailAddr,
						'name': self.receive[item]['name']
					}
				}
				self.contacts.update(temp)
		SaveJsonInfo(self.contactsJsonName, self.contacts)

		self.contactsList.clear()
		for x in self.contacts:
			if x != self.emailInfo['email']:
				item = QtGui.QListWidgetItem()
				item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignVCenter)
				icon3 = QtGui.QIcon()
				num = self.generateNum(x)
				icon3.addPixmap(QtGui.QPixmap(":/avatar/Avatars/%d.jpg"%num), QtGui.QIcon.Normal, QtGui.QIcon.Off)
				item.setIcon(icon3)

				my_contact = self.contacts[x]['name'] + '\n' + self.contacts[x]['fromAddr']
				item.setText(my_contact)
				self.contactsList.addItem(item)

		QMessageBox.information(self, '同步联系人', u'同步成功', 'ok')