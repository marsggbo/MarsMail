# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\14356\Desktop\EmailSystem\Email\Libs\login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(500, 300)
        Dialog.setSizeGripEnabled(True)
        self.loginlogo = QtGui.QLabel(Dialog)
        self.loginlogo.setGeometry(QtCore.QRect(180, 0, 101, 51))
        self.loginlogo.setAlignment(QtCore.Qt.AlignCenter)
        self.loginlogo.setObjectName(_fromUtf8("loginlogo"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(0, 50, 500, 51))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.loginmail = QtGui.QLineEdit(self.groupBox)
        self.loginmail.setGeometry(QtCore.QRect(180, 13, 190, 25))
        self.loginmail.setObjectName(_fromUtf8("loginmail"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(130, 13, 50, 25))
        self.label.setObjectName(_fromUtf8("label"))
        self.groupBox_3 = QtGui.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 152, 500, 51))
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.loginsmtp = QtGui.QLineEdit(self.groupBox_3)
        self.loginsmtp.setGeometry(QtCore.QRect(180, 13, 190, 25))
        self.loginsmtp.setObjectName(_fromUtf8("loginsmtp"))
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(110, 13, 50, 25))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 101, 500, 51))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.loginpwd = QtGui.QLineEdit(self.groupBox_2)
        self.loginpwd.setGeometry(QtCore.QRect(180, 13, 190, 25))
        self.loginpwd.setText(_fromUtf8(""))
        self.loginpwd.setEchoMode(QtGui.QLineEdit.Password)
        self.loginpwd.setObjectName(_fromUtf8("loginpwd"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(130, 13, 50, 25))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.groupBox_4 = QtGui.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(0, 203, 500, 51))
        self.groupBox_4.setTitle(_fromUtf8(""))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.loginpop = QtGui.QLineEdit(self.groupBox_4)
        self.loginpop.setGeometry(QtCore.QRect(180, 13, 190, 25))
        self.loginpop.setObjectName(_fromUtf8("loginpop"))
        self.label_4 = QtGui.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(110, 13, 50, 25))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.login = QtGui.QPushButton(Dialog)
        self.login.setGeometry(QtCore.QRect(130, 260, 75, 23))
        self.login.setObjectName(_fromUtf8("login"))
        self.cancel = QtGui.QPushButton(Dialog)
        self.cancel.setGeometry(QtCore.QRect(270, 260, 75, 23))
        self.cancel.setObjectName(_fromUtf8("cancel"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.loginlogo.setText(_translate("Dialog", "假装有logo", None))
        self.label.setText(_translate("Dialog", "邮箱:", None))
        self.label_3.setText(_translate("Dialog", "SMTP配置", None))
        self.label_2.setText(_translate("Dialog", "密码:", None))
        self.label_4.setText(_translate("Dialog", "POP3配置", None))
        self.login.setText(_translate("Dialog", "登录", None))
        self.cancel.setText(_translate("Dialog", "取消", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

