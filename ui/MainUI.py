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

    def getDistance(self):
        byteList = self.bus.read_i2c_block_data(self.address,0,6)
        distanceStr = ""
        for a in range(2):
            id = byteList[a * 3]
            distance = byteList[a * 3 + 1] * 256 + byteList[a * 3 + 2]
            distanceStr += str(id) + ":" + str(distance) + " "
        print (distanceStr)
    
    @pyqtSlot()
    def on_btnOilStop_clicked(self):
        self.bus.write_byte(self.address,22)
    @pyqtSlot()
    def on_btnOilStart_clicked(self):
        self.bus.write_byte(self.address,21)
        self.getDistance()
