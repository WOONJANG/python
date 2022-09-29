#함수 이용하기
import pandas as pd
from idlelib.iomenu import encoding
data = pd.read_csv("area.csv", encoding="euc-kr")

#add_liter return 함수
def add_liter(z):
    return str(z) +"L"

#data["휘발유"] = type은 Object임
#apply함수 : 해당 객체를 변환하여 반환하는 함수(return)
# data["휘발유"]=data["휘발유"].apply(add_liter)
# print(data["휘발유"])

#해당 함수에 조건문을 적용하여 값을 변동하는 형태
def add_literck(k):
    if k>1700:
        return str(k)+"L"
    return str(k)

data["휘발유"] = data["휘발유"].apply(add_literck)
print(data["휘발유"])
