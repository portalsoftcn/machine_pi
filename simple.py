import sys
from ui import MainUI
from PyQt5.QtWidgets import QApplication
if __name__== '__main__':
    app = QApplication(sys.argv)
    dlg = MainUI.MainWindow()
    dlg.show()
    sys.exit(app.exec_())
