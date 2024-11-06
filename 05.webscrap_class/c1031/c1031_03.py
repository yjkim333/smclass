# 오라클 db에서는 타입 결정되어
# 숫자형 문자타입과 숫자 와의 사칙연산 가능
# 파이썬에서 호출한 타입의 결과값이 어떻게 되는지 확인

import oracledb

def connects():
	user = 'ora_user'
	password = '1111'
	dsn = 'localhost:1521/xe'
	try : conn = oracledb.connect(user=user,password=password,dsn=dsn)
	except Exception as e: print("예외처리 :",e)
	return conn

conn = connects()
cursor = conn.cursor()
# chartable : number,number,varchar2,varchar2
sql = "select * from chartable"
cursor.execute(sql)
rows = cursor.fetchall()

for row in rows:
	# print(f"두 수의 합 : {row[1]+row[2]}")  ### 오라클에서는 계산이 되지만, 파이썬에서는 계산이 안됨.
	print(row)

print("검색 완료")

#-------------------------------------------

# chartable2 : number,number,number,number
sql = "select * from chartable2"
cursor.execute(sql)
rows = cursor.fetchall()

for row in rows:
	print(f"두 수의 합 : {row[1]+row[2]}") 
	print(row)

print("검색 완료")

print("ㅡ"*20)

#-------------------------------------------

sql = "select no,kor,to_char(kor_char,'00000000'),to_char(kor_mark,'999,999,999') from chartable2"
cursor.execute(sql)
rows = cursor.fetchall()
for row in rows:
	# print(f"두 수의 합 : {row[1]+row[2]}")  # 사칙연산 불가. str로 형변환해서 검색했기때문.
	print(row)



conn.close()