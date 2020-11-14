# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CheckReq.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

class Ui_CheckReqWindow(object):
    def setupUi(self, CheckReqWindow,area,StudentID):
        self.area = area
        self.StudentID = StudentID
        CheckReqWindow.setObjectName("CheckReqWindow")
        CheckReqWindow.resize(776, 600)
        self.centralwidget = QtWidgets.QWidget(CheckReqWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 90, 731, 441))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(20)
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers )


        db = pymysql.connect(host='127.0.0.1',database= 'mydb', port=3306,user='root',passwd='1234',charset='utf8mb4')
        cursor = db.cursor()
        sql = """
                SELECT S.SubjectID, S.SubjectName, S.Credit, F.Grade
                FROM SUBJECTS S, FINISHEDSUBJECT F
                WHERE 
                S.SubjectID = F.SUBJECT_SubjectID AND
                S.OpenYear = F.SUBJECT_OpenYear AND
                S.OpenSem = F.SUBJECT_OpenSem AND
                S.G2 = F.SUBJECT_G2 AND
                S.G3 = F.SUBJECT_G3 AND
                F.STUDENT_StudentID = {} AND
                F.SUBJECT_G3 = '{}';""".format(self.StudentID,self.area)

        #print(sql)
        cursor.execute(sql)
        rtn = cursor.fetchall()
        db.close()

        for row_number, row_data in enumerate(rtn):
            self.tableWidget.insertRow(row_number)
            for colum_number, data in enumerate (row_data):
                self.tableWidget.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))
        self.tableWidget.setHorizontalHeaderLabels(["학정번호", "과목명","학점","성적"])




        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 50, 171, 31))
        self.label.setObjectName("label")
        CheckReqWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CheckReqWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 776, 26))
        self.menubar.setObjectName("menubar")
        CheckReqWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CheckReqWindow)
        self.statusbar.setObjectName("statusbar")
        CheckReqWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CheckReqWindow)
        QtCore.QMetaObject.connectSlotsByName(CheckReqWindow)

    def retranslateUi(self, CheckReqWindow):
        _translate = QtCore.QCoreApplication.translate
        CheckReqWindow.setWindowTitle(_translate("CheckReqWindow", "MainWindow"))
        self.label.setText(_translate("CheckReqWindow", "{} 수강 과목".format(self.area)))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CheckReqWindow = QtWidgets.QMainWindow()
    ui = Ui_CheckReqWindow()
    ui.setupUi(CheckReqWindow)
    CheckReqWindow.show()
    sys.exit(app.exec_())
