#coding=utf-8
# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import os
import sys


class loadgif(QWidget):
	def __init__(self):
		super(loadgif, self).__init__()
		self.resize(100, 100)
		self.move(300, 300)
		self.setWindowFlags(Qt.FramelessWindowHint)
		movie = QMovie("souce/sendBuffer1.gif")
		movie.setScaledSize(QSize(100, 100))
		label = QLabel(parent=self)
		label.setMovie(movie)
		movie.start()

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	loadgif1 = loadgif()
	loadgif1.show()
	sys.exit(app.exec_())