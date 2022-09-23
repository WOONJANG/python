# messagebox는 alert과 동일한 메시지 출력
from tkinter.messagebox import *
from tkinter import *
from bs4 import BeautifulSoup
# requests 통신 api json형태로 변화되어서 웹사이트 접속하는 형태
import requests
from urllib import parse
from re import *
from sqlite3 import *
# db접속 정보 
from dbconnect import *
from datetime import *



# 크롤링 버튼 함수
def crawling_btn_def(data):
    # showinfo == alert
    # print(len(data)) # 빈 값이 1이 나오므로 len으로 조건문을 걸어야함
    if len(data) <= 1 | len(data) < 10 :
        showinfo("경고", "크롤링할 url주소 입력")
    else:
        # try, except, finally 문제 발생시 예외처리 하는 형태
        try:
            # urlencoding = parse.quote(data)
            # print(urlencoding)
            url = data
            url = "{}".format(data) # 문자열로 변환해야만 requests를 사용할 수 있음
            # print(type(url))
            # print(url) 
            check = requests.get(url.strip(), headers={"User-Agent":"Mozilla/5.1"}) # \n, \ 빈공간 제거
            # print(check)
            ck = check.raise_for_status()
            # print(type(ck))

            if ck==None:
            # if str(ck)=="None":
                html = BeautifulSoup(check.text, "lxml")
                # 스크래핑
                div = html.find("div",attrs={"module-design-id":"17"})
                div2 = div.find_all("div",attrs={"class":"component--item_card"})
                # 이름 스크래핑
                # title = div2[1].find("span", attrs={"class":"text--title"})
                # print(title)
                # 가격 스크래핑
                # money = div2[1].find("strong",attrs={"class":"text--price_seller"})
                # print(money)
                con = connect.cursor()
                for z in div2:
                    title = z.find("span", attrs={"class":"text--title"})
                    money = z.find("strong",attrs={"class":"text--price_seller"})
                    money = sub(",","", money.text) # sub 사용시 from re import *

                    # DB 에서 날짜 입력을 저장 시키기 위해서 strftime : 문자열 형태의 시간으로 변경
                    now_date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                    # now_date = datetime.today().strftime("%H:%M:%S")
                    print(title.text, money, now_date)
                    # DB 저장
                    sql = "insert into pension values ('0','"+title.text+"','"+money+"','"+now_date+"')"
                    con.execute(sql)
                    connect.commit()    

                showinfo("알림", "정상적인 주소 형태")
                showinfo("완료", data+" 스크래핑 완료")
        except:
            showinfo("알림", "크롤링할 url주소 확인")
            showinfo("실패", data+" 크롤링 실패")

    # print(data)


