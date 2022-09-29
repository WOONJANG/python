# 크롤링 & 스크래핑
from bs4 import BeautifulSoup
from requests import *

url = "https://www.ode.co.kr/shop/faq.html"
call = get(url)
call.raise_for_status()

htmlcode=BeautifulSoup(call.content.decode('euc-kr','replace'),"lxml")
# print(htmlcode)
code = htmlcode.find("div", attrs={"id":"faqTable"})
code2 = code.find("tbody")
code3 = code2.find_all("div", attrs={"class":"tb-center"})
code4 = code2.find_all("div", attrs={"class":"tb-left"})
# print(code3)
ea = len(code4)
# print(ea)
for idx, z in enumerate(code3):
    if idx != 0 | idx%2 != 0:
        print(z.get_text())
    if idx < ea:
        print(code4[idx].get_text())
        





'''
url = "http://jangwoon0518.cafe24.com/site.html"
call = get(url)
call.raise_for_status()

htmlcode=BeautifulSoup(call.content.decode('utf-8','replace'),"lxml")
# print(htmlcode)
code = htmlcode.find("div", attrs={"class":"divcss"})
code2 = code.find("ul",attrs={"class":"ulcss"})
code3 = code2.find_all("li")
# print(len(code3))
array = []
f = 0
for txt in code3:
    array += txt.get_text()

print(array)
'''