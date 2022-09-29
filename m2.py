#그래프에 대한 ticks 및 x,y축에 대한 표현방식
import matplotlib.pyplot as mpt
import mfont
#x축,y축의 배열의 개수는 같아야함.(인덱스 개수가 다르면 값이 출력되지 않음.) 
#값이 없을경우엔 0 으로하게되면 그래프가 확 떨어지게되므로 '' 공백으로 표시하거나 '최고점'으로 표시
#x축, y축 중 데이터에대한 숫자값은 무조건 있어야함.
#그래프로 y축에 한글, x축에 숫자로 표현 하거나 또는 반대로 x축에 한글, y축에 숫자로 표현해야함.
x=[10,15,17]
y=['서울','인천','대구']
'''
mpt.plot(x,y) #(x축값, y축값)
mpt.xlabel("X축", color='blue', loc='left') #left, center, right . default=center
mpt.ylabel("Y축", color='#00FFcc', loc='top')#top, center, bottom. default=center
mpt.show()
'''
'''
#본데이터
xx=[3,7,9]
yy=[5,9,12]
mpt.plot(xx,yy) #본 데이터는 무조건 개수가 같아야함
#ticks로 라벨 출력하는 부분
x1=[1,2,3]
y1=[3,6,9,12] 
#xticks, yticks :라벨을 직접 꾸미고 싶을때 사용
mpt.xticks(x1) #x축에 대한 라벨 출력형태
mpt.yticks(y1) #y축에 대한 라벨 출력형태
mpt.show()
'''

#응용부분
data1=[10,20,30,40]
data2=[10,20,30,40]
#ticks 본데이터에서 라벨을 꾸며주는 형태
mpt.xticks(data1, ['1월','2월','3월','4월'])
mpt.yticks(data2,[15,25,35,45]) #yticks(ticks,label)
mpt.plot(data1,data2) #본데이터 출력
mpt.show()
