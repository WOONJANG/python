from urllib import *
from requests import *

def download(url):
    with open("tmon.html","wb") as file:
        response = get(url)
        file.write(response.content)


url = "http://browse.auction.co.kr/search?keyword=팬션예약"
download(url)