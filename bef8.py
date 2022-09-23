from bs4 import BeautifulSoup
from requests import * 
from re import * 
from random import *
from csv import * # csv파일로 변환 할 수 있는 모듈

filenm = "kospi.csv"
f = open(filenm, "w", encoding="euc-kr", newline="") #csv파일 저장시 euc-kr적용하면 한글깨짐 방지
#newline : csv에 데이터 등록시 한칸 띄어쓰기가 되는 경우 있음. 해당

writer = writer(f)

url="https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page=1"
web=get(url)
web.raise_for_status()

html=BeautifulSoup(web.text,"lxml")
table=html.find("table",attrs={"class":"type_2"})
tbody=table.find("tbody")
tr=tbody.find_all("tr")

for data in tr:
    td = data.find_all("td")
    data = [text.get_text() for text in td]
    if len(data) <= 1:
        continue
    else:
        company = data[1]
        price = data[2].strip().replace(",","")
        face = data[3].strip().replace(",","")
        print(company,price,face)
        #writerow : 엑셀 기준 , 입력시켜서 다음칸으로 적용되는 형태
        rowdata=[company,price,face] #배열로 생성해야만 csv에서 하나의 행,열로 인식
        writer.writerow(rowdata)