#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import mainwin
import smbus2
import requests
import Adafruit_CharLCD
import socket
import time
import numpy
# 首先，咱们从刚刚源文件中将主窗体继承下来.就是修改过name属性的主窗体咯。
class MainWindow(mainwin.MainWin):
    # 咱们给个初始化函数，将文本框初始填有‘主窗口测试’几个字
    # 不能直接覆盖原有__ini__方法，这样会导致窗体启动失败。咱们新建一个，然后再调用
    def init_main_window(self):
        self.text_main.SetValue('主窗口测试')
    # 将点击按钮清空文本框的,功能写成函数
    def main_button_click(self, event):
        self.text_main.Clear()




if __name__ == '__main__':
    app = wx.App()
    # None表示的是此窗口没有上级父窗体。如果有，就直接在父窗体代码调用的时候填入‘self’就好了。
    main_win = mainwin.MainWin(None)
    main_win.Show()
    app.MainLoop()


    # import wx
    bus = smbus2.SMBus(1)
    address = 0x04

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

    while True:
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
            lcd.clear()
            lcd.message("IP:" + ip_address + "\nDo Command:" + cmd)
            bus.write_byte(0x04, int(cmd))



