import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QLabel, QGridLayout, QSizePolicy
from PyQt6.QtCore import Qt

import os
import time
from PyQt6.QtSql import QSqlDatabase, QSqlQuery


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        label = QLabel('Main App', parent=self)


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.window_width, self.window_height = 600, 200
        self.setFixedSize(self.window_width, self.window_height)
        layout = QGridLayout()
        self.setLayout(layout)

        labels = {}
        self.lineEdits = {}

        labels['Username'] = QLabel('Username')
        labels['Password'] = QLabel('Password')
        labels['Username'].setSizePolicy(
            QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        labels['Password'].setSizePolicy(
            QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self.lineEdits['Username'] = QLineEdit()
        self.lineEdits['Password'] = QLineEdit()
        self.lineEdits['Username'].setFixedWidth(200);
        self.lineEdits['Password'].setFixedWidth(200);
        self.lineEdits['Password'].setEchoMode(QLineEdit.EchoMode.Password)

        layout.addWidget(labels['Username'], 0, 0, 1, 1)
        layout.addWidget(self.lineEdits['Username'], 0, 1, 1, 3)

        layout.addWidget(labels['Password'], 1, 0, 1, 1)
        layout.addWidget(self.lineEdits['Password'], 1, 1, 1, 3)

        button_login = QPushButton('&Log In', clicked=self.checkCredentials)
        layout.addWidget(button_login, 2,3,1,1)
        
        self.status = QLabel('')
        self.status.setStyleSheet('font-size: 25px; color:red;')
        layout.addWidget(self.status, 3,0,1,3)

        self.connectToDb()

    def connectToDb(self):
        db = QSqlDatabase.addDatabase('QODBC')
        db.setDatabaseName(f'DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={os.path.join(os.getcwd(), 'Users:accdb')}')

        if not db.open():
            self.status.setText('Connection failed')

    def checkCredentials(self):
        username= self.lineEdits['Username'].text()
        password= self.lineEdits['Password'].text()

        query = QSqlQuery()
        query.prepare('SELECT * FROM Users WHERE Username=:username')
        query.bindValue(':username',username)
        query.exec()

        if query.first():
            if query.value('Password')==password:
                time.sleep(1)
                self.myApp = MyApp()
                self.myApp.show()
                self.close()
            else:
                self.status.setText('Password is not correct')
        else:
            self.status.setText('Username is not found')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet('''
                    QWidget {
                  font-size:20px;}
    QLineEdit{
        height:30px; 
    } 
                  ''')

    window = LoginWindow()
    window.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing window...')
