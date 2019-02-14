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
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.address = 0x04
        self.bus = smbus2.SMBus(1)
    @pyqtSlot()
    def on_btnOilStop_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print(" stop ")
        self.bus.write_byte(self.address,22)
    @pyqtSlot()
    def on_btnOilStart_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.bus.write_byte(self.address,21)
