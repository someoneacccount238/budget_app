# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from signup import Ui_Form4

from main import Ui_MainWindow
from PyQt6.QtSql import QSqlDatabase, QSqlQuery
import os
import time
import pyodbc
import pandas as pd


class Ui_Form(object):
    def openWindow_main(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openWindow_signup(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form4()
        self.ui.setupUi(self.window)
        self.window.show()

    def checkCredentials(self):
        DRIVER_NAME = 'SQL SERVER'
        SERVER_NAME = r'(localdb)\MSSQLLocalDB'
        DATABASE_NAME = 'DemoDB'
        USERNAME = r'DESKTOP-3EJ3O6V\Admin'
        PASSWORD = ''

        
        email = self.lineEdit.text()
        password = self.lineEdit_2.text()

        connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={
            SERVER_NAME};DATABASE={DATABASE_NAME}'
        conn = pyodbc.connect(connectionString)

        print(f'conn {conn}')

        cur = conn.cursor()
        db_cmd = "SELECT * FROM [DemoDB].[dbo].[User] WHERE Email=?"
        
        res = cur.execute(db_cmd,email)
 
        for r in res:
            print (r[2])

        conn.commit()
        cur.close()
        conn.close()
       
        if r[2].strip()== password:
            time.sleep(1)
            self.openWindow_main()
        else:
            print('Password isnt correct')

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(120, 60, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 120, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setPlaceholderText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_4 = QtWidgets.QPushButton(
            parent=Form, clicked=self.checkCredentials)
        self.pushButton_4.setGeometry(QtCore.QRect(150, 190, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_5 = QtWidgets.QLabel(parent=Form)
        self.label_5.setGeometry(QtCore.QRect(30, 20, 591, 101))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=Form)
        self.label_6.setGeometry(QtCore.QRect(30, 80, 591, 101))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButton_5 = QtWidgets.QPushButton(
            parent=Form,   clicked=lambda: self.openWindow_signup())
        self.pushButton_5.setGeometry(QtCore.QRect(90, 240, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_4.setText(_translate("Form", "Login"))
        self.label_5.setText(_translate("Form", "Email:"))
        self.label_6.setText(_translate("Form", "Password:"))
        self.pushButton_5.setText(_translate(
            "Form", "Don\'t have an account? Sign up"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
