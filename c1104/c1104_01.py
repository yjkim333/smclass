### 학생성적프로그램 ##
# students 테이블을 사용해서.
# 1. 학생성적입력
# students_seq,김유신 99 98 96 total avg rank sdate
# 2. 학생성적출력
# 3. 학생성적검색

import oracledb

# db 연결 함수선언
def connects():
	user = 'ora_user'
	password = '1111'
	dsn = 'localhost:1521:xe'
	try: conn = oracledb.connect(user=user,password=password,dsn=dsn)
	except Exception as e : print("예외처리 :",e)
	return conn

while True:
	print()
	print("  [  학생 성적 프로그램  ]")
	print("1. 학생 성적 입력")
	print("2. 학생 성적 출력")
	print("3. 학생 성적 검색")
	print("0. 프로그램 종료")
	choice = input("원하는 번호 입력 >> ")
	print()

	if choice == '1':
		# db 접속
		conn = connects()
		sql = "select stu_seq.currval from dual"
		cursor = conn.cursor()
		cursor.execute(sql)
		row = cursor.fetchone()
		cursor.close()
		
		print("  [ 학생 성적 입력 ]")
		no = row[0]
		name = input(f"{no}번 학생 이름 입력 >> ")
		kor = int(input("국어점수 입력 >> "))
		eng = int(input("영어점수 입력 >> "))
		math = int(input("수학점수 입력 >> "))

		conn.close()		

	elif choice == '2':
		pass

	elif choice == '3':
		pass

	elif choice == '0':
		print("-- 프로그램 종료 --")
		break