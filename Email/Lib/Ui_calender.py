# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\14356\Desktop\XYZMail\Libs\calender.ui'
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

class Ui_calenderDialog(object):
    def setupUi(self, calenderDialog):
        calenderDialog.setObjectName(_fromUtf8("calenderDialog"))
        calenderDialog.resize(400, 440)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(calenderDialog.sizePolicy().hasHeightForWidth())
        calenderDialog.setSizePolicy(sizePolicy)
        calenderDialog.setMinimumSize(QtCore.QSize(400, 440))
        calenderDialog.setMaximumSize(QtCore.QSize(400, 440))
        calenderDialog.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        calenderDialog.setStyleSheet(_fromUtf8("#calenderDialog{background-color:white;}\n"
"\n"
"#calenderclose{border-radius:15px;border:none;background-color: rgb(0,120,215);}\n"
"\n"
"#calenderclose:hover{background-color: #ccc;}"))
        calenderDialog.setSizeGripEnabled(True)
        self.calendarWidget = QtGui.QCalendarWidget(calenderDialog)
        self.calendarWidget.setGeometry(QtCore.QRect(0, 40, 400, 400))
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        self.widget = QtGui.QWidget(calenderDialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 401, 40))
        self.widget.setStyleSheet(_fromUtf8("background-color: rgb(66, 74, 89);"))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.calenderMin = QtGui.QPushButton(self.widget)
        self.calenderMin.setGeometry(QtCore.QRect(340, 10, 20, 20))
        self.calenderMin.setToolTip(_fromUtf8(""))
        self.calenderMin.setStyleSheet(_fromUtf8("#calenderMin{\n"
"background-color:rgb(255,224,81);\n"
"    border-radius:10px;}\n"
"#calenderMin:hover{\n"
"border-image: url(:/souce/souce/最小化.png);\n"
"}\n"
""))
        self.calenderMin.setText(_fromUtf8(""))
        self.calenderMin.setObjectName(_fromUtf8("calenderMin"))
        self.calenderClose = QtGui.QPushButton(self.widget)
        self.calenderClose.setGeometry(QtCore.QRect(370, 10, 20, 20))
        self.calenderClose.setStyleSheet(_fromUtf8("#calenderClose{\n"
"    background-color:tomato;\n"
"    border-radius:10px;}\n"
"#calenderClose:hover{border-image: url(:/souce/souce/关闭1.png);}\n"
""))
        self.calenderClose.setText(_fromUtf8(""))
        self.calenderClose.setObjectName(_fromUtf8("calenderClose"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(140, 0, 101, 41))
        self.label.setStyleSheet(_fromUtf8("color:white;"))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(calenderDialog)
        QtCore.QMetaObject.connectSlotsByName(calenderDialog)

    def retranslateUi(self, calenderDialog):
        calenderDialog.setWindowTitle(_translate("calenderDialog", "Calender", None))
        self.label.setText(_translate("calenderDialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">日    历</span></p></body></html>", None))

import souce_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    calenderDialog = QtGui.QDialog()
    ui = Ui_calenderDialog()
    ui.setupUi(calenderDialog)
    calenderDialog.show()
    sys.exit(app.exec_())

