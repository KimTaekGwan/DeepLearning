# myproject/pybo 에서 터미널을 실행하고 아래 내용을 입력
from db import db
# from datetime import dateimte

cursor = db.cursor()
for i in range(2,301):
	sql = f"insert into FileInfo (ID) values ('{i}')"
	cursor.execute(sql)

db.commit();
