# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\14356\Desktop\EmailSystem\Email\Libs\main.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1069, 590)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 570))
        MainWindow.setMaximumSize(QtCore.QSize(1069, 590))
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/pics/pics/XYZ.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8(""))
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.widget = QtGui.QWidget(self.centralWidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 200, 590))
        self.widget.setWhatsThis(_fromUtf8(""))
        self.widget.setStyleSheet(_fromUtf8("#widget{background-color: rgb(242, 242, 242);}\n"
"\n"
"QPushButton{border:none;}"))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.headpic_2 = QtGui.QGraphicsView(self.widget)
        self.headpic_2.setGeometry(QtCore.QRect(0, 0, 200, 50))
        self.headpic_2.setMaximumSize(QtCore.QSize(200, 50))
        self.headpic_2.setStyleSheet(_fromUtf8("border-image: url(:/souce/souce/XYZ.jpg);"))
        self.headpic_2.setObjectName(_fromUtf8("headpic_2"))
        self.slidebar = QtGui.QGroupBox(self.widget)
        self.slidebar.setGeometry(QtCore.QRect(0, 425, 26, 171))
        self.slidebar.setStyleSheet(_fromUtf8("QGroupBox{background-color: rgb(79, 79, 79);}\n"
"QPushButton{\n"
"    width:20px;\n"
"    height:20px;\n"
"}\n"
"QPushButton:hover {\n"
"       Background-color:rgb(29,171,123);\n"
"}"))
        self.slidebar.setObjectName(_fromUtf8("slidebar"))
        self.email = QtGui.QPushButton(self.slidebar)
        self.email.setGeometry(QtCore.QRect(2, 19, 25, 25))
        self.email.setMouseTracking(False)
        self.email.setAccessibleName(_fromUtf8(""))
        self.email.setStyleSheet(_fromUtf8("#sliderbar1:hover{\n"
"background-color: rgb(255, 170, 127);}"))
        self.email.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/souce/souce/邮箱 (1).png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.email.setIcon(icon1)
        self.email.setObjectName(_fromUtf8("email"))
        self.addressbook = QtGui.QPushButton(self.slidebar)
        self.addressbook.setGeometry(QtCore.QRect(2, 56, 25, 25))
        self.addressbook.setStyleSheet(_fromUtf8("leftbar QPushButtom{background-color:gray;}"))
        self.addressbook.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/souce/souce/通讯录.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addressbook.setIcon(icon2)
        self.addressbook.setObjectName(_fromUtf8("addressbook"))
        self.calender = QtGui.QPushButton(self.slidebar)
        self.calender.setGeometry(QtCore.QRect(2, 93, 25, 25))
        self.calender.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/souce/souce/日历.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.calender.setIcon(icon3)
        self.calender.setObjectName(_fromUtf8("calender"))
        self.settings = QtGui.QPushButton(self.slidebar)
        self.settings.setGeometry(QtCore.QRect(2, 130, 25, 25))
        self.settings.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/souce/souce/设置.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings.setIcon(icon4)
        self.settings.setObjectName(_fromUtf8("settings"))
        self.headlogo = QtGui.QGraphicsView(self.widget)
        self.headlogo.setGeometry(QtCore.QRect(60, 100, 80, 80))
        self.headlogo.setStyleSheet(_fromUtf8("border-image: url(:/souce/souce/登录.png);"))
        self.headlogo.setObjectName(_fromUtf8("headlogo"))
        self.groupBox = QtGui.QGroupBox(self.widget)
        self.groupBox.setGeometry(QtCore.QRect(0, 50, 200, 50))
        self.groupBox.setStyleSheet(_fromUtf8("QPushButton{background-color:rgb(41,189,139);}\n"
"QPushButton:hover {\n"
"       Background-color:rgb(29,171,123);\n"
"}"))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.mainwriteletter = QtGui.QPushButton(self.groupBox)
        self.mainwriteletter.setGeometry(QtCore.QRect(0, 0, 102, 50))
        self.mainwriteletter.setObjectName(_fromUtf8("mainwriteletter"))
        self.mainreceiveletter = QtGui.QPushButton(self.groupBox)
        self.mainreceiveletter.setGeometry(QtCore.QRect(100, 0, 100, 50))
        self.mainreceiveletter.setObjectName(_fromUtf8("mainreceiveletter"))
        self.mainlogin = QtGui.QPushButton(self.widget)
        self.mainlogin.setGeometry(QtCore.QRect(65, 200, 70, 25))
        self.mainlogin.setStyleSheet(_fromUtf8("background-color: rgb(41, 189, 139);"))
        self.mainlogin.setObjectName(_fromUtf8("mainlogin"))
        self.menu = QtGui.QWidget(self.centralWidget)
        self.menu.setGeometry(QtCore.QRect(200, 0, 870, 50))
        self.menu.setStyleSheet(_fromUtf8("background-color: rgb(66, 74, 89);\n"
"border:none;"))
        self.menu.setObjectName(_fromUtf8("menu"))
        self.graphicsView = QtGui.QGraphicsView(self.menu)
        self.graphicsView.setGeometry(QtCore.QRect(10, 15, 20, 20))
        self.graphicsView.setStyleSheet(_fromUtf8("border-image: url(:/souce/souce/搜索.png);"))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.searchlineEdit = QtGui.QLineEdit(self.menu)
        self.searchlineEdit.setGeometry(QtCore.QRect(40, 16, 140, 18))
        self.searchlineEdit.setStyleSheet(_fromUtf8("#searchlineEdit{background-color:white;}"))
        self.searchlineEdit.setText(_fromUtf8(""))
        self.searchlineEdit.setObjectName(_fromUtf8("searchlineEdit"))
        self.searchrange = QtGui.QGroupBox(self.menu)
        self.searchrange.setGeometry(QtCore.QRect(200, 0, 26, 50))
        self.searchrange.setStyleSheet(_fromUtf8("#searchrange{border:none;}\n"
"QGroupBox:hover{background-color: rgb(255, 255, 127);}\n"
"\n"
""))
        self.searchrange.setTitle(_fromUtf8(""))
        self.searchrange.setObjectName(_fromUtf8("searchrange"))
        self.pushButton = QtGui.QPushButton(self.searchrange)
        self.pushButton.setGeometry(QtCore.QRect(3, 15, 20, 20))
        self.pushButton.setStyleSheet(_fromUtf8("border-image: url(:/souce/souce/下拉 (2).png);"))
        self.pushButton.setText(_fromUtf8(""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.mainclose = QtGui.QPushButton(self.menu)
        self.mainclose.setGeometry(QtCore.QRect(830, 15, 20, 20))
        self.mainclose.setStyleSheet(_fromUtf8("#mainclose{\n"
"    background-color:tomato;\n"
"    border-radius:10px;}\n"
"#mainclose:hover{border-image: url(:/souce/souce/关闭1.png);}\n"
""))
        self.mainclose.setText(_fromUtf8(""))
        self.mainclose.setObjectName(_fromUtf8("mainclose"))
        self.mainmin = QtGui.QPushButton(self.menu)
        self.mainmin.setGeometry(QtCore.QRect(800, 15, 20, 20))
        self.mainmin.setToolTip(_fromUtf8(""))
        self.mainmin.setStyleSheet(_fromUtf8("#mainmin{\n"
"background-color:rgb(255,224,81);\n"
"    border-radius:10px;}\n"
"#mainmin:hover{\n"
"border-image: url(:/souce/souce/最小化.png);\n"
"}\n"
""))
        self.mainmin.setText(_fromUtf8(""))
        self.mainmin.setObjectName(_fromUtf8("mainmin"))
        self.receivedletter = QtGui.QGroupBox(self.centralWidget)
        self.receivedletter.setGeometry(QtCore.QRect(200, 50, 260, 540))
        self.receivedletter.setStyleSheet(_fromUtf8("#receivedletter{background-color: white;}\n"
"#receivedletter QPushButton{\n"
"    background-color: rgb(243,243,243);\n"
"    border:none;\n"
"}\n"
"#receivedletter QPushButton:hover{\n"
"    color:rgb(29,171,123);\n"
"}"))
        self.receivedletter.setTitle(_fromUtf8(""))
        self.receivedletter.setObjectName(_fromUtf8("receivedletter"))
        self.emailsort = QtGui.QPushButton(self.receivedletter)
        self.emailsort.setGeometry(QtCore.QRect(0, 0, 132, 50))
        self.emailsort.setObjectName(_fromUtf8("emailsort"))
        self.moreemail = QtGui.QPushButton(self.receivedletter)
        self.moreemail.setGeometry(QtCore.QRect(130, 0, 130, 50))
        self.moreemail.setObjectName(_fromUtf8("moreemail"))
        self.emaillist = QtGui.QListWidget(self.receivedletter)
        self.emaillist.setGeometry(QtCore.QRect(0, 50, 260, 490))
        self.emaillist.setGridSize(QtCore.QSize(260, 80))
        self.emaillist.setObjectName(_fromUtf8("emaillist"))
        self.showemail = QtGui.QGroupBox(self.centralWidget)
        self.showemail.setGeometry(QtCore.QRect(459, 50, 611, 540))
        self.showemail.setStyleSheet(_fromUtf8("#showemail{background-color: white;}\n"
""))
        self.showemail.setTitle(_fromUtf8(""))
        self.showemail.setObjectName(_fromUtf8("showemail"))
        self.emailShow = QtWebKit.QWebView(self.showemail)
        self.emailShow.setGeometry(QtCore.QRect(0, 0, 611, 544))
        self.emailShow.setUrl(QtCore.QUrl(_fromUtf8("qrc:/souce/index.html")))
        self.emailShow.setObjectName(_fromUtf8("emailShow"))
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.emaillist.setCurrentRow(-1)
        QtCore.QObject.connect(self.email, QtCore.SIGNAL(_fromUtf8("clicked()")), self.receivedletter.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "XYZ Mail", None))
        self.email.setToolTip(_translate("MainWindow", "邮件", None))
        self.addressbook.setToolTip(_translate("MainWindow", "通讯录", None))
        self.addressbook.setWhatsThis(_translate("MainWindow", "通讯录", None))
        self.calender.setToolTip(_translate("MainWindow", "日历", None))
        self.settings.setToolTip(_translate("MainWindow", "设置", None))
        self.mainwriteletter.setText(_translate("MainWindow", "写信", None))
        self.mainreceiveletter.setText(_translate("MainWindow", "收信", None))
        self.mainlogin.setText(_translate("MainWindow", "登录", None))
        self.searchlineEdit.setPlaceholderText(_translate("MainWindow", "搜索邮件信息", None))
        self.emailsort.setText(_translate("MainWindow", "排序", None))
        self.moreemail.setText(_translate("MainWindow", "更多", None))
        self.emaillist.setSortingEnabled(False)

from PyQt4 import QtWebKit
import souce_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

