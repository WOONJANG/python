from tkinter import *
def abc():
    print("test print")

root = Tk()
root.title("연습 프로그램") # 프로그램 타이틀 이름
root.geometry("500x500") # 가로크기 x 세로크기
root.resizable(True, False) # 가로크기조절여부, 세로크기조절여부 (True : 가능, False : 불가능)
btn1 = Button(root, text="클릭", command=abc) # command : 클릭시 함수 호출
btn2 = Button(root, width=10, height=2, text="클릭2")
# width=10 == 100px height=2 == 20px
btn1.pack()
btn2.pack()
root.mainloop() # GUI 프로그램 실행
