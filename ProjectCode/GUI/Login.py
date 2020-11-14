# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from MainPage import Ui_MainWindow

class Ui_LoginWindow(object):
    def login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if username == "2013147051":
            self.window = QtWidgets.QMainWindow()
            self.next = Ui_MainWindow()
            self.next.setupUi(self.window,username)
            MainWindow.hide()
            self.window.show()

            
            #print(self.next.StudentID)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 725)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(300, 540, 481, 40))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(300, 610, 481, 40))
        self.lineEdit_2.setObjectName("lineEdit_2")


        self.photo = QtWidgets.QLabel (self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(186, 30, 1028, 445))
        self.photo.setObjectName("graphicsView")
        self.pixmap = QtGui.QPixmap('yonsei.png')
        self.photo.setPixmap(self.pixmap)
        #self.photo.resize(self.pixmap.width(),self.pixmap.height())

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(820, 540, 141, 131))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.login)
        self.lineEdit_2.returnPressed.connect(self.login)
        self.lineEdit.returnPressed.connect(self.login)


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 520, 81, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 590, 81, 16))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1400, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.label.setText(_translate("MainWindow", "StudentID"))
        self.label_2.setText(_translate("MainWindow", "Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyle('window')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
