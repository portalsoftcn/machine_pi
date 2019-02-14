# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import smbus2
import threading
import time
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
        timer = threading.Timer(0.2,self.getDistance)
        timer.start()
    def getDistance(self):
        try:
            byteList = self.bus.read_i2c_block_data(self.address,0,6)
            distanceStr = ""
            for a in range(2):
                id = byteList[a * 3]
                distance = byteList[a * 3 + 1] * 256 + byteList[a * 3 + 2]
                distanceStr += str(id) + ":" + str(distance) + " "
            print (distanceStr)
        except OSError as e:
            print("bus read error",e)
                
        timer = threading.Timer(0.2,self.getDistance)
        timer.start()
        
    def doCommand(self,cmd):
        try:
            self.bus.write_byte(self.address,cmd)
        except OSError as e:
            print("bus write error",e)
            
    @pyqtSlot()
    def on_btnOilStop_clicked(self):
        self.doCommand(22)
    @pyqtSlot()
    def on_btnOilStart_clicked(self):
        self.doCommand(21)
        
