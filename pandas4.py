#txt 저장
import pandas as pd
data = {
    "area" : ['강남구','강동구','강북구','강서구'],
    "gasoline" : [1947,1812,1677,1721],
    "diesel" : [1947,1918,1809,1855],
    "ev" : [173.8,170,158.4,166]
    }

pr=pd.DataFrame(data)
#pr.to_csv("data.txt", encoding="euc-kr")
#txt파일로 저장 , 를 기준으로 저장됨 index=False를 사용하면 index번호 삭제 처리
# pr.to_csv("data.txt", encoding="euc-kr",index=False)
# pr.to_csv("data.xls", encoding="euc-kr",index=False)

#pandas에서 excel로 저장
#pip install xlwt
#pip install openpyxl
pr.to_excel("data.xlsx", index = False)

