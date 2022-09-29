import matplotlib.pyplot as mpt
import mfont

data=[30,25,20,17,10,6]
text=["1일차","2일차","3일차","4일차","5일차","6일차"]
#기본형태
# transform=[0.2,0.1,0.1,0,0,0] #원그래프를 변형하기위한 배열
transform=[0.05]*6 # 원그래프 배열개수에 맞춰서 모두

#autopct: 데이터 1개를 %로 구분하여 출력하는 함수.
#'%.1f' : 1개의 데이터에 소수점 1자리, f:flot
#%%:그래프에 %를 출력하기위한 표시
#startangle : 원에대한 각도조절
'''
#원그래프 기본형태
mpt.pie(data,labels=text,autopct='%.1f%%', startangle=90)
'''
#원그래프 변형형태
#explode : 원그래프에 대한 조각을 별도로 분리한 형태
mpt.pie(data,labels=text, autopct='%.1f%%',explode=transform)
mpt.title("원그래프 테스트")
mpt.legend(loc=(1,0.5)) #loc(라벨 위치변경)
mpt.show()