#pysqlite3, pysqlite , sqlite3
from sqlite3 import * #pip install pysqlite3
from dbconnect import *

cur = connect.cursor() #명령어를 입력시키기 위한 대기상태 .
cur.execute("select * from test3") #execute : 콘솔상태에 문자값을 입력
for a in cur.fetchall(): #fetchall(): select에 대한 data를 문자열 형태로 가져옴(fetch-php언어) 
    print(a)
    
# cur.execute("insert into test3 values('0','song','aaa111','송아지','01011112222','25')")

#java에서 ?를 이용하여 sql에 사용하는statement와 비슷한 형태구조를 가집니다.
sql="insert into test3 values('0',%s,%s,%s,%s,%s)" 

#with를 이용하여 여러개의 데이터를 한꺼번에 저장, 수정, 삭제를 할 수 있습니다
with connect:
    cur.execute(sql,('red','red1234','레드사용자','01022223333','55'))
    cur.execute(sql,('blue','blue1234','블루사용자','01022227777','50'))
    cur.execute(sql,('orange','orange1234','오렌지사용자','01033339988','45'))
    connect.commit() 

#commit을 사용해야 하는 이유는 insert후 delete를 바로 해버리는 파이썬 특유의 행동부분입니다.

    
'''
con = connect("./test.sql")
create = con.cursor()
create.execute("create table test(idx int(4) not null, name varchar(200) not null ")
insert = con.cursor()
insert.execute("insert into test values('0','hong');")
'''