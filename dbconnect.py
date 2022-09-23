from sqlite3 import * #pip install pysqlite3
from MySQLdb import * #database에 연결

# mysql 연결에 필요한 pip
# *필수
# * pip install dbconnect
# * pip install pysqlite3
# * pip install mysqlclient
# pip install
# pip install
# pip install
# pip install
# pip install


connect = connect(
    user = "jangwoon0518", 
    passwd = "boyun981124@",
    host = "umj7-009.cafe24.com",
    db = "jangwoon0518",
    charset="utf8" #서버 database의 \status 명령어로 확인.
    )