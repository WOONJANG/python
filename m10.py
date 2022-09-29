#원그래프 응용편
import pandas as pd
import matplotlib.pyplot as mpt
import mfont
data=[30,25,20,17,10,6]
text=["1일차","2일차","3일차","4일차","5일차","6일차"]
w={'width':0.5} # 0~1까지 width. 원에대한 두께 기본값 1. 꾸미기위한 속성값임!!
#wedgeprops:원안의 빈공간에 대한 크기를 반영하는 함수 
'''
mpt.pie(data,labels=text, autopct="%.1f%%", wedgeprops=w)
mpt.legend(loc=(1,0.5))
'''
csv=pd.read_csv("movie.csv",encoding="euc-kr")
#groupby : 해당 컬럼명으로 같은 데이터값을 카운팅하여 설정
gp=csv.groupby("영화관")
#gp.size() : 해당 파트별로 그룹개수를 출력
#data2 는 배열로 각 파트별 개수를 생성
data2=[gp.size()['cgv'],gp.size()['megabox']]
text2=["CGV","MEGABOX"]
mpt.pie(data2,labels=text2)
mpt.title("영화관 상영 개수 형태")
mpt.show()

#원그래프는 그룹화가 필요함
#막대 선 그래프는 별도의 데이터 구성
#select * from table group by~~~




