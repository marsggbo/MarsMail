# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\14356\Desktop\XYZMail\Libs/about.ui'
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

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName(_fromUtf8("About"))
        About.resize(960, 582)
        self.centralWidget = QtGui.QWidget(About)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(0, 40, 960, 540))
        self.label.setStyleSheet(_fromUtf8("border-image: url(:/souce/souce/关于.png);"))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.widget = QtGui.QWidget(self.centralWidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 960, 40))
        self.widget.setStyleSheet(_fromUtf8("background-color: rgb(34,36,59);\n"
"border:none;"))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(410, 0, 131, 41))
        self.label_2.setStyleSheet(_fromUtf8("font: 75 20px \"微软雅黑\";\n"
"font-weight:bold;\n"
"color:white;"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.aboutMin = QtGui.QPushButton(self.widget)
        self.aboutMin.setGeometry(QtCore.QRect(900, 10, 20, 20))
        self.aboutMin.setToolTip(_fromUtf8(""))
        self.aboutMin.setStyleSheet(_fromUtf8("#aboutMin{\n"
"background-color:rgb(255,224,81);\n"
"    border-radius:10px;}\n"
"#aboutMin:hover{\n"
"border-image: url(:/souce/souce/最小化.png);\n"
"}\n"
""))
        self.aboutMin.setText(_fromUtf8(""))
        self.aboutMin.setObjectName(_fromUtf8("aboutMin"))
        self.aboutClose = QtGui.QPushButton(self.widget)
        self.aboutClose.setGeometry(QtCore.QRect(930, 10, 20, 20))
        self.aboutClose.setStyleSheet(_fromUtf8("#aboutClose{\n"
"    background-color:tomato;\n"
"    border-radius:10px;}\n"
"#aboutClose:hover{border-image: url(:/souce/souce/关闭1.png);}\n"
""))
        self.aboutClose.setText(_fromUtf8(""))
        self.aboutClose.setObjectName(_fromUtf8("aboutClose"))
        self.widget.raise_()
        self.label.raise_()
        About.setCentralWidget(self.centralWidget)

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        About.setWindowTitle(_translate("About", "MainWindow", None))
        self.label_2.setText(_translate("About", "关   于", None))

import souce_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    About = QtGui.QMainWindow()
    ui = Ui_About()
    ui.setupUi(About)
    About.show()
    sys.exit(app.exec_())

