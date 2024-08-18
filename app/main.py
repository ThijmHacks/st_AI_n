#General Imports
import sys
import requests

#The Window Maker
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                            QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt
from PyQt5 import  QtGui

#Custom Import Package
from st_AI_n.responses import response

class StainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("st_AI_n")
        self.setWindowIcon(QtGui.QIcon('BotLogo.ico'))

if __name__ == "__main__":
        app = QApplication(sys.argv)
        st_AI_n__app = StainApp()
        st_AI_n__app.show()
        sys.exit(app.exec_())
