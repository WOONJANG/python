import matplotlib.pyplot as mpt
import mfont

x=[10,20,30,40]
y=[15,25,35,45]

mpt.plot(x,y,label="테스트 그래프", color="red", marker="o")
mpt.legend()
#enumerate : 그래프 값 포인트 부분에 배열의 값을 가져와서 text로 변환 함수 (수동. 반복문사용해 값을 가져와야함)
for idx,txt in enumerate(x): # 두값을 다 받지는못함. x, y축중 1곳만
    #idx(배열에 index, 0부터), txt(배열값)
    mpt.text(x[idx],y[idx]+0.7,txt,fontsize=16, ha="right", color="blue") #실제 배열값이 변하는것이 아니고 폰트의 위치가 변경
    #ha: left,right, center 반대방향
    #x[idx] : x배열값 (위치)
    #y[idx]+0.5 : y배열값 (위치) 에 글자를 0.5만큼 이동
 
mpt.show()
