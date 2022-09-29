# Database 연결
from sqlite3 import *
from MySQLdb import *

con = connect(
    user = "jangwoon0518",
    passwd = "boyun981124",
    host = "",
    db = "",
    charset ="utf8"  # MySQL 콘솔에서 \status 입력
)

cur = connect.cursor()
sql = "select * from TABLENAME"
cur.execute(sql)

# select에서 fetchall 함수를 이용하여 loop가 작동 되도록함
for z in cur.fetchall():
    print(z)

delsql = "delete from TABLENAME where 고유컬럼='고유값'"
cur.execute(delsql)

# insert, update

insertsql = "insert into TABLENAME values ('0',,,,)"
cur.execute(insertsql)
con.commit() # insert 할때는 commit 필수. 안하면 들어갔다 바로 지워짐