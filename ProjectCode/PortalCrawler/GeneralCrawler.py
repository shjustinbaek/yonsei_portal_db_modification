from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
import csv
import sys
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

#driver 정하기 크롬을 쓸것이냐, PhantomJS를 쓸 것이냐, 혹은 크롬 headless를 쓸것이냐.
#driver = webdriver.PhantomJS(r"C:\PhantomJs\bin\phantomjs\bin\phantomjs.exe")
driver = webdriver.Chrome(executable_path=r"C:\Users\naval\Downloads\chromedriver_win32\chromedriver.exe")
options = webdriver.ChromeOptions()

#create csv file
SUBJECT = open('db/SUBJECT_19_2_생활과학대학_to_글로벌인재대학.csv', 'w', encoding='utf-8', newline='')
CLASSPROPERTY = open('db/CLASSPROPERTY_19_2_생활과학대학_to_글로벌인재대학.csv', 'w', encoding='utf-8', newline='')
SUBJECT_PROFESSOR = open('db/SUBJECT_PROFESSOR_19_2_생활과학대학_to_글로벌인재대학.csv', 'w', encoding='utf-8', newline='')
WEEKLYSYLLABUS = open('db/WEEKLYSYLLABUS_19_2_생활과학대학_to_글로벌인재대학.csv', 'w', encoding='utf-8', newline='')
SUBJECT_BUILDING = open('db/SUBJECT_BUILDING_19_2_생활과학대학_to_글로벌인재대학.csv', 'w', encoding='utf-8', newline='')

wSUBJECT = csv.writer(SUBJECT)
wCLASSPROPERTY = csv.writer(CLASSPROPERTY)
wSUBJECT_PROFESSOR = csv.writer(SUBJECT_PROFESSOR)
wWEEKLYSYLLABUS = csv.writer(WEEKLYSYLLABUS)
wSUBJECT_BUILDING = csv.writer(SUBJECT_BUILDING)

# 각 relation column 이름 설정
subjectrownames = 'OpenYear, OpenSem,G1,G2,G3,SubjectID,SubjectName,Credit,SubjectTime,FullCapa,MajorCapa,1capa,2capa,3capa,4capa,IfExchangeP,MaxMileage,SyllUploadDate,SyllLastUpdate,SubjectisFor,SubjectGoal,Prerequisite,SubjectMethod,SubjectGP,TextBook,InfoProf,InfoTA,EngSyll'.split(',')
wSUBJECT.writerow(subjectrownames)
wCLASSPROPERTY.writerow(['OpenYear', 'OpenSem', 'G1', 'G2', 'G3', 'SubjectId', 'Property'])
wSUBJECT_PROFESSOR.writerow(['OpenYear','OpenSem','G1','G2','G3','SubjectID','ProfName', 'Department', 'OfficeNumber', 'Phone', 'Email'])
wWEEKLYSYLLABUS.writerow(['OpenYear', 'OpenSem', 'G1', 'G2', 'G3', 'SubjectId', 'Week', 'DatePeriod', 'Content', 'Event', 'Remarks'])
wSUBJECT_BUILDING.writerow(['OpenYear', 'OpenSem', 'G1', 'G2', 'G3', 'SubjectId','BuildingName'])


url = 'http://ysweb.yonsei.ac.kr:8888/curri120601/curri_new.jsp#top'
driver.get(url)
driver.implicitly_wait(3)
#### wait 해야함

#연도 설정
#참고: 마일리지 제도는 2015년 2학기 때부터 시행되었음
year_btn = Select(driver.find_element_by_css_selector('#HY'))
#자동화는 나중에
year_options = [x.text for x in list(year_btn.options) if int(x.text) >= 2015]
openyear = '2019'
year_btn.select_by_visible_text(openyear)

#학기 설정
semester = Select(driver.find_element_by_css_selector('#HG'))
semester_options = [x.text for x in list(semester.options)]
opensem = '2학기'
semester.select_by_visible_text(opensem)
#주의할것 - 여름학기 겨울학기 필요 없음.

