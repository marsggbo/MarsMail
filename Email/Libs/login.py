# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""
import smtplib
import json
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QDialog

from Ui_login import Ui_Dialog

# {
#   "email":"1435679023@qq.com",
#   "pwd":"19960229hexinABC",
#   "smtp_server":"smtp.qq.com",
#   "pop3_server":"pop.qq.com"
#
# }

def GetLoginInfo():
    f = open('conf.json','r',encoding='utf-8')
    s = json.load(f)
    f.close()
    return s

def SaveLoginInfo(data):
    f = open("conf.json","w",encoding='utf-8')
    data.write(json.loads(data))
    f.close()

class Login(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setupUi(self)
        self.email = GetLoginInfo()
        if self.email["email"] and self.email["pwd"]:
            email = self.email["email"]
            pwd = self.email["pwd"]
            self.loginmail.setText(email)
            self.loginpwd.setText(pwd)
            smtp_server = 'smtp.'+ email.split("@")[1]
            pop3_server = 'pop.'+ email.split("@")[1]
            self.loginsmtp.setText(smtp_server)
            self.loginpop.setText(pop3_server)

    @pyqtSlot()
    def on_login_clicked(self):
        self.email["email"] = self.loginmail.text()
        self.email["pwd"] = self.loginpwd.text()
        self.email["smtp_server"] = self.loginsmtp.text()
        self.email["pop3_server"] = self.loginpop.text()
        try:
            server = smtplib.SMTP_SSL(self.email["smtp_server"], 465)

            # server.set_debuglevel(1)
            server.login(self.email["email"], self.email["pwd"])

        except Exception as e:
            print(type(e))
            print(e)
        self.close()
    
    
    @pyqtSlot()
    def on_cancel_clicked(self):
       self.close()
