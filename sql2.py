from sqlite3 import *
from dbconnect import *
from random import *
# [25,26,27]
'''
#update
for a in range(25,28): #sql에 index고유값에 대한 범위를 선정
    cur=connect.cursor() # 해당 index값을 모두 변경이 되도록 반복 시킴
    sql = "update test3 set mpw='pass123456' where midx='"+str(a)+"'"
    #%s사용시 sql문법 전체를 %s로 적용해야만 정상적으로 반영이 됨 
    cur.execute(sql)
    connect.commit()

#delete
cur = connect.cursor()
for b in range(24,28):
    sql="delete from test3 where midx='"+str(b)+"'"
    cur.execute(sql)
    connect.commit()
'''
# 신규 테이블 생성
cur = connect.cursor()
sql = "create table shoping(sidx int(4) not null AUTO_INCREMENT, sname varchar(200) not null, primary key(sidx))"
cur.execute(sql)
connect.commit()
