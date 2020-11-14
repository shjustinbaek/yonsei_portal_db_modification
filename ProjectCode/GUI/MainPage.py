# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainPage.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
from SubjectInfo import Ui_SubjectInfoWindow
from CheckReq import Ui_CheckReqWindow




class Ui_MainWindow(object):
    def check_gradreq(self):
        r = self.gradreq.currentRow()
        area = self.gradreq.item(r,0).text()
        self.window = QtWidgets.QMainWindow()
        self.next = Ui_CheckReqWindow()
        self.next.setupUi(self.window,area,self.StudentID)
        #MainWindow.hide()
        self.window.show()
        

    def subject_info(self):
        r = self.tableWidget.currentRow()
        dis = [self.tableWidget.item(r,0).text(), self.tableWidget.item(r,1).text(), self.tableWidget.item(r,3).text(), self.tableWidget.item(r,4).text(), self.tableWidget.item(r,5).text()]
        self.window = QtWidgets.QMainWindow()
        self.next = Ui_SubjectInfoWindow()
        self.next.setupUi(self.window,dis)
        #MainWindow.hide()
        self.window.show()
        #print(dis0,dis1,dis2,dis3,dis4)

    def find_subject(self):
        db = pymysql.connect(host='127.0.0.1',database= 'mydb', port=3306,user='root',passwd='1234',charset='utf8mb4')
        cursor = db.cursor()
        sql = 'SELECT OpenYear,OpenSem,G1,G2,G3,SubjectID,SubjectName,Credit,SubjectTime,FullCapa SubjectName FROM SUBJECTS '
        semester = str(self.comboBox_5.currentText())
        gu2 = str(self.comboBox_2.currentText())
        gu3 = str(self.comboBox_3.currentText())
        sql += "WHERE OpenSem = '{}' ".format(semester) #AND G2 = '{}' AND G3 = '{}'".format(semester,gu2,gu3)
        if gu2 != '전체':
            sql += " AND G2 = '{}' ".format(gu2)
            if gu3 != '전체':
                sql += " AND G3 = '{}' ".format(gu3)
        #print(sql)

        if self.lineEdit.text() != "":
            sql = sql + " AND SubjectID LIKE '%{}%' ".format(self.lineEdit.text()) + "UNION ALL " + sql + " AND SubjectName LIKE '%{}%' ".format(self.lineEdit.text())
        sql += ';'

        #print(sql)
        cursor.execute(sql)
        rtn = cursor.fetchall()
        #print(rtn)
        db.close()
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(rtn):
            self.tableWidget.insertRow(row_number)
            for colum_number, data in enumerate (row_data):
                self.tableWidget.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))
        self.tableWidget.setHorizontalHeaderLabels(["개설연도", "개설학기","영역1","영역2","영역3","학정번호","과목명","학점","시간","정원"])


    def indexChanged(self, index):
        self.comboBox_3.clear()
        data = self.comboBox_2.itemData(index)
        if data is not None:
            self.comboBox_3.addItems(data)


    def setupUi(self, MainWindow,StudentID):
        self.StudentID = int(StudentID)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 725)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(220, 35, 190, 22))
        self.comboBox_2.setObjectName("comboBox_2")

        self.comboBox_2.addItem('전체', ['전체'])
        self.comboBox_2.addItem('학부선택(~2009)', ['전체','인간이해와역사', '과학과기술', '사회와가치', '문학과예술', '외국어와세계이해', '건강과스포츠'])
        self.comboBox_2.addItem('계열기초(~2009)', ['전체','계열기초'])
        self.comboBox_2.addItem('학부필수(~2009)', ['전체','인간의이해', '자연의이해', '사회의이해', '문화의이해', '세계의이해'])
        self.comboBox_2.addItem('학부기초(~2009)', ['전체','기독교의이해', '대학영어'])
        self.comboBox_2.addItem('선택교양(10~18)', ['전체','역사·철학영역', '과학·기술영역', '사회·윤리영역', '인문·예술영역', '세계문화·언어영역', '생활·건강영역'])
        self.comboBox_2.addItem('필수교양(10~18)', ['전체','문학과예술', '인간과역사', '언어와표현', '가치와윤리', '국가와사회공동체', '지역사회와세계', '논리와수리','자연과우주', '생명과환경', '소프트웨어'])
        self.comboBox_2.addItem('공통기초(10~18)', ['전체','채플', '기독교의이해', '대학영어', '글쓰기'])
        self.comboBox_2.addItem('기초교육(2019~)', ['전체','자율선택'])
        self.comboBox_2.addItem('대학교양(2019~)', ['전체','문학과예술', '인간과역사', '언어와표현', '가치와윤리', '국가와사회', '지역과세계', '논리와수리','자연과우주', '생명과환경', '정보와기술', '체육과건강'])
        self.comboBox_2.addItem('교양기초(2019~)', ['전체','채플', '기독교의이해', '글쓰기', '대학영어'])
        self.comboBox_2.addItem('음악대학', ['전체','음악대학공통', '교회음악전공', '성악전공', '피아노전공', '관현악전공', '작곡전공'])
        self.comboBox_2.addItem('사회과학대학', ['전체','사회과학대학공통', '정치외교학전공', '행정학전공', '사회복지학전공', '사회학전공', '문화인류학전공','언론홍보영상학부'])
        self.comboBox_2.addItem('생명시스템대학', ['전체','생명시스템공통', '시스템생물학전공', '생화학전공', '생명공학전공'])
        self.comboBox_2.addItem('글로벌인재대학', ['전체','GLC공통교과과정', '글로벌인재학부-국제통상전공', '글로벌인재학부-한국문화전공',
       '글로벌인재학부-한국언어문화교육전공', '글로벌인재학부-문화·미디어전공', '글로벌인재학부-응용정보공학전공',
       'GLD공통교과과정', '글로벌인재학부-바이오생활공학전공'])
        self.comboBox_2.addItem('약학대학', ['전체','약학전공'])
        self.comboBox_2.addItem('언더우드국제대학', ['전체','공통교과과정(신촌)', '공통교과과정(국제)', '언더우드학부(인문사회)-비교문학과문화',
       '언더우드학부(인문사회)-경제학', '언더우드학부(인문사회)-국제학', '언더우드학부(인문사회)-정치외교학',
       '언더우드학부(공학)-생명과학공학', '아시아학부-아시아학', '테크노아트학부-정보·인터랙션디자인',
       '테크노아트학부-창의기술경영', '테크노아트학부-문화디자인경영', '융합사회과학부-사회정의리더십',
       '융합사회과학부-계량위험관리', '융합사회과학부-과학기술정책', '융합사회과학부-지속개발협력',
       '융합과학공학부-나노과학공학', '융합과학공학부-에너지환경융합', '융합과학공학부-바이오융합'])
        self.comboBox_2.addItem('교육과학대학', ['전체','교육학전공', '체육교육학전공', '스포츠응용산업전공'])
        self.comboBox_2.addItem('생활과학대학', ['전체','의류환경학전공', '식품영양학전공', '실내건축학전공', '아동·가족전공', '생활디자인전공'])
        self.comboBox_2.addItem('공과대학', ['전체','공과대학공통', '화공생명공학전공', '전기전자공학전공', '건축공학전공', '건축학(설계)', '도시공학전공',
       '건설환경공학전공', '기계공학전공', '신소재공학전공', '산업공학전공', '컴퓨터과학전공', 'IT융합공학전공'])
        self.comboBox_2.addItem('이과대학', ['전체','이과대학 공통', '수학전공', '물리학전공', '화학전공', '지구시스템과학전공', '천문우주학전공',
       '대기과학전공'])
        self.comboBox_2.addItem('경영대학', ['전체','경영학전공'])
        self.comboBox_2.addItem('상경대학', ['전체','상경대학 공통', '경제학전공', '응용통계학전공'])
        self.comboBox_2.addItem('문과대학', ['전체','문과대학 공통', '국어국문학전공', '사학전공', '철학전공', '문헌정보학전공', '심리학전공',
       '중어중문학전공', '영어영문학전공', '독어독문학전공', '불어불문학전공', '노어노문학전공'])
        self.comboBox_2.currentIndexChanged.connect(self.indexChanged)



        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(430, 35, 190, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.indexChanged(self.comboBox_2.currentIndex())



        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(630, 35, 461, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.returnPressed.connect(self.find_subject)



        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(20, 35, 80, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_5 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_5.setGeometry(QtCore.QRect(120, 35, 80, 22))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1100, 35, 70, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.find_subject)




        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 110, 1071, 551))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setRowCount(6000)
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers )
        self.tableWidget.itemDoubleClicked.connect(self.subject_info)
        self.tableWidget.setHorizontalHeaderLabels(["개설연도", "개설학기","영역1","영역2","영역3","학정번호","과목명","학점","시간","정원"])




        #Check 졸업요건 
        db = pymysql.connect(host='127.0.0.1',database= 'mydb', port=3306,user='root',passwd='1234',charset='utf8mb4')
        cursor = db.cursor()
        sql = "SELECT * FROM GRADREQTREE WHERE DEPTH = '1'"
        cursor.execute(sql)
        rtn = cursor.fetchall()
        check = {}
        for i in rtn:
            if type(yiie[i[3]] ) != str:
                sql = """SELECT SUM(Credit) FROM SUBJECTS
                        WHERE (SUBJECTS.OpenYear, SUBJECTS.OpenSem, SUBJECTS.G2, SUBJECTS.G3, SUBJECTS.SubjectID) IN
                        (SELECT SUBJECT_OpenYear,SUBJECT_OpenSem, SUBJECT_G2,SUBJECT_G3, SUBJECT_SubjectID 
                        FROM finishedsubject 
                        WHERE STUDENT_StudentID = {} AND Grade != 'F') AND SUBJECTS.G3 = '{}';""".format(self.StudentID,i[3])
                cursor.execute(sql)
                temp = cursor.fetchall()[0][0]
                if temp == None:
                    check[i[3]] = ['X', yiie[i[3]]]
                    continue
                if int(temp) >= yiie[i[3]]:
                    check[i[3]] = ['O', 0]
                else:
                    check[i[3]] = ['X',yiie[i[3]]-int(temp)]
        db.close()


        self.gradreq = QtWidgets.QTableWidget(self.centralwidget)
        self.gradreq.setGeometry(QtCore.QRect(1125, 110, 245, 551))
        self.gradreq.setObjectName("gradreq")
        self.gradreq.setColumnCount(3)
        self.gradreq.setRowCount(15)
        self.gradreq.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.gradreq.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers )
        for row_number, row_data in enumerate(check.keys()):
            self.gradreq.insertRow(row_number)
            self.gradreq.setItem(row_number, 0, QtWidgets.QTableWidgetItem(row_data))
            self.gradreq.setItem(row_number, 1, QtWidgets.QTableWidgetItem(str(check[row_data][0])))
            self.gradreq.setItem(row_number, 2, QtWidgets.QTableWidgetItem(str(check[row_data][1])))

        self.gradreq.setHorizontalHeaderLabels(["졸업요건", "만족\n여부","부족\n학점"])
        header = self.gradreq.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.gradreq.itemDoubleClicked.connect(self.check_gradreq)
        




        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 80, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1140, 80, 71, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1190, 10, 81, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1290, 10, 81, 51))
        self.pushButton_3.setObjectName("pushButton_3")
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

        self.comboBox_4.setItemText(0, _translate("MainWindow", "2019"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "1학기"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "2학기"))
        self.pushButton.setText(_translate("MainWindow", "Search"))
        self.label.setText(_translate("MainWindow", "Search Result"))
        self.label_2.setText(_translate("MainWindow", "졸업요건"))
        self.pushButton_2.setText(_translate("MainWindow", "Campus\n"
"Map"))
        self.pushButton_3.setText(_translate("MainWindow", "Logout"))

yiie = {"필수교양5영억":15,
        "논리와수리":12,
        "자연과우주":6,
        "생명과환경":6,
        "전공기초":6,
        "채플":2,
        "전공선택":61,
        "전체이수학점":140,
        "글쓰기":3,
        "대학영어":4,
        "기독교의이해":3}



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