#가장 왼쪽 box
box1 = Select(driver.find_element_by_css_selector('#OCODE0'))
box1_options = [x.text for x in list(box1.options)]
box1_options = box1_options[:1] #Test 할때 한개만 돌리 위해서



for option1 in box1_options:
    ######### Test 용
    #option1 = box1_options[0]

    box1.select_by_visible_text(option1)
    #왼쪽에서 2번째 box
    box2 = Select(driver.find_element_by_css_selector('#OCODE1'))
    box2_options = [x.text for x in list(box2.options)]
    box2_options = box2_options[21:27]
    #box2_options.remove('계절학기') #계절학기는 필요가 없음.
    for option2 in box2_options:
        print("Crawling: {} ...".format(option2))
        ############## Test 용
        #option2 = box2_options[5]

        box2.select_by_visible_text(option2)
        #왼쪽에서 3번째 box
        box3 = Select(driver.find_element_by_css_selector("#S2"))
        box3_options = [x.text for x in list(box3.options) if x.text != '전체']
        for option3 in box3_options:

            ############# Test 용
            #option3 = box3_options[2]

            box3.select_by_visible_text(option3)
            search_btn = driver.find_element_by_css_selector("#myForm > table > tbody > tr:nth-child(1) > td:nth-child(1) > a:nth-child(6)")
            search_btn.click()

            # 페이지 수, 페이지 넘김 횟수 결정
            # 한 페이지에 최대 15개 display함
            content = WebDriverWait(driver, 10).until(
                             EC.presence_of_element_located((By.CSS_SELECTOR, "#contenttablejqxgrid")))
            # 게시글할 글이 있던 없던 row 태그는 15개씩 나온다. 게시글이 없다면. 비어있는 row 테그가 나온다.
            pg_info = driver.find_element_by_css_selector('#pager > div > div > div:nth-child(3)').text
            cls_num = int(pg_info.split()[-1])
            next_click_num = None
            if cls_num % 15 != 0:
                next_click_num = cls_num // 15
            else:
                next_click_num = (cls_num // 15) - 1

            # 정보 가져오기 (1페이지 읽고 -> 페이지 넘김 + 페이지 일고 x 넘김 횟수)
            rows = content.find_elements_by_css_selector("div[role = 'row']")
            ######################################## row for loop ##########################################
            for row in rows:
                subrow_end = None
                if row.text != '' and row.text != 'No data to display':
                    # SubjectID, ClassProperty
                    SubjectID = row.find_element_by_css_selector('div:nth-child(7) > span').text
                    ClassProp = None
                    try:
                        ClassProp = row.find_element_by_css_selector('div:nth-child(17) > span > a').text
                    except:
                        try:
                            ClassProp = row.find_element_by_css_selector('div:nth-child(17) > span > font').text
                            print('================\n',"폐강 선택 완료\n",'================\n')
                        except:
                            print("유의사항 선택 애러 error:", sys.exc_info()[0])

                    # write_to_CLASSPROPERTY
                    wCLASSPROPERTY.writerow([openyear,opensem,option1,option2,option3,SubjectID,ClassProp])

                    #보라 버튼
                    try:
                        syl = row.find_element_by_css_selector('div:nth-child(7) > span > a:nth-child(3)')
                        syl.click()
                        pop_up = driver.window_handles[1]
                        driver.switch_to_window(pop_up)
                        driver.implicitly_wait(3)

                        ClsInfoBox = driver.find_elements_by_css_selector('body > form > table:nth-child(3) > tbody > tr')
                        if ClsInfoBox[4].text.startswith('참고자료'):
                            ProfInfo = ClsInfoBox[6:-10]
                        else:
                            ProfInfo = ClsInfoBox[5:-10]
                        NProf = int(len(ProfInfo)/3)

                        #Writewrite_to_SUBJECT_PROFESSOR
                        for i in range(NProf):
                            ProfName = ProfInfo[i*3].find_element_by_css_selector('td:nth-child(2)').text
                            Department = ProfInfo[i*3].find_element_by_css_selector('td:nth-child(4)').text
                            OfficeNumber = ProfInfo[i*3+1].find_element_by_css_selector('td:nth-child(2)').text
                            Phone = ProfInfo[i*3+1].find_element_by_css_selector('td:nth-child(4)').text
                            Email = ProfInfo[i*3+2].find_element_by_css_selector('td:nth-child(2)').text
                            wSUBJECT_PROFESSOR.writerow(
                                [openyear, opensem, option1, option2, option3, SubjectID, ProfName, Department,
                                 OfficeNumber, Phone, Email])

                        #SUBJECT/BUILDING TABLE
                        BuildingName = ClsInfoBox[3].find_elements_by_css_selector('td')[1].text
                        #write [openyear,opensem,option1,option2,option3,SubjectID,BuildingName]
                        wSUBJECT_BUILDING.writerow([openyear,opensem,option1,option2,option3,SubjectID,BuildingName])

                        SyllUploadDate = ClsInfoBox[1].find_elements_by_css_selector('td')[1].text
                        SyllLastUpdate = ClsInfoBox[1].find_elements_by_css_selector('td')[3].text
                        SubjectisFor = ClsInfoBox[-9].find_elements_by_css_selector('td')[1].text
                        SubjectGoal = ClsInfoBox[-8].find_elements_by_css_selector('td')[1].text
                        Prerequisite = ClsInfoBox[-7].find_elements_by_css_selector('td')[1].text
                        SubjectMethod = ClsInfoBox[-6].find_elements_by_css_selector('td')[1].text
                        SubjectGP = ClsInfoBox[-5].find_elements_by_css_selector('td')[1].text
                        TextBook = ClsInfoBox[-4].find_elements_by_css_selector('td')[1].text
                        InfoProf = ClsInfoBox[-3].find_elements_by_css_selector('td')[1].text
                        InfoTA = ClsInfoBox[-2].find_elements_by_css_selector('td')[1].text
                        EngSyll = ClsInfoBox[-1].find_elements_by_css_selector('td')[1].text

                        subrow_end = [SyllUploadDate,SyllLastUpdate,SubjectisFor,SubjectGoal,Prerequisite,SubjectMethod,SubjectGP,TextBook,InfoProf,InfoTA,EngSyll]

                        #WEEKLYSYLLABUS 가져오기
                        weekrows = driver.find_elements_by_css_selector('body > form > table:nth-child(4) > tbody > tr')
                        for eachweek in weekrows[1:]:
                            week_info = eachweek.find_elements_by_css_selector('td')
                            week_txt = [a.text for a in week_info]
                            #WEEKLYSYLLABUS write row
                            wWEEKLYSYLLABUS.writerow([openyear,opensem,option1,option2,option3,SubjectID]+week_txt)

                        driver.close()
                        driver.switch_to_window(driver.window_handles[0])


                    except:
                        print("Unexpected error:", sys.exc_info()[0])
                        driver.close()
                        driver.switch_to_window(driver.window_handles[0])
                        print('unable to access 주황버튼 from {}'.format(row.text))

                    #주황버튼
                    try:
                        mile = row.find_element_by_css_selector('div:nth-child(7) > span > a:nth-child(4)')
                        mile.click()
                        pop_up = driver.window_handles[1]
                        driver.switch_to_window(pop_up)
                        driver.implicitly_wait(3)

                        # get_class_info
                        cls_info = driver.find_element_by_css_selector(
                            'body > form > table:nth-child(3) > tbody > tr:nth-child(4)')
                        cls_child = cls_info.find_elements_by_css_selector("*")
                        temp1 = [x.text for x in cls_child]
                        if len(temp1) != 18:
                            print("Error with top table at 주황버튼")
                        #write subject table
                        #SubjectName, Credit,SubjectTime, FullCapa, MajorCapa, 1capa, 2capa, 3capa, 4capa, IfExchangeP, MaxMileage
                        subrow_mid = [temp1[1],temp1[2],temp1[4],temp1[6],temp1[2],temp1[8],temp1[9],temp1[10],temp1[11],temp1[12],temp1[13],temp1[14]]
                        wSUBJECT.writerow([openyear,opensem,option1,option2,option3,SubjectID]+subrow_mid+subrow_end)

                        driver.close()
                        driver.switch_to_window(driver.window_handles[0])
                    except:
                        print("Unexpected error:", sys.exc_info()[0])
                        driver.close()
                        driver.switch_to_window(driver.window_handles[0])
                        print('unable to access 주황버튼 from {}'.format(row.text))
                else:
                    pass
            ######################################## row for loop ##########################################

            for i in range(next_click_num):
                #가장 끝페이지로 갔다가 다시 돌아옴 (상관은 없다)
                nxt = driver.find_element_by_css_selector('#pager > div > div > div:nth-child(1)')
                nxt.click()
                content = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#contenttablejqxgrid")))
                rows = content.find_elements_by_css_selector("div[role = 'row']")
                ######################################## row for loop ##########################################
                for row in rows:
                    subrow_end = None
                    if row.text != '' and row.text != 'No data to display':
                        # SubjectID, ClassProperty
                        SubjectID = row.find_element_by_css_selector('div:nth-child(7) > span').text
                        ClassProp = None
                        try:
                            ClassProp = row.find_element_by_css_selector('div:nth-child(17) > span > a').text
                        except:
                            try:
                                ClassProp = row.find_element_by_css_selector('div:nth-child(17) > span > font').text
                                print('================\n', "폐강 선택 완료\n", '================\n')
                            except:
                                print("유의사항 선택 애러 error:", sys.exc_info()[0])

                        # write_to_CLASSPROPERTY
                        wCLASSPROPERTY.writerow([openyear, opensem, option1, option2, option3, SubjectID, ClassProp])

                        # 보라 버튼
                        try:
                            syl = row.find_element_by_css_selector('div:nth-child(7) > span > a:nth-child(3)')
                            syl.click()
                            pop_up = driver.window_handles[1]
                            driver.switch_to_window(pop_up)
                            driver.implicitly_wait(3)

                            ClsInfoBox = driver.find_elements_by_css_selector(
                                'body > form > table:nth-child(3) > tbody > tr')
                            if ClsInfoBox[4].text.startswith('참고자료'):
                                ProfInfo = ClsInfoBox[6:-10]
                            else:
                                ProfInfo = ClsInfoBox[5:-10]
                            NProf = int(len(ProfInfo) / 3)

                            # Writewrite_to_SUBJECT_PROFESSOR
                            for i in range(NProf):
                                ProfName = ProfInfo[i * 3].find_element_by_css_selector('td:nth-child(2)').text
                                Department = ProfInfo[i * 3].find_element_by_css_selector('td:nth-child(4)').text
                                OfficeNumber = ProfInfo[i * 3 + 1].find_element_by_css_selector('td:nth-child(2)').text
                                Phone = ProfInfo[i * 3 + 1].find_element_by_css_selector('td:nth-child(4)').text
                                Email = ProfInfo[i * 3 + 2].find_element_by_css_selector('td:nth-child(2)').text
                                wSUBJECT_PROFESSOR.writerow(
                                    [openyear, opensem, option1, option2, option3, SubjectID, ProfName, Department,
                                     OfficeNumber, Phone, Email])

                            # SUBJECT/BUILDING TABLE
                            BuildingName = ClsInfoBox[3].find_elements_by_css_selector('td')[1].text
                            # write [openyear,opensem,option1,option2,option3,SubjectID,BuildingName]
                            wSUBJECT_BUILDING.writerow(
                                [openyear, opensem, option1, option2, option3, SubjectID, BuildingName])

                            SyllUploadDate = ClsInfoBox[1].find_elements_by_css_selector('td')[1].text
                            SyllLastUpdate = ClsInfoBox[1].find_elements_by_css_selector('td')[3].text
                            SubjectisFor = ClsInfoBox[-9].find_elements_by_css_selector('td')[1].text
                            SubjectGoal = ClsInfoBox[-8].find_elements_by_css_selector('td')[1].text
                            Prerequisite = ClsInfoBox[-7].find_elements_by_css_selector('td')[1].text
                            SubjectMethod = ClsInfoBox[-6].find_elements_by_css_selector('td')[1].text
                            SubjectGP = ClsInfoBox[-5].find_elements_by_css_selector('td')[1].text
                            TextBook = ClsInfoBox[-4].find_elements_by_css_selector('td')[1].text
                            InfoProf = ClsInfoBox[-3].find_elements_by_css_selector('td')[1].text
                            InfoTA = ClsInfoBox[-2].find_elements_by_css_selector('td')[1].text
                            EngSyll = ClsInfoBox[-1].find_elements_by_css_selector('td')[1].text

                            subrow_end = [SyllUploadDate, SyllLastUpdate, SubjectisFor, SubjectGoal, Prerequisite,
                                          SubjectMethod, SubjectGP, TextBook, InfoProf, InfoTA, EngSyll]

                            # WEEKLYSYLLABUS 가져오기
                            weekrows = driver.find_elements_by_css_selector(
                                'body > form > table:nth-child(4) > tbody > tr')
                            for eachweek in weekrows[1:]:
                                week_info = eachweek.find_elements_by_css_selector('td')
                                week_txt = [a.text for a in week_info]
                                # WEEKLYSYLLABUS write row
                                wWEEKLYSYLLABUS.writerow(
                                    [openyear, opensem, option1, option2, option3, SubjectID] + week_txt)

                            driver.close()
                            driver.switch_to_window(driver.window_handles[0])


                        except:
                            print("Unexpected error:", sys.exc_info()[0])
                            driver.close()
                            driver.switch_to_window(driver.window_handles[0])
                            print('unable to access 주황버튼 from {}'.format(row.text))

                        # 주황버튼
                        try:
                            mile = row.find_element_by_css_selector('div:nth-child(7) > span > a:nth-child(4)')
                            mile.click()
                            pop_up = driver.window_handles[1]
                            driver.switch_to_window(pop_up)
                            driver.implicitly_wait(3)

                            # get_class_info
                            cls_info = driver.find_element_by_css_selector(
                                'body > form > table:nth-child(3) > tbody > tr:nth-child(4)')
                            cls_child = cls_info.find_elements_by_css_selector("*")
                            temp1 = [x.text for x in cls_child]
                            if len(temp1) != 18:
                                print("Error with top table at 주황버튼")
                            # write subject table
                            # SubjectName, Credit,SubjectTime, FullCapa, MajorCapa, 1capa, 2capa, 3capa, 4capa, IfExchangeP, MaxMileage
                            subrow_mid = [temp1[1], temp1[2], temp1[4], temp1[6], temp1[2], temp1[8], temp1[9],
                                          temp1[10], temp1[11], temp1[12], temp1[13], temp1[14]]
                            wSUBJECT.writerow(
                                [openyear, opensem, option1, option2, option3, SubjectID] + subrow_mid + subrow_end)

                            driver.close()
                            driver.switch_to_window(driver.window_handles[0])
                        except:
                            print("Unexpected error:", sys.exc_info()[0])
                            driver.close()
                            driver.switch_to_window(driver.window_handles[0])
                            print('unable to access 주황버튼 from {}'.format(row.text))
                    else:
                        pass
                ######################################## row for loop ##########################################

SUBJECT.close()
CLASSPROPERTY.close()
SUBJECT_PROFESSOR.close()
WEEKLYSYLLABUS.close()
SUBJECT_BUILDING.close()



