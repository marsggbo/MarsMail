# -*- coding: utf-8 -*-

"""
Module implementing contacts.
"""

from PyQt4 import QtCore,  QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QDialog

from Ui_contacts import Ui_contacts
from writemail import WriteEmailDialog
from DealJsonFile import GetJsonInfo

class contacts(QDialog, Ui_contacts):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        super(contacts, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
        self.emailInfo = GetJsonInfo('conf.json')
        self.contacts = GetJsonInfo('contacts.json')
        self.contUserMail.setText(self.emailInfo["email"])

        # 绑定QListWidget
        self.connect(self.contactsList, SIGNAL('itemClicked(QListWidgetItem *)'), self.itemClicked)

        for item in self.contacts:
            my_contact = self.contacts[item]['name'] + '\n' + self.contacts[item]['fromAddr']
            self.contactsList.addItem(my_contact)
    
    @pyqtSlot()
    def itemClicked(self):
        my_currentItem = self.contactsList.currentItem()
        my_text = my_currentItem.text().split('\n')
        self.contName.setText(my_text[0])
        self.contEmail.setText(my_text[1])
        print(self.contName.text())


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            QApplication.postEvent(self, QEvent(174))
            event.accept()
 
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    @pyqtSlot()
    def on_contClose_clicked(self):
        self.close()
    
    @pyqtSlot()
    def on_contMin_clicked(self):
        self.showMinimized()
    
    @pyqtSlot()
    def on_contWriteLetter_clicked(self):
        my_writemail  = WriteEmailDialog()
        my_writemail.exec_()
    
    @pyqtSlot()
    def on_delContact_clicked(self):
        pass
    
    @pyqtSlot()
    def on_contCancel_clicked(self):
        pass
    
    @pyqtSlot()
    def on_contSave_clicked(self):
        pass

# if __name__ == '__main__':
     
#     import sys
#     app = QApplication(sys.argv)
#     aboutus = contacts()
#     aboutus.show()
#     sys.exit(app.exec_())
