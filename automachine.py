import sys
import smbus2
import requests
import Adafruit_CharLCD
import socket
import time
import ui.MainUI
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    """
    app = QApplication(sys.argv)
    desktop = QApplication.desktop();
    screenRect = desktop.screenGeometry()
    screenW = screenRect.width()
    screenH = screenRect.height()
    w = QWidget()
    w.resize(screenW, screenH)
    w.setWindowTitle('磨机辅助控制系统')
    w.show()
    sys.exit(app.exec_())
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('www.baidu.com', 0))
        ip = s.getsockname()[0]
    except:
        ip = "x.x.x.x"
    finally:
        s.close()

    ip_address = ip
    lcd = Adafruit_CharLCD.Adafruit_CharLCD()
    lcd.clear()
    lcd.message("IP:" + ip_address + "\nReady Do Command")
    """
    
    bus = smbus2.SMBus(1)
    address = 0x04
    while True:
        print ("distance is:")
        time.sleep(0.2)
        byteList = bus.read_i2c_block_data(address, 0, 6)
        distanceStr = ""
        for a in range(2):
            id = byteList[a * 3]
            distance = byteList[a * 3 + 1] * 256 + byteList[a * 3 + 2]
            distanceStr += str(id) + ":" + str(distance) + " "
        print (distanceStr)
        ret = requests.get("http://erp.zzhcdr.com/getcmd.jsp")
        cmd = ret.text.strip()
        if cmd != '':
            #lcd.clear()
            #lcd.message("IP:" + ip_address + "\nDo Command:" + cmd)
            bus.write_byte(0x04, int(cmd))
