from PyQt5 import QtWidgets, uic
#from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QGridLayout
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from openpyxl import load_workbook
from subprocess import call
from tkinter import messagebox
import serial

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Design/Main.ui', self)
        
        # Define any widgets for the main page
        self.pushButton = self.findChild(QtWidgets.QPushButton, 'pushButton')
        
        # Connect any signals from the widgets to the appropriate functions
        self.pushButton.clicked.connect(self.loadPage2)

        self.show() # Show the GUI

        
    def loadPage2(self):
        # Switch to the new page
        self.page2 = Page2()
        self.setCentralWidget(self.page2)

class Page2(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Design/Page2.ui', self)
        
        # Define any widgets for this page
        self.label = self.findChild(QtWidgets.QLabel, 'label')
        self.pushButton = self.findChild(QtWidgets.QPushButton, 'pushButton')
        
        # Connect any signals from the widgets to the appropriate functions
        self.pushButton.clicked.connect(self.doSomething)
        self.show() # Show the GUI

        
    def doSomething(self):
        # Define any functions for this page
        self.label.setText('Button clicked!')

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()