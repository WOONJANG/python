from bs4 import BeautifulSoup #파싱과 파서를 하기위해서 모듈사용
# 운영체제가 기본으로 제공하는 모듈
from os import *
# htmlcode = BeautifulSoup("<div><span>테스트1</span></div>")
# soup = BeautifulSoup("<span><b><i>테스트2</i></b></span>")
# print(htmlcode.prettify())
# print(soup.prettify())

dictory = "html"
print(getcwd()) # 현재 파일 경로
mkdir(dictory) # mkdir 디렉토리만들기