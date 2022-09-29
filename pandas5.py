#평균값, 최소, 최대값, 특정 행렬값(loc)로 출력
import pandas as pd
from idlelib.iomenu import encoding
#read_csv 로드 시 파일에 인코딩과 로드할 인코딩이 같아야 합니다.
 
data = pd.read_csv("area.csv", encoding="euc-kr")
# print(data)


#describe() : 평균값 및 카운터값, 최소값, 최대값 등 다양한 정보를 출력 산술 하는 함수 (문자열상태X)
#25~75% : 전체데이터에 대한 파트부분
# print(data.describe())
#loc는 특정 index값을 가져와서 해당 데이터만 출력
# print(data.loc[0])

#특정 index값 및 특정 컬럼값을 가져오는 데이터 출력
# print(data.loc[0]["경유"])

#두가지 지역을 비교하는 데이터
# print(data.loc[[0,1],"경유"])
print(data.loc[[0,1],["휘발유","경유"]])
