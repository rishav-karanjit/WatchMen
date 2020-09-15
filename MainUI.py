from PyQt5 import QtWidgets, uic
import sys

from AddProduct import AddProductUI
class MainUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        self.initUI()

    def initUI(self): 
        uic.loadUi('./UI/Main.ui', self) 
        
        self.button_AddP = self.findChild(QtWidgets.QPushButton, 'AddProduct')
        self.button_PList = self.findChild(QtWidgets.QPushButton, 'ProductLists')
        self.button_DelP = self.findChild(QtWidgets.QPushButton, 'DeleteProduct')
        self.button_ChgF = self.findChild(QtWidgets.QPushButton, 'ChangeFace')
        
        self.button_AddP.clicked.connect(self.AddP)
        self.show()

    def AddP(self):
        self.dialog=AddProductUI()
        self.close()