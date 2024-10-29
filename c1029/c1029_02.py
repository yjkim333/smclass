## 학생 성적 출력을 하시오 ##
import oracledb

conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')

cursor = conn.cursor()

sql = "select * from students"
cursor.execute(sql)

rows = cursor.fetchall()

title = ['번호','이름','국어','영어','수학','합계','평균','등수','등록일']
for i,t in enumerate(title):
	if i == 1:
			print(f"{t:10}",end='\t')
			continue
	print(t,end='\t')
print()
print("ㅡ"*50)

for row in rows:
	for i,r in enumerate(row):
		if i == 1:
			print(f"{r:10}",end='\t')
			continue
		if i == 6:
			print(f"{r:.2f}",end='\t')
			continue
		if i == 8:
			print(r.strftime("%Y/%m/%d"))
			continue
		print(r,end='\t')
print()

conn.close()