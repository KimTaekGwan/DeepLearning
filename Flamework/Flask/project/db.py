# myproject/pybo/db.py
from pymysql import cursors, connect

db = connect(host='localhost',
                user='root',
                password='1234',
                database='checker',
                cursorclass=cursors.DictCursor)