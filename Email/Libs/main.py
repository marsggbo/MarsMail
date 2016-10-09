# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
from PyQt4 import QtCore,  QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Ui_main import Ui_MainWindow
from calender import calenderDialog
from writemail import WriteEmailDialog

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_writeletter_clicked(self):
        print('write')
        
    @pyqtSlot()
    def on_receiveletter_clicked(self):
        print('receive')

    @pyqtSlot()
    def on_calender_clicked(self):
       my_calender = calenderDialog()
       my_calender.exec_()
    
    @pyqtSlot()
    def on_writeletter_2_clicked(self):
       my_writemail  = WriteEmailDialog()
       my_writemail.exec_()

        
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())

