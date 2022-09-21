from tkinter import *


root = Tk()
root.title("연습 프로그램")
root.geometry("500x500")
root.resizable(False, False)
# 텍스트필드
txt = Entry(root, width=60) # Entry : 한줄짜리 input (width (O) height (X))  / Text : insert와 함께 사용하여 적용해야함 (width (O) height (O))
txt.pack()
txt2 = Text(root, width=60, height=2)
txt2.pack()
# Text : 1.0 => 1 = "첫번째 행" 0 = "열의 첫번째 위치", END = "마지막 단어 까지"
txt2.insert(END, "")
# 버튼 함수
def aaa():
    url = txt.get()
    url2 = txt2.get(0.1, END)
    print(url)
    print(url2)
# 버튼 생성
btn1 = Button(root, width=5, height=2, text="크롤링", command=aaa)
btn1.pack()


root.mainloop()