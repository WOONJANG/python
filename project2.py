from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from asyncio.tasks import sleep
from selenium.webdriver.common.by import By

#자동로그인, 자동 페이지 이동, 자동검색 ...

bw=webdriver.Chrome(ChromeDriverManager().install())
bw.get("https://www.naver.com") #페이지이동 - 크롬 브라우저에서 자동으로 페이지 이동

#https://search.naver.com/search.naver?query= : 네이버
#https://search.daum.net/search?q= : 다음
#https://google.com/search?q= : 구글

# gopage=bw.find_element("link_login")

#검색어 홍길동을 자동으로 네이버에 검색
search = "홍길동"
bw.get("http://naver.com?query="+search)
bw.get("http://search.naver.com?query="+search)
bw.get("http://search.naver.com/search.naver?query="+search)

sleep(10) #10초 딜레이

bw.get("http://search.naver.com/search.naver?query="+search)

#검색어를 이순신으로 변경해서 네이버에 검색->네이버메인->검색->메인->네이버검색->다음검색
search = "이순신" 
bw.get("http://search.naver.com/search.naver?query="+search)
bw.get("http://naver.com")
bw.get("http://search.naver.com/search.naver?query="+search)
bw.get("http://naver.com")
bw.get("http://search.naver.com/search.naver?query="+search)
bw.get("http://search.daum.net/search?q="+search)