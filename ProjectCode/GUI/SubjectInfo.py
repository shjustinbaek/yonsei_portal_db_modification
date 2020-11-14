# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SubjectInfo.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
import seaborn as sns
import pandas as pd
import warnings
warnings.filterwarnings(action='ignore')



class Ui_SubjectInfoWindow(object):

    def setupUi(self, SubjectInfoWindow,dis):
        self.dis = dis
        #print(self.dis)
        SubjectInfoWindow.setObjectName("SubjectInfoWindow")
        SubjectInfoWindow.resize(1000, 728)
        self.centralwidget = QtWidgets.QWidget(SubjectInfoWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1000, 728))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.tableWidget_profinfo = QtWidgets.QTableWidget(self.tab)
        self.tableWidget_profinfo.setGeometry(QtCore.QRect(50, 40, 900, 131))
        self.tableWidget_profinfo.setObjectName("tableWidget_profinfo")
        self.tableWidget_profinfo.setColumnCount(5)
        self.tableWidget_profinfo.setRowCount(3)
        self.tableWidget_profinfo.setHorizontalHeaderLabels(["담당교수", "담당교수소속","연구실","연락처","e-mail"])
        header = self.tableWidget_profinfo.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)

        q = self.dis[0]
        w = self.dis[1]
        e = self.dis[2]
        r = self.dis[3]
        t = self.dis[4]
        # print(q)
        # print(w)
        db = pymysql.connect(host='127.0.0.1', database='mydb', port=3306, user='root', passwd='1234', charset='utf8mb4')
        cursor = db.cursor()
        sql1 = 'SELECT professor.ProfName, Department, OfficeNumber, Phone, Email FROM professor, subjects_professor'
        sql1 += '''
                      WHERE SUBJECT_OpenYear='{}' AND SUBJECT_OpenSem='{}'AND SUBJECT_G2='{}' AND SUBJECT_G3='{}' AND 
                      SUBJECT_SubjectID='{}' AND PROFESSOR.ProfName = SUBJECTS_PROFESSOR.PROFESSOR_ProfName AND 
                      PROFESSOR.Department = SUBJECTS_PROFESSOR.PROFESSOR_Department AND PROFESSOR.Email = SUBJECTS_PROFESSOR.PROFESSOR_Email;'''.format(q, w, e, r, t)
        # print(sql1)
        cursor.execute(sql1)
        rtn1 = cursor.fetchall()
        # print(rtn1)
        db.close()
        self.tableWidget_profinfo.setRowCount(0)
        for row_number1, row_data1 in enumerate(rtn1):
            self.tableWidget_profinfo.insertRow(row_number1)
            for colum_number1, data1 in enumerate(row_data1):
                self.tableWidget_profinfo.setItem(row_number1, colum_number1, QtWidgets.QTableWidgetItem(str(data1)))


        self.tableWidget_subjectinfo = QtWidgets.QTableWidget(self.tab)
        self.tableWidget_subjectinfo.setGeometry(QtCore.QRect(50, 220, 900, 451))
        self.tableWidget_subjectinfo.setObjectName("tableWidget_subjectinfo")
        self.tableWidget_subjectinfo.setColumnCount(1)
        self.tableWidget_subjectinfo.setRowCount(14)
        header = self.tableWidget_subjectinfo.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_subjectinfo.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

        db = pymysql.connect(host='127.0.0.1', database='mydb', port=3306, user='root', passwd='1234',
                             charset='utf8mb4')
        cursor = db.cursor()
        sql2 = 'SELECT  SubjectName, Credit, SubjectTime, SyllUploadDate, SyllLastUpdate, SubjectsFor, SubjectGoal, Prerequisite, SubjectMethod, SubjectGP, TextBook, InfoProf, InfoTA, EngSyll FROM subjects'
        sql2 += ''' 
            WHERE OpenYear='{}' AND OpenSem='{}'AND G2='{}' AND G3='{}' AND SubjectID='{}';'''.format(
            q, w, e, r, t)
        #print(sql2)
        cursor.execute(sql2)
        rtn2 = cursor.fetchall()
        #print(rtn2)
        db.close()
        self.tableWidget_subjectinfo.setRowCount(0)
        for i in range(14):
            self.tableWidget_subjectinfo.insertRow(i)
        for row_number2, row_data2 in enumerate(rtn2):
            for colum_number2, data2 in enumerate(row_data2):
                self.tableWidget_subjectinfo.setItem(colum_number2,row_number2, QtWidgets.QTableWidgetItem(str(data2)))
        self.tableWidget_subjectinfo.setVerticalHeaderLabels(["교과목명", "학점", "강의시간", "최초등록일", "최종수정일", "수강대상", "수업목표및개요", "선수과목", "강좌운영방식", "성적평가방법", "교재", "교수정보","조교정보","영문수업계획"])

        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(50, 10, 91, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(50, 190, 91, 16))
        self.label_6.setObjectName("label_6")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.tableWidget_syllabus = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_syllabus.setGeometry(QtCore.QRect(20, 50, 951, 610))
        self.tableWidget_syllabus.setObjectName("tableWidget_syllabus")
        self.tableWidget_syllabus.setColumnCount(5)
        self.tableWidget_syllabus.setRowCount(20)
        self.tableWidget_syllabus.setHorizontalHeaderLabels(["주", "기간", "수업내용", "교재범위,과제물", "비고"])
        header3 = self.tableWidget_syllabus.horizontalHeader()
        header3.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header3.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header3.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header3.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        header3.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_syllabus.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)        


        db = pymysql.connect(host='127.0.0.1', database='mydb', port=3306, user='root', passwd='1234',
                             charset='utf8mb4')
        cursor = db.cursor()
        sql3 = 'SELECT  Week, DatePeriod, Content, Event, Remarks from weeklysyllabus'
        sql3 += ''' 
                   WHERE SUBJECT_OpenYear='{}' AND SUBJECT_OpenSem='{}'AND SUBJECT_G2='{}' AND SUBJECT_G3='{}' AND SUBJECT_SubjectID='{}'
                   ORDER BY cast(Week as unsigned);'''.format(q, w, e, r, t)
        #print(sql3)
        cursor.execute(sql3)
        rtn3 = cursor.fetchall()
        #print(rtn3)
        db.close()
        self.tableWidget_syllabus.setRowCount(0)
        for row_number3, row_data3 in enumerate(rtn3):
            self.tableWidget_syllabus.insertRow(row_number3)
            for colum_number3, data3 in enumerate(row_data3):
                self.tableWidget_syllabus.setItem(row_number3, colum_number3, QtWidgets.QTableWidgetItem(str(data3)))



        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(20, 20, 64, 15))
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")



        #################### 마일리지
        sns.set(rc={'figure.figsize':(9,2.2)})
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(50, 50, 900, 350))
        self.label_3.setObjectName("label_3")

        db = pymysql.connect(host='127.0.0.1',database= 'mydb', port=3306,user='root',passwd='1234',charset='utf8mb4')
        cursor = db.cursor()
        sql =  """SELECT MileageBet, IfEnrolled, SUBJECT_OpenSem FROM APPLIEDSUBJECT WHERE SUBJECT_G2='{}' AND SUBJECT_G3='{}' AND 
                SUBJECT_SubjectID='{}';""".format(e, r, t)
        cursor.execute(sql)
        temp = list(cursor.fetchall())
        rtn = pd.DataFrame(temp,columns = ['A','B','C'])
        db.close()



        ax = sns.swarmplot(x="C", y="A", data=rtn)
        fig = ax.get_figure()
        fig.savefig("mileage.png")
        self.pixmap = QtGui.QPixmap("mileage.png")
        self.label_3.setPixmap(self.pixmap)


        self.mileage1 = QtWidgets.QLabel(self.tab_3)
        self.mileage1.setGeometry(QtCore.QRect(50, 50, 900, 250))
        self.mileage1.setObjectName("mileage1")

        self.mileagetable = QtWidgets.QTableWidget(self.tab_3)
        self.mileagetable.setGeometry(QtCore.QRect(50, 350, 900, 250))
        self.mileagetable.setObjectName("mileage2")
        self.mileagetable.setColumnCount(2)
        self.mileagetable.setRowCount(1000)
        self.tabWidget.addTab(self.tab_3, "")

        self.mileagetable.setRowCount(0)
        for row_number, row_data in enumerate(temp):
            self.mileagetable.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.mileagetable.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))
        self.mileagetable.setHorizontalHeaderLabels(["신청 마일리지", "성공 여부"])
        header = self.mileagetable.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)


        SubjectInfoWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(SubjectInfoWindow)
        self.statusbar.setObjectName("statusbar")
        SubjectInfoWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SubjectInfoWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SubjectInfoWindow)

    def retranslateUi(self, SubjectInfoWindow):
        _translate = QtCore.QCoreApplication.translate
        SubjectInfoWindow.setWindowTitle(_translate("SubjectInfoWindow", "MainWindow"))
        self.label_5.setText(_translate("SubjectInfoWindow", "교수님 정보"))
        self.label_6.setText(_translate("SubjectInfoWindow", "Subject Info"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("SubjectInfoWindow", "Basic Info"))
        self.label.setText(_translate("SubjectInfoWindow", "Syllabus"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("SubjectInfoWindow", "Syllabus"))
        #self.mileage1.setText(_translate("SubjectInfoWindow", "TextLabel"))
        #self.label_3.setText(_translate("SubjectInfoWindow", "TextLabel"))
        #self.mileagetable.setText(_translate("SubjectInfoWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("SubjectInfoWindow", "Mileage History"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SubjectInfoWindow = QtWidgets.QMainWindow()
    ui = Ui_SubjectInfoWindow()
    ui.setupUi(SubjectInfoWindow)
    SubjectInfoWindow.show()
    sys.exit(app.exec_())