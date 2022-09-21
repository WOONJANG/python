from bs4 import BeautifulSoup
from requests import *

url = "https://comic.naver.com/index"
result = get(url)
 # status 코드에 대한 문제사항 출력 None = 문제 없음
result.raise_for_status()
print(result.raise_for_status())

html = BeautifulSoup(result.text,"lxml") #lxml(자동파서) - 설치 필요
cartoon = html.find("ol",attrs={"id":"realTimeRankFavorite"})
atag = cartoon.find_all("a")
for aa in atag:
    print(aa.get_text())
# print(cartoon.a.get_text())