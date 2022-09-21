from bs4 import BeautifulSoup
from os import *
from requests import *
from idlelib.iomenu import encoding
from urllib.request import urlopen
from tkinter import *

# GUI 기초
root = Tk()
root.title("Webpage Crawling")
root.geometry("500x100")
root.resizable(False, False)


url = Text(root, width=400, height=2)
url.pack()
url.insert(END, "URL을 입력하세요.")


def pageload():
    urladdr = url.get(0.1, END)
    check = get(urladdr)
    if check.status_code == codes.ok:
        html = urlopen(urladdr)
        object = BeautifulSoup(html, "html.parser")
        import io
        files = io.open("test.html", "w", encoding="UTF-8")
        print(object, file=files)
        files.close()
        print("완료 되었다. 생성")
    else:
        print("올바른 웹페이지가 아닙니다.")


btn = Button(root, text="웹크롤링", command=pageload)
btn.pack()


# GUI 생성
root.mainloop()
