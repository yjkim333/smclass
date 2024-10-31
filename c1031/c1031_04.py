### 입력한 달 뒤에 입사한 사원 출력

import oracledb

def connects():
	user = 'ora_user'
	password = '1111'
	dsn = 'localhost:1521/xe'
	try : conn = oracledb.connect(user=user,password=password,dsn=dsn)
	except Exception as e: print("예외처리 :",e)
	return conn


d_day = int(input("숫자를 입력하세요. >> "))
print(d_day)

conn = connects()
cursor = conn.cursor()
sql = "select emp_name,hire_date from employees where substr(hire_date,4,2) >= :d_day"
cursor.execute(sql,d_day=d_day)
rows = cursor.fetchall()

for row in rows:
	print(row)

print("완료")


