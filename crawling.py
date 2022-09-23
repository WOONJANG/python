from tkinter import *
from bs4 import BeautifulSoup
from idlelib.iomenu import encoding
from urllib.request import urlopen
from random import *
from crawling_def import *
from _functools import partial

# GUI 생성
root = Tk()
root.title("쿠팡-펜션 크롤링")
root.geometry("640x100")
root.configure(background="black")
root.resizable(False,False)

# Label 생성
msg = Label(root, text="쿠팡 크롤링 주소 형식")
msg.pack()
msg2 = Label(root, text="예시) http://browse.auction.co.kr/search?keyword=팬션예약")
msg2.pack()

# 입력 생성
src = Text(root, width=50, height=3) # 크롤링 주소 입력 창
src.insert(END, "") # 사용자가 입력한 주소값을 전달받기 위한 코드
src.place(x=50, y=50) # place는 원하는 위치에 오브젝트를 설정할 수 있음

def textload():
    # 사용자가 입력한 값을 변수로 변환
    url = src.get("1.0",END)
    # crawling_def.py로 함수 전달
    crawling_btn_def(url)


btn = Button(root, text="크롤링", width=10, height=2, background="green", command=textload)
btn.place(x=450, y=50)


# # 버튼 생성 (import)
# btn = Button(root, text="크롤링", width=10, height=2, background="green", command=crawling_btn_def)
# btn.place(x=450, y=50)

# # 버튼 생성 (partial)
# partial(함수명,"인자값")
# btn = Button(root, text="크롤링", width=10, height=2, background="green", command=partial(crawling_btn_def, "홍길동"))
# btn.place(x=450, y=50)

# # 버튼 생성 (lambda)
# btn = Button(root, text="크롤링", width=10, height=2, background="green", command=lambda:crawling_btn_def("이순신"))
# btn.place(x=450, y=50)

# # 일반적인 방식
# import crawling_def as craw
# btn = Button(root, width=10, height=2, background="green", text="크롤링 시작", command=craw.crawling_btn_def("홍길동"))
# btn.place(x=450, y=50)

# 닫기 버튼 함수
def close_btn_def():
    root.destroy()
# 닫기 버튼 생성
close_btn = Button(root, text="닫기", width=10, height=2, background="red", command=close_btn_def)
close_btn.place(x=550, y=50)

# GUI 실행
root.mainloop()
