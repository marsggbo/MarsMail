# -*- coding: utf-8 -*-

from PyQt4 import QtCore,QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Ui_about import Ui_About

class About(QMainWindow, Ui_About):
	def __init__(self, parent=None):
		super(About, self).__init__(parent)
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
	def on_aboutMin_clicked(self):
		self.showMinimized()

	@pyqtSlot()
	def on_aboutClose_clicked(self):
		self.close()

if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	ui = About()
	ui.show()
	sys.exit(app.exec_())