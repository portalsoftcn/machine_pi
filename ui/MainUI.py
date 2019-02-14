# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import smbus2
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from .Ui_MainWin import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    address = 0x04
    bus = None
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        bus = smbus2.SMBus(1)
        
    
    @pyqtSlot()
    def on_btnOilStop_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.lblPlatform.setText('油泵停止')
    
    @pyqtSlot()
    def on_btnOilStart_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.lblPlatform.setText('油泵启动')
