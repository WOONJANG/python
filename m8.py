#막대그래프+pandas
import pandas as pd
import matplotlib.pyplot as mpt
import mfont

data=pd.read_csv("area.csv", encoding="euc-kr")
#높은 순위 데이터부터 그래프에 반영을 하는것을 추천
'''
mpt.bar(data['지역'],data['경유'])
mpt.bar(data['지역'],data['휘발유'])
mpt.bar(data['지역'],data['LPG'])
'''

#데이터를 지속적으로 누적시켜서 출력하는 형태
mpt.bar(data['지역'],data['경유'], label='경유')
mpt.bar(data['지역'],data['휘발유'], label='휘발유')
mpt.bar(data['지역'],data['LPG'],label='LPG')
#bottom = 그래프를 출력할 때 해당 데이터와 bottom으로 사용 할 데이터가 누적되어 출력됨.
mpt.bar(data['지역'],data['경유'],bottom=data['LPG']+data['휘발유'],label='총금액')
#bottom을 2번쓰려면 데이터를 합쳐서 사용
mpt.legend()
mpt.show()

