from PyQt6 import QtCore, QtGui, QtWidgets, uic
import time



class MyWindow(QtWidgets. QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('main.ui', self)
        budget_action = self.pushButton_4.clicked.connect(self.open_budget)




import sys
app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
    
app.exec()
