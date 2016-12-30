# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\14356\Desktop\XYZMail\Libs\contacts.ui'
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

class Ui_contacts(object):
    def setupUi(self, contacts):
        contacts.setObjectName(_fromUtf8("contacts"))
        contacts.resize(745, 565)
        contacts.setMinimumSize(QtCore.QSize(741, 560))
        contacts.setMaximumSize(QtCore.QSize(745, 565))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/souce/souce/登录.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        contacts.setWindowIcon(icon)
        contacts.setStyleSheet(_fromUtf8("font: 11pt \"微软雅黑\";"))
        contacts.setSizeGripEnabled(True)
        self.contactsBack = QtGui.QWidget(contacts)
        self.contactsBack.setGeometry(QtCore.QRect(0, 0, 1000, 600))
        self.contactsBack.setMinimumSize(QtCore.QSize(1000, 600))
        self.contactsBack.setMaximumSize(QtCore.QSize(1000, 600))
        self.contactsBack.setStyleSheet(_fromUtf8("background-color: rgb(66, 74, 89);"))
        self.contactsBack.setObjectName(_fromUtf8("contactsBack"))
        self.label_7 = QtGui.QLabel(self.contactsBack)
        self.label_7.setGeometry(QtCore.QRect(290, 0, 100, 51))
        self.label_7.setStyleSheet(_fromUtf8("color:white;"))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.contactsBox = QtGui.QWidget(self.contactsBack)
        self.contactsBox.setGeometry(QtCore.QRect(0, 49, 1000, 541))
        self.contactsBox.setStyleSheet(_fromUtf8("background-color: rgb(219,219,219);\n"
""))
        self.contactsBox.setObjectName(_fromUtf8("contactsBox"))
        self.contactINfo = QtGui.QWidget(self.contactsBox)
        self.contactINfo.setGeometry(QtCore.QRect(479, 0, 521, 550))
        self.contactINfo.setStyleSheet(_fromUtf8("background-color: rgb(219,219,219);"))
        self.contactINfo.setObjectName(_fromUtf8("contactINfo"))
        self.contactsList = QtGui.QListWidget(self.contactsBox)
        self.contactsList.setGeometry(QtCore.QRect(11, 10, 221, 501))
        self.contactsList.setStyleSheet(_fromUtf8("#contactsList{border:none;background-color: rgb(238, 238, 238);}\n"
"\n"
"\n"
"#contactsList::Item{\n"
"width:260px;\n"
"height:55px;\n"
"}\n"
"#contactsList::Item:hover{\n"
"background-color: rgb(41, 189, 139);\n"
"}"))
        self.contactsList.setFrameShape(QtGui.QFrame.StyledPanel)
        self.contactsList.setLineWidth(1)
        self.contactsList.setIconSize(QtCore.QSize(55, 55))
        self.contactsList.setGridSize(QtCore.QSize(200, 65))
        self.contactsList.setViewMode(QtGui.QListView.ListMode)
        self.contactsList.setModelColumn(0)
        self.contactsList.setWordWrap(False)
        self.contactsList.setObjectName(_fromUtf8("contactsList"))
        self.createContact = QtGui.QPushButton(self.contactsBox)
        self.createContact.setGeometry(QtCore.QRect(30, 470, 26, 26))
        self.createContact.setStyleSheet(_fromUtf8("#createContact{\n"
"background-color: rgb(37, 172, 125);\n"
"border-radius:13px;\n"
"border:none;\n"
"font: 75 25px \"Consolas\";\n"
"color:white;\n"
"}\n"
"#createContact:hover{\n"
"background-color: rgb(37, 172, 125);\n"
"    background-color: rgb(46, 213, 155);\n"
"}"))
        self.createContact.setObjectName(_fromUtf8("createContact"))
        self.contInfoTop = QtGui.QGroupBox(self.contactsBox)
        self.contInfoTop.setGeometry(QtCore.QRect(240, 10, 501, 111))
        self.contInfoTop.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 238);"))
        self.contInfoTop.setTitle(_fromUtf8(""))
        self.contInfoTop.setObjectName(_fromUtf8("contInfoTop"))
        self.contLogo = QtGui.QLabel(self.contInfoTop)
        self.contLogo.setGeometry(QtCore.QRect(29, 19, 80, 80))
        self.contLogo.setStyleSheet(_fromUtf8(""))
        self.contLogo.setText(_fromUtf8(""))
        self.contLogo.setObjectName(_fromUtf8("contLogo"))
        self.contWriteLetter = QtGui.QPushButton(self.contInfoTop)
        self.contWriteLetter.setGeometry(QtCore.QRect(270, 10, 100, 30))
        self.contWriteLetter.setStyleSheet(_fromUtf8("#contWriteLetter{\n"
"    border:none;\n"
"    font-size:14px;\n"
"    background-color:rgb(219,219,219);\n"
"}\n"
"#contWriteLetter:hover{\n"
"background-color: rgb(26, 227, 159);\n"
"color:white;\n"
"}"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/souce/souce/发送.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.contWriteLetter.setIcon(icon1)
        self.contWriteLetter.setObjectName(_fromUtf8("contWriteLetter"))
        self.delContact = QtGui.QPushButton(self.contInfoTop)
        self.delContact.setGeometry(QtCore.QRect(390, 10, 100, 30))
        self.delContact.setStyleSheet(_fromUtf8("#delContact{\n"
"    border:none;\n"
"    font-size:14px;\n"
"    background-color: rgb(219,219,219);\n"
"}\n"
"#delContact:hover{\n"
"background-color:tomato;\n"
"color:white;\n"
"}"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/souce/souce/关闭1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delContact.setIcon(icon2)
        self.delContact.setObjectName(_fromUtf8("delContact"))
        self.label_8 = QtGui.QLabel(self.contInfoTop)
        self.label_8.setGeometry(QtCore.QRect(120, 43, 51, 21))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.contInfoTop)
        self.label_9.setGeometry(QtCore.QRect(120, 66, 51, 31))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.contName = QtGui.QLineEdit(self.contInfoTop)
        self.contName.setGeometry(QtCore.QRect(180, 44, 241, 21))
        self.contName.setStyleSheet(_fromUtf8("#contName{border:none;}\n"
"#contName:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"}"))
        self.contName.setText(_fromUtf8(""))
        self.contName.setObjectName(_fromUtf8("contName"))
        self.contEmail = QtGui.QLineEdit(self.contInfoTop)
        self.contEmail.setGeometry(QtCore.QRect(180, 72, 241, 21))
        self.contEmail.setStyleSheet(_fromUtf8("#contEmail{\n"
"border:none;\n"
"}\n"
"#contEmail:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"}"))
        self.contEmail.setText(_fromUtf8(""))
        self.contEmail.setObjectName(_fromUtf8("contEmail"))
        self.createAlert = QtGui.QLabel(self.contInfoTop)
        self.createAlert.setGeometry(QtCore.QRect(120, 10, 141, 31))
        self.createAlert.setStyleSheet(_fromUtf8("color:tomato;"))
        self.createAlert.setObjectName(_fromUtf8("createAlert"))
        self.must2 = QtGui.QLabel(self.contInfoTop)
        self.must2.setGeometry(QtCore.QRect(100, 40, 21, 21))
        self.must2.setStyleSheet(_fromUtf8("color:tomato;"))
        self.must2.setObjectName(_fromUtf8("must2"))
        self.must1 = QtGui.QLabel(self.contInfoTop)
        self.must1.setGeometry(QtCore.QRect(100, 70, 21, 21))
        self.must1.setStyleSheet(_fromUtf8("color:tomato;"))
        self.must1.setObjectName(_fromUtf8("must1"))
        self.contInfoBottom = QtGui.QGroupBox(self.contactsBox)
        self.contInfoBottom.setGeometry(QtCore.QRect(240, 130, 501, 381))
        self.contInfoBottom.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 238);"))
        self.contInfoBottom.setTitle(_fromUtf8(""))
        self.contInfoBottom.setObjectName(_fromUtf8("contInfoBottom"))
        self.label = QtGui.QLabel(self.contInfoBottom)
        self.label.setGeometry(QtCore.QRect(30, 18, 71, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.contInfoBottom)
        self.label_2.setGeometry(QtCore.QRect(63, 68, 61, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.contInfoBottom)
        self.label_3.setGeometry(QtCore.QRect(43, 98, 81, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.contInfoBottom)
        self.label_4.setGeometry(QtCore.QRect(30, 170, 71, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.contInfoBottom)
        self.label_5.setGeometry(QtCore.QRect(80, 210, 31, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.contInfoBottom)
        self.label_6.setGeometry(QtCore.QRect(50, 240, 71, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.contRemarkName = QtGui.QLineEdit(self.contInfoBottom)
        self.contRemarkName.setGeometry(QtCore.QRect(130, 67, 241, 21))
        self.contRemarkName.setObjectName(_fromUtf8("contRemarkName"))
        self.contPhone = QtGui.QLineEdit(self.contInfoBottom)
        self.contPhone.setGeometry(QtCore.QRect(130, 98, 241, 21))
        self.contPhone.setObjectName(_fromUtf8("contPhone"))
        self.contQQ = QtGui.QLineEdit(self.contInfoBottom)
        self.contQQ.setGeometry(QtCore.QRect(130, 210, 241, 21))
        self.contQQ.setObjectName(_fromUtf8("contQQ"))
        self.contWechat = QtGui.QLineEdit(self.contInfoBottom)
        self.contWechat.setGeometry(QtCore.QRect(130, 240, 241, 21))
        self.contWechat.setObjectName(_fromUtf8("contWechat"))
        self.contReset = QtGui.QPushButton(self.contInfoBottom)
        self.contReset.setGeometry(QtCore.QRect(280, 310, 90, 30))
        self.contReset.setStyleSheet(_fromUtf8("#contReset{\n"
"    border:none;\n"
"    font-size:14px;\n"
"color:white;\n"
"    background-color: rgb(29, 171, 123);\n"
"}\n"
"#contReset:hover{\n"
"background-color: rgb(26, 227, 159);\n"
"}"))
        self.contReset.setObjectName(_fromUtf8("contReset"))
        self.contSave = QtGui.QPushButton(self.contInfoBottom)
        self.contSave.setGeometry(QtCore.QRect(130, 310, 90, 30))
        self.contSave.setStyleSheet(_fromUtf8("#contSave{\n"
"    border:none;\n"
"    font-size:14px;\n"
"color:white;\n"
"    background-color: rgb(29, 171, 123);\n"
"}\n"
"#contSave:hover{\n"
"background-color: rgb(26, 227, 159);\n"
"}"))
        self.contSave.setObjectName(_fromUtf8("contSave"))
        self.sync = QtGui.QPushButton(self.contactsBox)
        self.sync.setGeometry(QtCore.QRect(70, 470, 26, 26))
        self.sync.setStyleSheet(_fromUtf8("#sync{\n"
"background-color: rgb(37, 172, 125);\n"
"border-radius:13px;\n"
"border:none;\n"
"font: 75 25px \"Consolas\";\n"
"color:white;\n"
"}\n"
"#sync:hover{\n"
"background-color: rgb(37, 172, 125);\n"
"    background-color: rgb(46, 213, 155);\n"
"}"))
        self.sync.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/souce/souce/同步.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sync.setIcon(icon3)
        self.sync.setObjectName(_fromUtf8("sync"))
        self.contClose = QtGui.QPushButton(self.contactsBack)
        self.contClose.setGeometry(QtCore.QRect(710, 10, 20, 20))
        self.contClose.setStyleSheet(_fromUtf8("#contClose{\n"
"    background-color:tomato;\n"
"    border-radius:10px;}\n"
"#contClose:hover{border-image: url(:/souce/souce/关闭1.png);}\n"
""))
        self.contClose.setText(_fromUtf8(""))
        self.contClose.setObjectName(_fromUtf8("contClose"))
        self.contMin = QtGui.QPushButton(self.contactsBack)
        self.contMin.setGeometry(QtCore.QRect(680, 10, 20, 20))
        self.contMin.setToolTip(_fromUtf8(""))
        self.contMin.setStyleSheet(_fromUtf8("#contMin{\n"
"background-color:rgb(255,224,81);\n"
"    border-radius:10px;}\n"
"#contMin:hover{\n"
"    border-image: url(:/souce/souce/最小化.png);\n"
"}\n"
""))
        self.contMin.setText(_fromUtf8(""))
        self.contMin.setObjectName(_fromUtf8("contMin"))
        self.contUserMail = QtGui.QLabel(self.contactsBack)
        self.contUserMail.setGeometry(QtCore.QRect(70, 0, 211, 48))
        self.contUserMail.setStyleSheet(_fromUtf8("#contUserMail{\n"
"    font: 75 14px \"微软雅黑\";\n"
"color:white;\n"
"}"))
        self.contUserMail.setText(_fromUtf8(""))
        self.contUserMail.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.contUserMail.setObjectName(_fromUtf8("contUserMail"))
        self.contUserLogo = QtGui.QLabel(self.contactsBack)
        self.contUserLogo.setGeometry(QtCore.QRect(0, 0, 48, 48))
        self.contUserLogo.setStyleSheet(_fromUtf8("border-radius:24px;\n"
"background-color: transparent;"))
        self.contUserLogo.setText(_fromUtf8(""))
        self.contUserLogo.setObjectName(_fromUtf8("contUserLogo"))

        self.retranslateUi(contacts)
        QtCore.QMetaObject.connectSlotsByName(contacts)

    def retranslateUi(self, contacts):
        contacts.setWindowTitle(_translate("contacts", "联系人", None))
        self.label_7.setText(_translate("contacts", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">通讯录</span></p></body></html>", None))
        self.contactsList.setSortingEnabled(True)
        self.createContact.setToolTip(_translate("contacts", "新建联系人", None))
        self.createContact.setWhatsThis(_translate("contacts", "新建联系人", None))
        self.createContact.setText(_translate("contacts", "+", None))
        self.contWriteLetter.setText(_translate("contacts", "写信", None))
        self.delContact.setText(_translate("contacts", "删除联系人", None))
        self.label_8.setText(_translate("contacts", "用户名:", None))
        self.label_9.setText(_translate("contacts", "邮   箱:", None))
        self.createAlert.setText(_translate("contacts", "请在此添加用户信息", None))
        self.must2.setText(_translate("contacts", "*", None))
        self.must1.setText(_translate("contacts", "*", None))
        self.label.setText(_translate("contacts", "基本信息", None))
        self.label_2.setText(_translate("contacts", "备注：", None))
        self.label_3.setText(_translate("contacts", "联系电话:", None))
        self.label_4.setText(_translate("contacts", "社交信息", None))
        self.label_5.setText(_translate("contacts", "QQ:", None))
        self.label_6.setText(_translate("contacts", "WeChat:", None))
        self.contReset.setText(_translate("contacts", "重置", None))
        self.contSave.setText(_translate("contacts", "保存", None))
        self.sync.setToolTip(_translate("contacts", "同步联系人", None))

import avatars_rc
import souce_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    contacts = QtGui.QDialog()
    ui = Ui_contacts()
    ui.setupUi(contacts)
    contacts.show()
    sys.exit(app.exec_())

