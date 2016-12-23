# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\14356\Desktop\EmailSystem_搜索_转发_回复_12.15\Email\Libs\writemail.ui'
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

class Ui_WriteEmailDialog(object):
    def setupUi(self, WriteEmailDialog):
        WriteEmailDialog.setObjectName(_fromUtf8("WriteEmailDialog"))
        WriteEmailDialog.resize(718, 560)
        WriteEmailDialog.setStyleSheet(_fromUtf8(""))
        WriteEmailDialog.setSizeGripEnabled(True)
        self.head = QtGui.QGroupBox(WriteEmailDialog)
        self.head.setGeometry(QtCore.QRect(0, 0, 721, 50))
        self.head.setStyleSheet(_fromUtf8("QGroupBox{background-color: rgb(244, 244, 244);}\n"
"#send,#save,#accessory{border:none;background-color: rgb(244, 244, 244);}\n"
"#send:hover{background-color: rgb(219,219,219);}\n"
"#accessory:hover{background-color: rgb(219,219,219);}\n"
"#save:hover{background-color: rgb(219,219,219);}"))
        self.head.setTitle(_fromUtf8(""))
        self.head.setObjectName(_fromUtf8("head"))
        self.send = QtGui.QPushButton(self.head)
        self.send.setGeometry(QtCore.QRect(30, 15, 60, 30))
        self.send.setStyleSheet(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/souce/souce/发送.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.send.setIcon(icon)
        self.send.setObjectName(_fromUtf8("send"))
        self.accessory = QtGui.QPushButton(self.head)
        self.accessory.setGeometry(QtCore.QRect(110, 15, 60, 30))
        self.accessory.setStyleSheet(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/souce/souce/附件.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.accessory.setIcon(icon1)
        self.accessory.setObjectName(_fromUtf8("accessory"))
        self.save = QtGui.QPushButton(self.head)
        self.save.setGeometry(QtCore.QRect(190, 15, 81, 30))
        self.save.setStyleSheet(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/souce/souce/保存.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save.setIcon(icon2)
        self.save.setObjectName(_fromUtf8("save"))
        self.groupBox = QtGui.QGroupBox(WriteEmailDialog)
        self.groupBox.setGeometry(QtCore.QRect(0, 49, 720, 91))
        self.groupBox.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.subject = QtGui.QLabel(self.groupBox)
        self.subject.setGeometry(QtCore.QRect(40, 60, 60, 15))
        self.subject.setObjectName(_fromUtf8("subject"))
        self.subjectEdit = QtGui.QLineEdit(self.groupBox)
        self.subjectEdit.setGeometry(QtCore.QRect(100, 60, 271, 20))
        self.subjectEdit.setObjectName(_fromUtf8("subjectEdit"))
        self.receiver = QtGui.QLabel(self.groupBox)
        self.receiver.setGeometry(QtCore.QRect(40, 10, 60, 15))
        self.receiver.setObjectName(_fromUtf8("receiver"))
        self.receiverEdit = QtGui.QLineEdit(self.groupBox)
        self.receiverEdit.setGeometry(QtCore.QRect(100, 10, 271, 20))
        self.receiverEdit.setObjectName(_fromUtf8("receiverEdit"))
        self.emailContent = QtGui.QPlainTextEdit(WriteEmailDialog)
        self.emailContent.setGeometry(QtCore.QRect(0, 199, 720, 361))
        self.emailContent.setPlainText(_fromUtf8(""))
        self.emailContent.setObjectName(_fromUtf8("emailContent"))
        self.richEmailEdit = QtWebKit.QWebView(WriteEmailDialog)
        self.richEmailEdit.setGeometry(QtCore.QRect(0, 140, 721, 411))
        self.richEmailEdit.setUrl(QtCore.QUrl(_fromUtf8("file:///C:/Users/14356/Desktop/EmailSystem_搜索_转发_回复_12.15/Email/Libs/kindeditor-4.1.7/examples/default.html")))
        self.richEmailEdit.setObjectName(_fromUtf8("richEmailEdit"))

        self.retranslateUi(WriteEmailDialog)
        QtCore.QMetaObject.connectSlotsByName(WriteEmailDialog)
        WriteEmailDialog.setTabOrder(self.receiverEdit, self.subjectEdit)
        WriteEmailDialog.setTabOrder(self.subjectEdit, self.send)
        WriteEmailDialog.setTabOrder(self.send, self.accessory)
        WriteEmailDialog.setTabOrder(self.accessory, self.save)
        WriteEmailDialog.setTabOrder(self.save, self.richEmailEdit)
        WriteEmailDialog.setTabOrder(self.richEmailEdit, self.emailContent)

    def retranslateUi(self, WriteEmailDialog):
        WriteEmailDialog.setWindowTitle(_translate("WriteEmailDialog", "Dialog", None))
        self.send.setText(_translate("WriteEmailDialog", "发送", None))
        self.accessory.setText(_translate("WriteEmailDialog", "附件", None))
        self.save.setText(_translate("WriteEmailDialog", "存入草稿", None))
        self.subject.setText(_translate("WriteEmailDialog", "主 题:", None))
        self.receiver.setText(_translate("WriteEmailDialog", "收件人:", None))

from PyQt4 import QtWebKit
import souce_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    WriteEmailDialog = QtGui.QDialog()
    ui = Ui_WriteEmailDialog()
    ui.setupUi(WriteEmailDialog)
    WriteEmailDialog.show()
    sys.exit(app.exec_())

