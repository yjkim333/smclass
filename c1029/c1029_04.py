# employees 테이블에서 이름이 a가 포함되어 있는 모든 것 출력

import oracledb

# db 연동 함수 선언
def connections():
	try:
		conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')
		print("db 연결 :",conn.version)
	except Exception as e: print("예외발생 :",e)
	return conn

# db 연동 함수 호출
conn = connections()

cursor = conn.cursor()

# sql = "select * from employees where emp_name like '%a%'"
# cursor.execute(sql)


# 월급이 4000-8000 사이의 사원을 모두 출력하시오
# sql = "select employee_id,emp_name,salary from employees where salary>=4000 and salary <=8000"
# cursor.execute(sql)

# 월급 범위를 입력받아 사이의 사원을 모두 출력하시오
num1 = input("숫자1")
num2 = input("숫자2")
sql = "select employee_id,emp_name,salary from employees where salary>=:num1 and salary <=:num2 order by salary"
cursor.execute(sql,num1=num1,num2=num2)




### search 값 입력 받아 검색
# search = input("검색할 이름 입력 >> ")
# search = '%'+search+'%'
# sql = "select * from employees where emp_name like :search"
# cursor.execute(sql,search=search)


# 키워드 검색
# search = input("검색할 번호 입력 >> ")
# sql = "select * from employees where employee_id >= :search"
# cursor.execute(sql,search=search)

# 번호순서
# search = input("검색할 번호 입력 >> ")
# sql = "select * from employees where employee_id >= :1"
# cursor.execute(sql,[search])


# sql = f"select * from employees where emp_name like '%{search}%'"
# cursor.execute(sql)

rows = cursor.fetchall()
# for row in rows:
# 	for i,r in enumerate(row):
# 		if i == 1:
# 			print(f"{r:18}",end='\t')
# 			continue
# 		if i == 2:
# 			print(f"{r:10}",end='\t')
# 			continue
# 		if i == 3:
# 			print(f"{r:20}",end='\t')
# 			continue
# 		print(r,end='\t')
# 	print()



# 딕셔너리타입으로 저장
title = ['employee_id','emp_name','salary']
a_list = [dict(zip(title,row)) for row in rows]
print(a_list)

conn.close()