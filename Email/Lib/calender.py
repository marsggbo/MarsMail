# -*- coding: utf-8 -*-

from PyQt4 import QtCore,QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Ui_calender import Ui_calenderDialog

class calenderDialog(QDialog, Ui_calenderDialog):
	def __init__(self, parent=None):
		super(calenderDialog, self).__init__(parent)
		self.setupUi(self)
		self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)

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
	def on_calenderClose_clicked(self):
		self.close()

	@pyqtSlot()
	def on_calenderMin_clicked(self):
		self.showMinimized()
