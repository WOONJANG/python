from bs4 import BeautifulSoup
from os import *
from requests import *
from idlelib.iomenu import encoding
from urllib.request import urlopen
from tkinter import *

# url = "https://sports.naver.com/news?oid=236&aid=0000227648"
url = "https://www.nate.com/"
res = get(url)
res.raise_for_status()

result = BeautifulSoup(res.text, "lxml")
# 태그 이름을 적용하여 태그 안에 있는 텍스트를 가져올 수 있음
# 단 중복된 태그가 있을 경우 제일 먼저 읽어오는 라인만 처리가 됨
# print(str(result.title))
# print(result.title.get_text())
# print(result.h4.get_text())

# find : 해당 단어를 찾습니다. attrs(attribute 속성명)
rank = result.find("div",attrs={"class":"isKeyword"})
# print(rank.h4.get_text())
# print(rank.li)
# rank에만 속하는 태그 중 span 태그와 해당 class명을 검토
# ranknum = rank.find("span",attrs={"class":"num_rank"})
ranksubject = rank.find("span",attrs={"class":"txt_rank"})
# print(len(rank.li)) # 반복되는 태그의 개수를 확인함
# print(ranknum.get_text())
# print(ranksubject.get_text())

# find : 1개의 태그
# find_all : 해당 부모 마크업 안에 있는 모든 태그를 의미 기본으로 배열형태로 구조가 변경됨
ranknum = rank.find_all("span",attrs={"class":"num_rank"})
ranksubject = rank.find_all("span",attrs={"class":"txt_rank"})
w = 0
for bb in ranknum:
    print(bb.get_text())
    print(ranksubject[w].get_text())
    w+=1

# for cc in ranksubject:
#     print(cc.get_text())