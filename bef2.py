from bs4 import BeautifulSoup
from os import *
from requests import * # requests : 해당 url 접속 정보를 확인 (lib 설치해야함)

url = get("http://www.naver.com/")
print("응답코드 : ", url.status_code) # 200 : 정상

if url.status_code == codes.ok:
    print(url.text)
    print("정상적인 웹사이트 페이지입니다.")
else:
    print("보안 또는 코드에 문제가 있는 웹 사이트입니다.")
