#오름차순, 내림차순, 데이터수정(임시수정)
#pandas버전확인
# print(pd.__version__)
import pandas as pd
from idlelib.iomenu import encoding
data = pd.read_csv("area.csv", encoding="euc-kr")

#오름차순 정렬 (sort_values)
# print(data.sort_values("휘발유")) 

#내림차순 정렬(sort_values(ascending=False))
# print(data.sort_values("휘발유",ascending=False))
# print(data["경유"].sort_values(ascending=False))

#index 숫자값으로 내림차순
# print(data.sort_index(ascending=False))

#두개 값을 내림차순 (2가지 키값을 비교)
# print(data.sort_values(["휘발유","경유","LPG"],ascending=False))

#------------------------------------#
#해당 column에 있는 문자값만 변경
# print(data["지역"].replace({"서울":"서울특별시","인천":"인천광역시","대전":"대전광역시"}))

#모든 데이터값 중 해당 문자값 변경
# print(data.replace({"서울":"서울특별시","인천":"인천광역시","대전":"대전광역시"}))
#------------------------------------#
#기타문법(영어만 적용. 대소문자 변경)
# print(data["지역"].str.upper()) #소문자를 모두 대문자로 변경
# print(data["지역"].str.lower()) #대문자를 모두 소문자로 변경
#------------------------------------#
#컬럼값 추가하여 +,-,*,/ 등 산술연산으로 추가하는 방식
data['평균값'] = (data['휘발유']+data['경유']+data['LPG']) / 3
# print(data)

#해당 컬럼값을 숨김
print(data.drop(columns=["LPG"]))

#index 해당 번호값을 숨김
print(data.drop(index=7))
