import pandas as pd
from idlelib.iomenu import encoding
data = pd.read_csv("area.csv", encoding="euc-kr")

#출력 조건문 True/False로 출력 (pandas전용. 숫자 위주로 사용)
# print(data["휘발유"] <= 1700) 

#변수에 조건을 적용하고 해당 조건을 배열키로 적용하여 필터링하게 됩니다.
filter = (data["휘발유"] <= 1700) 
# print(data[filter])  #휘발유 1700이하만 출력
# print(data[~filter]) #휘발유 1700이상만 출력 . ~(반대)  

# &, | 를 이용하여 두 조건이 만족하는 사항에서 데이터를 출력
filter2 = data.loc[(data["휘발유"] <= 1700)&(data["지역"] == "대구")]
print(filter2)


filter3 = data.loc[(data["휘발유"] <= 1700)&(data["경유"] <= 1800)]
print(filter3)