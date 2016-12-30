# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\14356\Desktop\XYZMail\Libs\writemail.ui'
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
        self.head = QtGui.QWidget(WriteEmailDialog)
        self.head.setGeometry(QtCore.QRect(0, 0, 721, 41))
        self.head.setStyleSheet(_fromUtf8("#head{background-color: rgb(66,74,89);}\n"
"#send,#save,#accessory{border:none;background-color: rgb(66,74,89);color:white;border-radius:15px;}\n"
"#send:hover,#accessory:hover,#save:hover{background-color: rgb(90,90,90);}\n"
"\n"
""))
        self.head.setObjectName(_fromUtf8("head"))
        self.send = QtGui.QPushButton(self.head)
        self.send.setGeometry(QtCore.QRect(30, 5, 60, 30))
        self.send.setStyleSheet(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/souce/souce/发送.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.send.setIcon(icon)
        self.send.setObjectName(_fromUtf8("send"))
        self.accessory = QtGui.QPushButton(self.head)
        self.accessory.setGeometry(QtCore.QRect(110, 5, 60, 30))
        self.accessory.setStyleSheet(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/souce/souce/附件.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.accessory.setIcon(icon1)
        self.accessory.setObjectName(_fromUtf8("accessory"))
        self.save = QtGui.QPushButton(self.head)
        self.save.setGeometry(QtCore.QRect(190, 5, 81, 30))
        self.save.setStyleSheet(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/souce/souce/草稿1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save.setIcon(icon2)
        self.save.setObjectName(_fromUtf8("save"))
        self.writeClose = QtGui.QPushButton(self.head)
        self.writeClose.setGeometry(QtCore.QRect(680, 10, 20, 20))
        self.writeClose.setStyleSheet(_fromUtf8("#writeClose{\n"
"    background-color:tomato;\n"
"    border-radius:10px;}\n"
"#writeClose:hover{border-image: url(:/souce/souce/关闭1.png);}\n"
""))
        self.writeClose.setText(_fromUtf8(""))
        self.writeClose.setObjectName(_fromUtf8("writeClose"))
        self.writeMin = QtGui.QPushButton(self.head)
        self.writeMin.setGeometry(QtCore.QRect(650, 10, 20, 20))
        self.writeMin.setToolTip(_fromUtf8(""))
        self.writeMin.setStyleSheet(_fromUtf8("#writeMin{\n"
"background-color:rgb(255,224,81);\n"
"    border-radius:10px;}\n"
"#writeMin:hover{\n"
"border-image: url(:/souce/souce/最小化.png);\n"
"}\n"
""))
        self.writeMin.setText(_fromUtf8(""))
        self.writeMin.setObjectName(_fromUtf8("writeMin"))
        self.groupBox = QtGui.QGroupBox(WriteEmailDialog)
        self.groupBox.setGeometry(QtCore.QRect(0, 39, 720, 101))
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
        self.attachShowBox = QtGui.QGroupBox(self.groupBox)
        self.attachShowBox.setGeometry(QtCore.QRect(390, 2, 331, 87))
        self.attachShowBox.setStyleSheet(_fromUtf8("#attachShowBox{\n"
"border:none;\n"
"}"))
        self.attachShowBox.setTitle(_fromUtf8(""))
        self.attachShowBox.setObjectName(_fromUtf8("attachShowBox"))
        self.label = QtGui.QLabel(self.attachShowBox)
        self.label.setGeometry(QtCore.QRect(0, 0, 81, 31))
        self.label.setStyleSheet(_fromUtf8("color:tomato;\n"
"font: 75 14px \"微软雅黑\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.attachList = QtGui.QListWidget(self.attachShowBox)
        self.attachList.setGeometry(QtCore.QRect(77, 0, 251, 87))
        self.attachList.setStyleSheet(_fromUtf8("#attachList{\n"
"border:none;\n"
"}\n"
"#attachList::Item{\n"
"height:30px;\n"
"}\n"
"#attachList::Item:hover{\n"
"background-color: rgb(41, 189, 139);\n"
"}"))
        self.attachList.setObjectName(_fromUtf8("attachList"))
        self.emailContent = QtGui.QPlainTextEdit(WriteEmailDialog)
        self.emailContent.setGeometry(QtCore.QRect(0, 199, 720, 361))
        self.emailContent.setPlainText(_fromUtf8(""))
        self.emailContent.setObjectName(_fromUtf8("emailContent"))
        self.richEmailEdit = QtWebKit.QWebView(WriteEmailDialog)
        self.richEmailEdit.setGeometry(QtCore.QRect(0, 140, 721, 411))
        self.richEmailEdit.setUrl(QtCore.QUrl(_fromUtf8("file:///C:/Users/14356/Desktop/EmailSystem_搜索_转发_回复_12.15/Email/Libs/kindeditor-4.1.7/examples/default.html")))
        self.richEmailEdit.setObjectName(_fromUtf8("richEmailEdit"))
        self.loading = QtGui.QLabel(WriteEmailDialog)
        self.loading.setGeometry(QtCore.QRect(240, 180, 200, 200))
        self.loading.setStyleSheet(_fromUtf8("background-color:transparent;"))
        self.loading.setText(_fromUtf8(""))
        self.loading.setObjectName(_fromUtf8("loading"))

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
        self.label.setText(_translate("WriteEmailDialog", "已添加附件", None))

from PyQt4 import QtWebKit
import avatars_rc
import souce_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    WriteEmailDialog = QtGui.QDialog()
    ui = Ui_WriteEmailDialog()
    ui.setupUi(WriteEmailDialog)
    WriteEmailDialog.show()
    sys.exit(app.exec_())

