# BeautifulSoup에 대한 bs4를 사용하기 위해서는 라이브러리를 pom.xml처럼 파이썬에 등록을 시켜줘야 함
# 설치 형태 : cmd로 설치
'''
1. 파이썬이 설치된 경로확인
2. cmd로 해당 디렉토리로 이동
3. script 디렉토리
4. pip install beautifulsoup4
'''
# urlopen 함수 : 원하는 웹페이지 주소 접속 및 연결
from urllib.request import urlopen
# BeautifulSoup 함수 : 접속한 웹페이지에 대한 모든 문서파일을 파서하는 역할
from bs4 import BeautifulSoup
from idlelib.iomenu import encoding
# urlopen("웹주소")
html = urlopen("https://dnfasb.netlify.app/")
# 해당 url parser작업
object = BeautifulSoup(html,"html.parser")
# 해당 parser문자를 html로 저장
files = open("1.html","w",encoding="UTF-8")
print(object,file=files)
files.close()