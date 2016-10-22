# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import json
from PyQt4 import QtCore,  QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import time, threading, os
from multiprocessing import Process

from Ui_main import Ui_MainWindow
from calender import calenderDialog
from writemail import WriteEmailDialog
from login import Login
from pop import ReceiveMail

def GetLoginInfo():
    f = open("conf.json",'r',encoding='utf-8')
    s = json.load(f)
    f.close()
    return s

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
#        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
#        def mousePressEvent(self, event):
#            if event.button() == Qt.LeftButton:
#                self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
#                QApplication.postEvent(self, QEvent(174))
#                event.accept()
# 
#        def mouseMoveEvent(self, event):
#            if event.buttons() == Qt.LeftButton:
#                self.move(event.globalPos() - self.dragPosition)
#                event.accept()
                
        self.emailInfo = {
            "email": "1435679023@qq.com",
            "pwd": "19960229hexinABC",
            "to_addr": "",
            "smtp_server": "smtp.qq.com",
            "pop3_server":"pop.qq.com",
            "subject": "",
            "html": "",
            "plain": "",
        }

        # 邮件数量
        self.index = 0
        self.page = 0

        # 绑定QListWidget
        self.emaillist.addItem("1")
        self.emaillist.addItem("235")
        self.emaillist.addItem("236")
        self.emaillist.addItem("241")
        self.connect(self.emaillist, SIGNAL('itemClicked(QListWidgetItem *)'), self.itemClicked) 



    @pyqtSlot()
    def itemClicked(self):
        my_currentItem = self.emaillist.currentItem()
        my_text = my_currentItem.text()
        self.webView.setUrl(QtCore.QUrl("../data/%s.html"%str(my_text)))

    @pyqtSlot()
    def on_calender_clicked(self):
        my_calender = calenderDialog()
        my_calender.exec_()
       
    @pyqtSlot()
    def on_mainwriteletter_clicked(self):
        my_writemail  = WriteEmailDialog()
        my_writemail.exec_()
    
    def addQListWidgetItem(self):
        self.emaillist.addItem("qwe")
        self.emaillist.addItem("abc")
        self.emaillist.addItem("dsfd")
        self.emaillist.addItem("cdas")

    @pyqtSlot()
    def on_mainreceiveletter_clicked(self):
        my_index = ReceiveMail().GetEmailNum()
        print(my_index)
        my_pop3 = ReceiveMail().Receive(my_index)
        my_addItem = self.addQListWidgetItem()
        p1 = Process(target=my_pop3)
        p1.start()
        p1.join()

        p2 = Process(target=my_addItem)
        p2.start()
        p2.join()


    def on_mainclose_clicked(self):
        self.close()
    
    @pyqtSlot()
    def on_mainmin_clicked(self):
        self.showMinimized()
        
    
    @pyqtSlot()
    def on_emailsort_clicked(self):
        print("排序")


        
    @pyqtSlot()
    def on_moreemail_clicked(self):
        self.page += 1
        my_index = ReceiveMail().GetEmailNum()
        my_next_index = my_index - 6*self.page
        print(my_index)
        my_pop3 = ReceiveMail().Receive(my_next_index)
        my_addItem = self.addQListWidgetItem()
        p1 = Process(target=my_pop3)
        print('开始收取邮件！')
        p1.start()
        p1.join()

        p2 = Process(target=my_addItem)
        p2.start()
        p2.join()
       
    
        
    @pyqtSlot()
    def on_mainlogin_clicked(self):
        print('login')
        my_login = Login()
        my_login.exec_()
        
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    app.addLibraryPath('./plugins')
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
