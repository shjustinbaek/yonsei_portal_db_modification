from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
import csv


#driver 정하기 크롬을 쓸것이냐, PhantomJS를 쓸 것이냐, 혹은 크롬 headless를 쓸것이냐.
#driver = webdriver.PhantomJS(r"C:\PhantomJs\bin\phantomjs\bin\phantomjs.exe")
driver = webdriver.Chrome(executable_path=r"C:\Users\naval\Downloads\chromedriver_win32\chromedriver.exe")
options = webdriver.ChromeOptions()



#create csv file
total_cols = ['구분1','구분2','구분3','학정번호-분반-실습','과목명','학점','담당교수','강의시간','강의실','정원','참여인원',
              '전공자 정원 (2전공포함)','학년별정원 1학년','학년별정원 2학년','학년별정원 3학년','학년별정원 4학년','교환학생 가능여부',
              'Max Mileage','마일리지 최소값','마일리지 최대값', '마일리지 평균값'
              '순위','마일리지','전공자/복수전공자(전공자정원포함여부)','신청과목수','졸업신청','초수강여부','총이수학점/졸업이수학점','직전학기이수학점/학기당수강학점','학년','수강여부','비고']
f = open('yonseimileage.csv', 'w', encoding='ms949', newline='')
wr = csv.writer(f)
wr.writerow(total_cols)


url = 'http://ysweb.yonsei.ac.kr:8888/curri120601/curri_new.jsp#top'
driver.get(url)
driver.implicitly_wait(3)
#### wait 해야함

#연도 설정
#참고: 마일리지 제도는 2015년 2학기 때부터 시행되었음
year_btn = Select(driver.find_element_by_css_selector('#HY'))
#자동화는 나중에
year_options = [x.text for x in list(year_btn.options) if int(x.text) >= 2015]
year_btn.select_by_visible_text('2019')

#학기 설정
semester = Select(driver.find_element_by_css_selector('#HG'))
semester_options = [x.text for x in list(semester.options)]
semester.select_by_visible_text('1학기')
#주의할것 - 여름학기 겨울학기 필요 없음.

#가장 왼쪽 box
box1 = Select(driver.find_element_by_css_selector('#OCODE0'))
box1_options = [x.text for x in list(box1.options)]
box1_options = box1_options[:1] #Test 할때 한개만 돌리 위해서
for option1 in box1_options:
    box1.select_by_visible_text(option1)
    #왼쪽에서 2번째 box
    box2 = Select(driver.find_element_by_css_selector('#OCODE1'))
    box2_options = [x.text for x in list(box2.options)]
    box2_options.remove('계절학기') #계절학기는 필요가 없음.
    for option2 in box2_options:
        box2.select_by_visible_text(option2)
        #왼쪽에서 3번째 box
        box3 = Select(driver.find_element_by_css_selector("#S2"))
        box3_options = [x.text for x in list(box3.options) if x.text != '전체']
        for option3 in box3_options:
            box3.select_by_visible_text(option3)
            search_btn = driver.find_element_by_css_selector("#myForm > table > tbody > tr:nth-child(1) > td:nth-child(1) > a:nth-child(6)")
            search_btn.click()

            #과목 정보 가져오기


            # 페이지 수, 페이지 넘김 횟수 결정
            # 한 페이지에 최대 15개 display함            '
            content = WebDriverWait(driver, 5).until(
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
            rtn = []
            for row in rows:
                if row.text != '' and row.text != 'No data to display':
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

                        # 마일리지 신청 조회
                        mile_info = driver.find_element_by_css_selector("body > form > table:nth-child(9)")
                        mile_rows = mile_info.find_elements_by_css_selector("tr")
                        del mile_rows[1]
                        mile_childs = [x.find_elements_by_css_selector("td") for x in mile_rows]
                        temp2 = []
                        for a in mile_childs:
                            temp2.append(temp1 + [x.text for x in a])
                        del temp2[0]
                        rtn.extend(temp2)

                        driver.close()
                        driver.switch_to_window(driver.window_handles[0])
                    except:
                        driver.close()
                        driver.switch_to_window(driver.window_handles[0])
                        print('unable to access info from {}'.format(row.text))
                else:
                    pass
            for i in rtn:
                wr.writerow([option1,option2,option3] + i)
                print('writing row...')
            for i in range(next_click_num):
                nxt = driver.find_element_by_css_selector('#pager > div > div > div:nth-child(1)')
                nxt.click()
                content = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#contenttablejqxgrid")))
                rows = content.find_elements_by_css_selector("div[role = 'row']")
                rtn = []
                for row in rows:
                    if row.text != ''and row.text != 'No data to display':
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

                            # 마일리지 신청 조회
                            mile_info = driver.find_element_by_css_selector("body > form > table:nth-child(9)")
                            mile_rows = mile_info.find_elements_by_css_selector("tr")
                            del mile_rows[1]
                            mile_childs = [x.find_elements_by_css_selector("td") for x in mile_rows]
                            temp2 = []
                            for a in mile_childs:
                                temp2.append(temp1 + [x.text for x in a])
                            del temp2[0]
                            rtn.extend(temp2)

                            driver.close()
                            driver.switch_to_window(driver.window_handles[0])
                        except:
                            driver.close()
                            driver.switch_to_window(driver.window_handles[0])
                            print('unable to access info from {}'.format(row.text))
                    else:
                        pass
                for i in rtn:
                    wr.writerow([option1, option2, option3] + i)
                    print('writing row...')

f.close()


