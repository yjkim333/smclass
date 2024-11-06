# [프로그램 설치]
# 1. python 설치
# 윈도우 설정 - 고급시스템 설정 - 환경변수 - 시스템변수 - path - python 경로 추가
# C:\python\Scripts\
# C:\python\
# 윈도우r - cmd - python - python 버전나와야 함.

# 2. 라이브러리 설치
# pip install 
# pip install requests
# pip install beautifulsoup4
# pip install lxml

# 3. selenium 설치
# 크롬웹드라이버 다운
## chromedriver 크롬 드라이버 다운로드
# https://chromedriver.chromium.org/downloads

# 4. 오라클 라이브러리 설치
# python -m pip install oracledb

# C:\python\python.exe -m pip install --upgrade pip


import oracledb

# oracle 연결  -  외부 (프로그램) 연결 시에는 예외 처리!
# oracle 연결 => sql developer 연결됨
# sql developer 속성
# 연결했으면 끝에 close()!!
conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
# 연결이 잘 되었는지 확인
print(conn.version)

# sql 실행창 오픈
# cursor = conn.cursor()
# sql = "select count(*) from member"
# cursor.execute(sql)
# cursor.execute(sql) # -> cursor에 데이터 들어와있음


# fetchone() - 1개의 검색된 데이터 호출
# count1 = cursor.fetchone()
# print("개수 :",count1)

# 여러개의 검색된 데이터 호출
cursor = conn.cursor()
sql = "select * from member"
cursor.execute(sql)
rows = cursor.fetchall()

# for row in rows:
# 	print(row)

# print(rows[0][0],rows[0][1],rows[0][2],rows[0][3],rows[0][4],rows[0][5],rows[0][6],rows[0][7])

title = ['id','pw','이름','이메일','전화번호','성별','취미','날짜']
for t in title:
	print(f"{t:10}",end='\t')
print()
print("ㅡ"*60)

for row in rows:
	for j in range(len(title)):
		print(f"{row[j]:10}",end='\t')
	print()

conn.close()




