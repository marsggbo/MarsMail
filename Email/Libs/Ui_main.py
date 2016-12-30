# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\14356\Desktop\XYZMail\Libs\main.ui'
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
        MainWindow.resize(1069, 584)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 570))
        MainWindow.setMaximumSize(QtCore.QSize(1069, 590))
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/pics/pics/XYZ.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8("*{\n"
"font: 14px \"Microsoft YaHei UI\";\n"
"border:none;\n"
"}\n"
"\n"
"/*界面上端样式*/\n"
"#topWidget{\n"
"background-color: rgb(242, 242, 242);\n"
"}\n"
"\n"
"/*下拉菜单样式*/\n"
"QComboBox{\n"
"background-color: rgb(242, 242, 242);\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"background-color: rgb(222, 222, 222);\n"
"}\n"
"/*下面是下拉按钮部分属性的设置。*/\n"
"QComboBox::drop-down {\n"
"subcontrol-origin: padding;\n"
"subcontrol-position: top right;\n"
"width: 30px;\n"
"border-left-width: 0px;\n"
"border-left-color: gray;\n"
"border-left-style: solid;\n"
"border-top-right-radius: 3px;\n"
"border-bottom-right-radius: 3px;\n"
"}\n"
" \n"
"/*下面是下拉按钮正常的背景图片。*/\n"
"QComboBox::down-arrow {\n"
"border-image: url(:/souce/souce/下拉.png);\n"
"}\n"
"\n"
"/*下面是下拉按钮鼠标放上去的背景图片。*/\n"
"QComboBox::down-arrow:hover{\n"
"border-image: url(:/souce/souce/下拉1.png);\n"
"}\n"
"\n"
"/*下面是下拉按钮鼠标按下去的背景图片。*/\n"
"/*QComboBox::down-arrow:pressed {\n"
"border-image: url(:/images/Login_Ui/drop_down_pressed.png);\n"
"}*/\n"
"\n"
"#topWidget{\n"
"background-color: rgb(66, 74, 89);\n"
"}\n"
"#searchMode{\n"
"background-color: rgb(66, 74, 89);\n"
"color:white;\n"
"border:1px solid white;\n"
"border-radius:5px;\n"
"}\n"
"#searchMode:hover{\n"
"border:1px solid rgb(41,189,139);\n"
"}\n"
"\n"
"QListWidget{\n"
"background-color:white;border:none;\n"
"}\n"
"QListWidget::Item{\n"
"width:260px;\n"
"height:80px;\n"
"}\n"
"QListWidget::Item:hover{\n"
"background-color: rgb(41, 189, 139);\n"
"}\n"
"\n"
"#leftWidget{\n"
"border:none;\n"
"background-color: rgb(242,242,242);\n"
"}\n"
"\n"
"#mainUserName{\n"
"font: 87 12px \"Arial Black\";\n"
"color: rgb(36, 170, 112);\n"
"}\n"
"\n"
"\n"
"#receivedBox:hover,#sentBox:hover,#deleteBox:hover,#draftBox:hover{\n"
"background-color: rgb(230,230,230);\n"
"color: rgb(41,189,139);\n"
"border-left:5px solid  rgb(41,189,139);\n"
"}"))
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.leftWidget = QtGui.QWidget(self.centralWidget)
        self.leftWidget.setGeometry(QtCore.QRect(0, 0, 200, 590))
        self.leftWidget.setWhatsThis(_fromUtf8(""))
        self.leftWidget.setStyleSheet(_fromUtf8(""))
        self.leftWidget.setObjectName(_fromUtf8("leftWidget"))
        self.headpic_2 = QtGui.QGraphicsView(self.leftWidget)
        self.headpic_2.setGeometry(QtCore.QRect(0, 0, 200, 50))
        self.headpic_2.setMaximumSize(QtCore.QSize(200, 50))
        self.headpic_2.setStyleSheet(_fromUtf8("border-image: url(:/souce/souce/logo渐变.png);"))
        self.headpic_2.setObjectName(_fromUtf8("headpic_2"))
        self.slidebar = QtGui.QGroupBox(self.leftWidget)
        self.slidebar.setGeometry(QtCore.QRect(0, 547, 201, 36))
        self.slidebar.setStyleSheet(_fromUtf8("QGroupBox{background-color: rgb(79, 79, 79);}\n"
"QPushButton{\n"
"    width:20px;\n"
"    height:20px;\n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(134, 134, 134);\n"
"}"))
        self.slidebar.setObjectName(_fromUtf8("slidebar"))
        self.about = QtGui.QPushButton(self.slidebar)
        self.about.setGeometry(QtCore.QRect(140, 0, 40, 40))
        self.about.setMouseTracking(False)
        self.about.setAccessibleName(_fromUtf8(""))
        self.about.setStyleSheet(_fromUtf8("#sliderbar1:hover{\n"
"background-color: rgb(255, 170, 127);}"))
        self.about.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/souce/souce/关于 (1).png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.about.setIcon(icon1)
        self.about.setObjectName(_fromUtf8("about"))
        self.addressbook = QtGui.QPushButton(self.slidebar)
        self.addressbook.setGeometry(QtCore.QRect(20, 0, 40, 40))
        self.addressbook.setStyleSheet(_fromUtf8("leftbar QPushButtom{background-color:gray;}"))
        self.addressbook.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/souce/souce/通讯录.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addressbook.setIcon(icon2)
        self.addressbook.setObjectName(_fromUtf8("addressbook"))
        self.calender = QtGui.QPushButton(self.slidebar)
        self.calender.setGeometry(QtCore.QRect(80, 0, 40, 40))
        self.calender.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/souce/souce/日历.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.calender.setIcon(icon3)
        self.calender.setObjectName(_fromUtf8("calender"))
        self.headlogo = QtGui.QGraphicsView(self.leftWidget)
        self.headlogo.setGeometry(QtCore.QRect(60, 110, 80, 80))
        self.headlogo.setStyleSheet(_fromUtf8("#headlogo{\n"
"background-color: rgb(242, 242, 242);\n"
"border-radius:40px;\n"
"}"))
        self.headlogo.setObjectName(_fromUtf8("headlogo"))
        self.groupBox = QtGui.QGroupBox(self.leftWidget)
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
        self.mainwriteletter.setStyleSheet(_fromUtf8("color:white;"))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/souce/souce/写信.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mainwriteletter.setIcon(icon4)
        self.mainwriteletter.setObjectName(_fromUtf8("mainwriteletter"))
        self.mainreceiveletter = QtGui.QPushButton(self.groupBox)
        self.mainreceiveletter.setGeometry(QtCore.QRect(100, 0, 100, 50))
        self.mainreceiveletter.setStyleSheet(_fromUtf8("color:white;"))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/souce/souce/收信 .png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mainreceiveletter.setIcon(icon5)
        self.mainreceiveletter.setObjectName(_fromUtf8("mainreceiveletter"))
        self.loading = QtGui.QLabel(self.groupBox)
        self.loading.setGeometry(QtCore.QRect(122, 10, 30, 30))
        self.loading.setText(_fromUtf8(""))
        self.loading.setObjectName(_fromUtf8("loading"))
        self.mainlogin = QtGui.QPushButton(self.leftWidget)
        self.mainlogin.setGeometry(QtCore.QRect(80, 240, 41, 41))
        self.mainlogin.setStyleSheet(_fromUtf8("#mainlogin{\n"
"background-color: rgb(41, 189, 139);\n"
"border-radius:20px;\n"
"\n"
"}\n"
"#mainlogin:hover{\n"
"    background-color: rgb(38, 234, 166);\n"
"}"))
        self.mainlogin.setObjectName(_fromUtf8("mainlogin"))
        self.mainUserName = QtGui.QLabel(self.leftWidget)
        self.mainUserName.setGeometry(QtCore.QRect(0, 200, 201, 31))
        self.mainUserName.setStyleSheet(_fromUtf8(""))
        self.mainUserName.setText(_fromUtf8(""))
        self.mainUserName.setAlignment(QtCore.Qt.AlignCenter)
        self.mainUserName.setObjectName(_fromUtf8("mainUserName"))
        self.sentBox = QtGui.QPushButton(self.leftWidget)
        self.sentBox.setGeometry(QtCore.QRect(0, 360, 201, 31))
        self.sentBox.setStyleSheet(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/souce/souce/发件箱1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sentBox.setIcon(icon6)
        self.sentBox.setIconSize(QtCore.QSize(20, 20))
        self.sentBox.setObjectName(_fromUtf8("sentBox"))
        self.receivedBox = QtGui.QPushButton(self.leftWidget)
        self.receivedBox.setGeometry(QtCore.QRect(0, 320, 201, 31))
        self.receivedBox.setStyleSheet(_fromUtf8(""))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/souce/souce/收件箱1png.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.receivedBox.setIcon(icon7)
        self.receivedBox.setIconSize(QtCore.QSize(20, 20))
        self.receivedBox.setAutoRepeat(False)
        self.receivedBox.setObjectName(_fromUtf8("receivedBox"))
        self.deleteBox = QtGui.QPushButton(self.leftWidget)
        self.deleteBox.setGeometry(QtCore.QRect(0, 400, 201, 31))
        self.deleteBox.setStyleSheet(_fromUtf8(""))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/souce/souce/垃圾箱1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteBox.setIcon(icon8)
        self.deleteBox.setIconSize(QtCore.QSize(20, 20))
        self.deleteBox.setObjectName(_fromUtf8("deleteBox"))
        self.draftBox = QtGui.QPushButton(self.leftWidget)
        self.draftBox.setGeometry(QtCore.QRect(0, 440, 201, 31))
        self.draftBox.setStyleSheet(_fromUtf8(""))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/souce/souce/草稿箱1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.draftBox.setIcon(icon9)
        self.draftBox.setIconSize(QtCore.QSize(20, 20))
        self.draftBox.setObjectName(_fromUtf8("draftBox"))
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
        self.emaillist = QtGui.QListWidget(self.receivedletter)
        self.emaillist.setGeometry(QtCore.QRect(0, 50, 260, 490))
        self.emaillist.setStyleSheet(_fromUtf8(""))
        self.emaillist.setTabKeyNavigation(True)
        self.emaillist.setObjectName(_fromUtf8("emaillist"))
        self.sentList = QtGui.QListWidget(self.receivedletter)
        self.sentList.setGeometry(QtCore.QRect(0, 50, 260, 490))
        self.sentList.setStyleSheet(_fromUtf8("#sentList{background-color: rgb(242,242,242);}\n"
"#sentList::Item{\n"
"width:260px;\n"
"height:80px;\n"
"}\n"
"#sentList::Item:hover{\n"
"background-color: rgb(41, 189, 139);\n"
"}"))
        self.sentList.setTabKeyNavigation(True)
        self.sentList.setObjectName(_fromUtf8("sentList"))
        self.searchList = QtGui.QListWidget(self.receivedletter)
        self.searchList.setGeometry(QtCore.QRect(0, 50, 260, 490))
        self.searchList.setStyleSheet(_fromUtf8("#searchList{background-color: rgb(242,242,242);}\n"
"#searchList::Item{\n"
"width:260px;\n"
"height:80px;\n"
"}\n"
"#searchList::Item:hover{\n"
"background-color: rgb(41, 189, 139);\n"
"}"))
        self.searchList.setTabKeyNavigation(True)
        self.searchList.setObjectName(_fromUtf8("searchList"))
        self.itemSortMode = QtGui.QComboBox(self.receivedletter)
        self.itemSortMode.setGeometry(QtCore.QRect(0, 0, 131, 51))
        self.itemSortMode.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.itemSortMode.setStyleSheet(_fromUtf8(""))
        self.itemSortMode.setObjectName(_fromUtf8("itemSortMode"))
        self.itemSortMode.addItem(_fromUtf8(""))
        self.itemSortMode.addItem(_fromUtf8(""))
        self.itemSortMode.addItem(_fromUtf8(""))
        self.itemSortOrder = QtGui.QComboBox(self.receivedletter)
        self.itemSortOrder.setGeometry(QtCore.QRect(130, 0, 131, 51))
        self.itemSortOrder.setStyleSheet(_fromUtf8(""))
        self.itemSortOrder.setObjectName(_fromUtf8("itemSortOrder"))
        self.itemSortOrder.addItem(_fromUtf8(""))
        self.itemSortOrder.addItem(_fromUtf8(""))
        self.deleteList = QtGui.QListWidget(self.receivedletter)
        self.deleteList.setGeometry(QtCore.QRect(0, 50, 260, 490))
        self.deleteList.setStyleSheet(_fromUtf8("#deleteList{background-color: rgb(242,242,242);}\n"
"#deleteList::Item{\n"
"width:260px;\n"
"height:80px;\n"
"}\n"
"#deleteList::Item:hover{\n"
"background-color: rgb(41, 189, 139);\n"
"}"))
        self.deleteList.setTabKeyNavigation(True)
        self.deleteList.setObjectName(_fromUtf8("deleteList"))
        self.draftList = QtGui.QListWidget(self.receivedletter)
        self.draftList.setGeometry(QtCore.QRect(0, 50, 260, 490))
        self.draftList.setStyleSheet(_fromUtf8("#draftList{background-color: rgb(242,242,242);}\n"
"#draftList::Item{\n"
"width:260px;\n"
"height:80px;\n"
"}\n"
"#draftList::Item:hover{\n"
"background-color: rgb(41, 189, 139);\n"
"}"))
        self.draftList.setTabKeyNavigation(True)
        self.draftList.setObjectName(_fromUtf8("draftList"))
        self.sentList.raise_()
        self.searchList.raise_()
        self.itemSortMode.raise_()
        self.itemSortOrder.raise_()
        self.deleteList.raise_()
        self.draftList.raise_()
        self.emaillist.raise_()
        self.showemail = QtGui.QGroupBox(self.centralWidget)
        self.showemail.setGeometry(QtCore.QRect(459, 50, 611, 540))
        self.showemail.setStyleSheet(_fromUtf8("#showemail{background-color: white;}\n"
""))
        self.showemail.setTitle(_fromUtf8(""))
        self.showemail.setObjectName(_fromUtf8("showemail"))
        self.emailShow = QtWebKit.QWebView(self.showemail)
        self.emailShow.setGeometry(QtCore.QRect(0, 122, 611, 421))
        self.emailShow.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.emailShow.setUrl(QtCore.QUrl(_fromUtf8("qrc:/souce/index.html")))
        self.emailShow.setObjectName(_fromUtf8("emailShow"))
        self.contInfoTop = QtGui.QGroupBox(self.showemail)
        self.contInfoTop.setGeometry(QtCore.QRect(0, 50, 611, 80))
        self.contInfoTop.setStyleSheet(_fromUtf8("background-color:white;\n"
"font: 14px \"微软雅黑\";\n"
"border:none;"))
        self.contInfoTop.setTitle(_fromUtf8(""))
        self.contInfoTop.setObjectName(_fromUtf8("contInfoTop"))
        self.contLogo = QtGui.QLabel(self.contInfoTop)
        self.contLogo.setGeometry(QtCore.QRect(10, 20, 41, 41))
        self.contLogo.setStyleSheet(_fromUtf8("border-image: url(:/souce/souce/登录.png);"))
        self.contLogo.setText(_fromUtf8(""))
        self.contLogo.setObjectName(_fromUtf8("contLogo"))
        self.contName = QtGui.QLabel(self.contInfoTop)
        self.contName.setGeometry(QtCore.QRect(120, 20, 161, 20))
        self.contName.setStyleSheet(_fromUtf8(""))
        self.contName.setText(_fromUtf8(""))
        self.contName.setObjectName(_fromUtf8("contName"))
        self.contEmail = QtGui.QLabel(self.contInfoTop)
        self.contEmail.setGeometry(QtCore.QRect(330, 20, 271, 20))
        self.contEmail.setStyleSheet(_fromUtf8(""))
        self.contEmail.setText(_fromUtf8(""))
        self.contEmail.setObjectName(_fromUtf8("contEmail"))
        self.contEmailTime = QtGui.QLabel(self.contInfoTop)
        self.contEmailTime.setGeometry(QtCore.QRect(120, 50, 141, 20))
        self.contEmailTime.setStyleSheet(_fromUtf8(""))
        self.contEmailTime.setText(_fromUtf8(""))
        self.contEmailTime.setObjectName(_fromUtf8("contEmailTime"))
        self.contEmailSubject = QtGui.QLabel(self.contInfoTop)
        self.contEmailSubject.setGeometry(QtCore.QRect(330, 50, 281, 20))
        self.contEmailSubject.setStyleSheet(_fromUtf8(""))
        self.contEmailSubject.setText(_fromUtf8(""))
        self.contEmailSubject.setObjectName(_fromUtf8("contEmailSubject"))
        self.label = QtGui.QLabel(self.contInfoTop)
        self.label.setGeometry(QtCore.QRect(63, 20, 51, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.contInfoTop)
        self.label_2.setGeometry(QtCore.QRect(60, 50, 51, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.contInfoTop)
        self.label_3.setGeometry(QtCore.QRect(280, 20, 41, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.contInfoTop)
        self.label_4.setGeometry(QtCore.QRect(280, 50, 41, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.attachList = QtGui.QListWidget(self.showemail)
        self.attachList.setGeometry(QtCore.QRect(0, 431, 601, 101))
        self.attachList.setStyleSheet(_fromUtf8("#attachList{\n"
"background-color: rgb(242,242,242);\n"
"border:none;\n"
"}\n"
"#attachList::Item{\n"
"height:35px;\n"
"width:100px;\n"
"}\n"
"#attachList::Item:hover{\n"
"background-color: rgb(41, 189, 139);\n"
"}"))
        self.attachList.setFlow(QtGui.QListView.TopToBottom)
        self.attachList.setObjectName(_fromUtf8("attachList"))
        self.emailBtnBox = QtGui.QGroupBox(self.showemail)
        self.emailBtnBox.setGeometry(QtCore.QRect(0, 0, 611, 51))
        self.emailBtnBox.setStyleSheet(_fromUtf8("#emailBtnBox{\n"
"background-color: rgb(242,242,242);\n"
"border:none;\n"
"}\n"
"QPushButton{\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(232,232,232);\n"
"}"))
        self.emailBtnBox.setTitle(_fromUtf8(""))
        self.emailBtnBox.setObjectName(_fromUtf8("emailBtnBox"))
        self.mainReply = QtGui.QPushButton(self.emailBtnBox)
        self.mainReply.setGeometry(QtCore.QRect(0, 0, 80, 51))
        self.mainReply.setStyleSheet(_fromUtf8(""))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/souce/souce/发送.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mainReply.setIcon(icon10)
        self.mainReply.setObjectName(_fromUtf8("mainReply"))
        self.mainForward = QtGui.QPushButton(self.emailBtnBox)
        self.mainForward.setGeometry(QtCore.QRect(78, 0, 80, 51))
        self.mainForward.setStyleSheet(_fromUtf8(""))
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/souce/souce/转发.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mainForward.setIcon(icon11)
        self.mainForward.setObjectName(_fromUtf8("mainForward"))
        self.delEmail = QtGui.QPushButton(self.emailBtnBox)
        self.delEmail.setGeometry(QtCore.QRect(245, 0, 80, 51))
        self.delEmail.setStyleSheet(_fromUtf8(""))
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/souce/souce/关闭1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delEmail.setIcon(icon12)
        self.delEmail.setObjectName(_fromUtf8("delEmail"))
        self.restoreEmail = QtGui.QPushButton(self.emailBtnBox)
        self.restoreEmail.setGeometry(QtCore.QRect(245, 0, 80, 51))
        self.restoreEmail.setStyleSheet(_fromUtf8(""))
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8(":/souce/souce/还原.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.restoreEmail.setIcon(icon13)
        self.restoreEmail.setObjectName(_fromUtf8("restoreEmail"))
        self.mainAttach = QtGui.QPushButton(self.emailBtnBox)
        self.mainAttach.setGeometry(QtCore.QRect(156, 0, 91, 51))
        self.mainAttach.setStyleSheet(_fromUtf8(""))
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8(":/souce/souce/附件.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mainAttach.setIcon(icon14)
        self.mainAttach.setObjectName(_fromUtf8("mainAttach"))
        self.mainclose = QtGui.QPushButton(self.centralWidget)
        self.mainclose.setGeometry(QtCore.QRect(1030, 15, 20, 20))
        self.mainclose.setStyleSheet(_fromUtf8("#mainclose{\n"
"    background-color:tomato;\n"
"    border-radius:10px;}\n"
"#mainclose:hover{border-image: url(:/souce/souce/关闭1.png);}\n"
""))
        self.mainclose.setText(_fromUtf8(""))
        self.mainclose.setObjectName(_fromUtf8("mainclose"))
        self.mainmin = QtGui.QPushButton(self.centralWidget)
        self.mainmin.setGeometry(QtCore.QRect(1000, 15, 20, 20))
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
        self.topWidget = QtGui.QWidget(self.centralWidget)
        self.topWidget.setGeometry(QtCore.QRect(200, 0, 871, 51))
        self.topWidget.setStyleSheet(_fromUtf8(""))
        self.topWidget.setObjectName(_fromUtf8("topWidget"))
        self.mainSearch = QtGui.QPushButton(self.topWidget)
        self.mainSearch.setGeometry(QtCore.QRect(0, 10, 30, 30))
        self.mainSearch.setStyleSheet(_fromUtf8("#mainSearch{\n"
"    border:none;\n"
"    border-radius:15px;\n"
"}\n"
"#mainSearch:hover{\n"
"    background-color:rgb(41,189,139);\n"
"}"))
        self.mainSearch.setText(_fromUtf8(""))
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(_fromUtf8(":/souce/souce/搜索_白.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mainSearch.setIcon(icon15)
        self.mainSearch.setObjectName(_fromUtf8("mainSearch"))
        self.searchlineEdit = QtGui.QLineEdit(self.topWidget)
        self.searchlineEdit.setGeometry(QtCore.QRect(36, 9, 221, 30))
        self.searchlineEdit.setStyleSheet(_fromUtf8("#searchlineEdit{\n"
"background-color: rgb(213, 213, 213);\n"
"border-radius:15px;\n"
"}\n"
"#searchlineEdit:hover{\n"
"background-color:white;\n"
"}"))
        self.searchlineEdit.setText(_fromUtf8(""))
        self.searchlineEdit.setObjectName(_fromUtf8("searchlineEdit"))
        self.searchMode = QtGui.QComboBox(self.topWidget)
        self.searchMode.setGeometry(QtCore.QRect(269, 10, 91, 31))
        self.searchMode.setStyleSheet(_fromUtf8(""))
        self.searchMode.setObjectName(_fromUtf8("searchMode"))
        self.searchMode.addItem(_fromUtf8(""))
        self.searchMode.addItem(_fromUtf8(""))
        self.searchMode.addItem(_fromUtf8(""))
        self.searchMode.addItem(_fromUtf8(""))
        self.searchMode.addItem(_fromUtf8(""))
        self.topWidget.raise_()
        self.leftWidget.raise_()
        self.receivedletter.raise_()
        self.showemail.raise_()
        self.mainclose.raise_()
        self.mainmin.raise_()
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.emaillist.setCurrentRow(-1)
        self.sentList.setCurrentRow(-1)
        self.searchList.setCurrentRow(-1)
        self.deleteList.setCurrentRow(-1)
        self.draftList.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "XYZ Mail", None))
        self.about.setToolTip(_translate("MainWindow", "关于", None))
        self.about.setWhatsThis(_translate("MainWindow", "关于", None))
        self.addressbook.setToolTip(_translate("MainWindow", "通讯录", None))
        self.addressbook.setWhatsThis(_translate("MainWindow", "通讯录", None))
        self.calender.setToolTip(_translate("MainWindow", "日历", None))
        self.mainwriteletter.setText(_translate("MainWindow", "写信", None))
        self.mainreceiveletter.setText(_translate("MainWindow", "收信", None))
        self.mainlogin.setText(_translate("MainWindow", "登录", None))
        self.sentBox.setText(_translate("MainWindow", "发件箱", None))
        self.receivedBox.setText(_translate("MainWindow", "收件箱", None))
        self.deleteBox.setText(_translate("MainWindow", "垃圾箱", None))
        self.draftBox.setText(_translate("MainWindow", "草稿箱", None))
        self.emaillist.setSortingEnabled(True)
        self.sentList.setSortingEnabled(True)
        self.searchList.setSortingEnabled(True)
        self.itemSortMode.setItemText(0, _translate("MainWindow", "按时间排序", None))
        self.itemSortMode.setItemText(1, _translate("MainWindow", "按主题排序", None))
        self.itemSortMode.setItemText(2, _translate("MainWindow", "按联系人排序", None))
        self.itemSortOrder.setItemText(0, _translate("MainWindow", "升序", None))
        self.itemSortOrder.setItemText(1, _translate("MainWindow", "降序", None))
        self.deleteList.setSortingEnabled(True)
        self.draftList.setSortingEnabled(True)
        self.label.setText(_translate("MainWindow", "用户名", None))
        self.label_2.setText(_translate("MainWindow", "时    间", None))
        self.label_3.setText(_translate("MainWindow", "邮  箱", None))
        self.label_4.setText(_translate("MainWindow", "主  题", None))
        self.attachList.setSortingEnabled(True)
        self.mainReply.setText(_translate("MainWindow", "回复", None))
        self.mainForward.setText(_translate("MainWindow", "转发", None))
        self.delEmail.setText(_translate("MainWindow", "删除", None))
        self.restoreEmail.setText(_translate("MainWindow", "还原", None))
        self.mainAttach.setText(_translate("MainWindow", "查看附件", None))
        self.searchlineEdit.setPlaceholderText(_translate("MainWindow", "搜索邮件信息", None))
        self.searchMode.setItemText(0, _translate("MainWindow", "请选择", None))
        self.searchMode.setItemText(1, _translate("MainWindow", "主题", None))
        self.searchMode.setItemText(2, _translate("MainWindow", "时间", None))
        self.searchMode.setItemText(3, _translate("MainWindow", "联系人", None))
        self.searchMode.setItemText(4, _translate("MainWindow", "邮件内容", None))

from PyQt4 import QtWebKit
import avatars_rc
import souce_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

