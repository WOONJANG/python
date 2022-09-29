import pandas as pd
from sqlite3 import *
from dbconnect import *

sqlin = connect.cursor()

sql="select * from test3"
#read_sql_query, read_sql (pandas전용 DB연결 형태)
#read_sql_query("SQL문법", "DB접속정보")
data=pd.read_sql_query(sql,connect)

#삭제형태로 가져오는 컬럼형태
# data = data.drop(columns=["midx","mpw","mtel"]) 

#저장할 컬럼만 가져오는 형태
data=data[["mid","mnm","mage"]]
data=pd.DataFrame(data)
data=data.rename(columns={"mid":"아이디","mnm":"고객명","mage":"나이"})
print(data)
#r : 기존 데이터를 삭제하고 새롭게 저장할 수 있도록 사용하는 속성값. 덮어쓰기    
data.to_csv(r"test3.csv", encoding="euc-kr") 