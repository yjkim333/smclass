import oracledb

### sql developer 실행 ###  !끝나면 종료!
# user='ora_user',password='1111',dsn='localhost:1521/xe' = 오라클 속성
conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')

### sql 창 열림(ora_user 접속 - 창 열림) ###
cursor = conn.cursor()

# sql 작성 & 실행
sql = "select * from students"
cursor.execute(sql)

# 데이터 vs로 가져오기 - fetchone() - 1개 가져오기, fetchmany() - 숫자만큼 가져오기, fetchall() - 모든 데이터 가져오기
rows = cursor.fetchall()
titles = ['번호','이름','국어','영어','수학','합계','평균','등수','입력일']
for title in titles:
	print(title,end='\t')
print()
print('ㅡ'*55)


for row in rows:
	for i,r in enumerate(row):
		if i == 1:
			print(f"{r:10}",end='\t')
			continue
		if i == 6:
			print(f"{r:.2f}",end='\t')
			continue
		if i == 8:
			# strftime() - 날짜포맷 함수 : $Y ->2024, %y ->24
			print(r.strftime("%Y/%m/%d"),end='\t')
			continue
		print(r,end='\t')
	print()








# 종료
conn.close()