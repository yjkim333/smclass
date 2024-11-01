### 학생성적프로그램 ##
# students 테이블을 사용해서.
# 1. 학생성적입력
# students_seq,김유신 99 98 96 total avg rank sdate
# 2. 학생성적출력
# 3. 학생성적검색


import oracledb
import datetime
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수','등록일']

## db 연결 함수 선언 ##
def connects():
	user = 'ora_user'
	password = '1111'
	dsn = 'localhost:1521/xe'
	try: conn = oracledb.connect(user=user,password=password,dsn=dsn)
	except Exception as e: print("예외발생 :",e)
	return conn

while True:
	print()
	print("    [   학생 성적 프로그램   ]")
	print()
	print("1. 학생 성적 입력")
	print("2. 학생 성적 출력")
	print("3. 학생 성적 검색")
	print("0. 프로그램 종료")
	print()
	choice = input("원하는 번호 입력 >> ")

	if choice == '1':
		print("   [  학생 성적 입력  ]")
		name = input("1) 학생 이름 입력 >> ")
		kor = int(input("2) 국어 성적 입력 >> "))
		eng = int(input("3) 영어 성적 입력 >> "))
		math = int(input("3) 수학 성적 입력 >> "))
		total = kor+eng+math
		avg = (kor+eng+math)/3
		rank = 0
		# sdate = datetime.datetime.now()
		s_list = [name,kor,eng,math,total,avg,rank]
		print(s_list)

		# db 연결
		conn = connects()
		cursor = conn.cursor()
		sql = "insert into students values(stu_seq.nextval,:1,:2,:3,:4,:5,:6,:7,sysdate)"
		cursor.execute(sql,s_list)
		conn.commit()
		conn.close()


	elif choice == '2':
		print("   [  학생 성적 출력  ]")
		print()
		# 상단타이틀
		for i,s in enumerate(s_title):
			if i == 1 : 
					print(f"{s:12}",end='\t')
					continue
			if i == 6 : 
					print(f"{s:5}",end='\t')
					continue
			print(s,end='\t')
		print()
		print("ㅡ"*45)

		# db 연결
		conn = connects()
		cursor = conn.cursor()
		sql = "select * from students"
		cursor.execute(sql)
		rows = cursor.fetchall()
		for row in rows:
			for i,r in enumerate(row):
				if i == 1 : 
					print(f"{r:12}",end='\t')
					continue
				if i == 6 :
					print(f"{r:5.2f}",end='\t')
					continue
				if i == 8 :
					print(f"{r.strftime('%y-%m-%d')}")
					continue
				print(r,end='\t')
		print()
		conn.close()

	elif choice == '3':
		print("   [  학생 성적 검색  ]")
		print()
		search = input("검색할 학생 이름 입력 >> ")
		print()
		# 상단타이틀
		for i,s in enumerate(s_title):
			if i == 1 : 
					print(f"{s:12}",end='\t')
					continue
			if i == 6 : 
					print(f"{s:5}",end='\t')
					continue
			print(s,end='\t')
		print()
		print("ㅡ"*45)		
		# db 연결
		conn = connects()
		cursor = conn.cursor()
		sql = "select * from students where name = :name"
		cursor.execute(sql,name=search)
		rows = cursor.fetchall()
		for row in rows:
			for i,r in enumerate(row):
				if i == 1 : 
					print(f"{r:12}",end='\t')
					continue
				if i == 6 :
					print(f"{r:5.2f}",end='\t')
					continue
				if i == 8 :
					print(f"{r.strftime('%y-%m-%d')}")
					continue
				print(r,end='\t')
		print()
		conn.close()


	elif choice == '0':
		print("--- 프로그램 종료 ---")
		break
