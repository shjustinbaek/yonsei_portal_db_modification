# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SubjectInfo.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

class Ui_SubjectInfoWindow(object):
    def setupUi(self, SubjectInfoWindow,dis):
        self.dis = dis
        SubjectInfoWindow.setObjectName("SubjectInfoWindow")
        SubjectInfoWindow.resize(1000, 728)
        self.centralwidget = QtWidgets.QWidget(SubjectInfoWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(540, 120, 391, 491))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(50, 130, 211, 51))

        self.listWidget.setObjectName("listWidget")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(280, 130, 211, 51))
        self.listWidget_2.setObjectName("listWidget_2")
        self.listWidget_3 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_3.setGeometry(QtCore.QRect(50, 220, 211, 51))
        self.listWidget_3.setObjectName("listWidget_3")
        self.listWidget_4 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_4.setGeometry(QtCore.QRect(280, 220, 211, 51))
        self.listWidget_4.setObjectName("listWidget_4")
        SubjectInfoWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SubjectInfoWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 26))
        self.menubar.setObjectName("menubar")
        SubjectInfoWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SubjectInfoWindow)
        self.statusbar.setObjectName("statusbar")
        SubjectInfoWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SubjectInfoWindow)
        QtCore.QMetaObject.connectSlotsByName(SubjectInfoWindow)

    def retranslateUi(self, SubjectInfoWindow):
        _translate = QtCore.QCoreApplication.translate
        SubjectInfoWindow.setWindowTitle(_translate("SubjectInfoWindow", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SubjectInfoWindow = QtWidgets.QMainWindow()
    ui = Ui_SubjectInfoWindow()
    ui.setupUi(SubjectInfoWindow)
    SubjectInfoWindow.show()
    sys.exit(app.exec_())
