# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\gitwork\machine_pi\ui\MainWin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 418)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 781, 101))
        self.groupBox.setObjectName("groupBox")
        self.lblPlatform = QtWidgets.QLabel(self.groupBox)
        self.lblPlatform.setGeometry(QtCore.QRect(90, 30, 54, 12))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lblPlatform.setFont(font)
        self.lblPlatform.setObjectName("lblPlatform")
        self.lblBeam = QtWidgets.QLabel(self.groupBox)
        self.lblBeam.setGeometry(QtCore.QRect(90, 60, 54, 12))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lblBeam.setFont(font)
        self.lblBeam.setObjectName("lblBeam")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 54, 12))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 54, 12))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 130, 781, 271))
        self.groupBox_2.setObjectName("groupBox_2")
        self.btnOilStop = QtWidgets.QPushButton(self.groupBox_2)
        self.btnOilStop.setGeometry(QtCore.QRect(150, 30, 75, 23))
        self.btnOilStop.setObjectName("btnOilStop")
        self.btnOilStart = QtWidgets.QPushButton(self.groupBox_2)
        self.btnOilStart.setGeometry(QtCore.QRect(40, 30, 75, 23))
        self.btnOilStart.setObjectName("btnOilStart")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "磨机辅助控制系统"))
        self.groupBox.setTitle(_translate("MainWindow", "状态显示"))
        self.lblPlatform.setText(_translate("MainWindow", "111cm"))
        self.lblBeam.setText(_translate("MainWindow", "50cm"))
        self.label.setText(_translate("MainWindow", "平台移动:"))
        self.label_2.setText(_translate("MainWindow", "横梁移动:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "控制"))
        self.btnOilStop.setText(_translate("MainWindow", "油泵停止"))
        self.btnOilStart.setText(_translate("MainWindow", "油泵启动"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

