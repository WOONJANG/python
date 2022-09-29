#막대그래프 (bar, barh)
import matplotlib.pyplot as mpt
import mfont

person = ["이순신","강감찬","유관순"]
product=[46,10,86]
barcolor=["red","green","orange"] #배경색상

#막대그래프
'''
bar=mpt.bar(person,product,color=barcolor)
mpt.ylim(5,100) #5단위로 끊어서 최대 100까지 #ylim : 범위와 단위를 정할 때 사용. lim=limit의 줄임말
#ylim(단위,최대값)-y축에 limit
# mpt.xticks(rotation=45)
#rotation:출력 데이터 텍스트를 45도로 기울게 설정
for idx,txt in enumerate(bar): #bar(문자와 숫자 겸용)
    #txt.get_height() : 막대그래프의 세로값을 계산해서 출력
    mpt.text(idx, txt.get_height(), product[idx]) 
mpt.show()

'''
#가로그래프
bar=mpt.barh(person,product,color=barcolor)
mpt.xlim(0,100)
#set_hatch : 배경에 간단한 도형 출력
# bar[0].set_hatch('\\') #역슬래시는 \\ 두개 사용할것
# bar[1].set_hatch('*')
# bar[2].set_hatch('x')
for idx,txt in enumerate(bar): 
    #주의점 barh 사용시 x축을 기준으로 get_width사용
    mpt.text(txt.get_width()+5,idx,product[idx])

mpt.show()