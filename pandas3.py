#csv 저장
import pandas as pd
data = {
    "area" : ['강남구','강동구','강북구','강서구'],
    "gasoline" : [1947,1812,1677,1721],
    "diesel" : [1947,1918,1809,1855],
    "ev" : [173.8,170,158.4,166]
    }
#csv 생성시 DataFrame을 무조건 선언 후 저장합니다. 
pr = pd.DataFrame(data)
pr.index.name="유가리스트"
#to_csv 는 csv file로 저장하는 함수 (pandas 전용 문법) 
pr.to_csv('opinet.csv', encoding='euc-kr')
#encoding : csv 파일은 기본으로 euc-kr을 사용

data2 =pd.read_csv('opinet.csv', encoding='euc-kr',skiprows=1) #skiprows : 1줄 스킵하고 출력
print(data2)