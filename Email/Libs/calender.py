# -*- coding: utf-8 -*-

"""
Module implementing calenderDialog.
"""

from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QDialog

from Ui_calender import Ui_calenderDialog
import sys

class calenderDialog(QDialog, Ui_calenderDialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(calenderDialog, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_calenderclose_clicked(self):
        self.close()
