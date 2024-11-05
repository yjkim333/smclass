### 학생성적프로그램 ##
# students 테이블을 사용해서.
# 1. 학생성적입력
# students_seq,김유신 99 98 96 total avg rank sdate
# 2. 학생성적출력
# 3. 학생성적검색

import oracledb

s_title = ['번호','이름','국어','영어','수학','합계','평균','등수','등록일']

# db 연결 함수선언
def connects():
	user = 'ora_user'
	password = '1111'
	dsn = 'localhost:1521/xe'
	try: conn = oracledb.connect(user=user,password=password,dsn=dsn)
	except Exception as e : print("예외처리 :",e)
	return conn

while True:
	print()
	print("  [  학생 성적 프로그램  ]")
	print("1. 학생 성적 입력")
	print("2. 학생 성적 출력")
	print("3. 학생 성적 검색")
	print("4. 학생 성적 정렬")
	print("5. 학생 등수 처리")
	print("0. 프로그램 종료")
	choice = input("원하는 번호 입력 >> ")
	print()

	if choice == '1':
		# db 접속
		conn = connects()
		# sql = "select stu_seq.currval from dual"
		cursor = conn.cursor()
		# cursor.execute(sql)
		# row = cursor.fetchone()
		cursor.close()
		
		print("  [ 학생 성적 입력 ]")
		# no = row[0]
		name = input(f"학생 이름 입력 >> ")
		kor = int(input("국어점수 입력 >> "))
		eng = int(input("영어점수 입력 >> "))
		math = int(input("수학점수 입력 >> "))
		total = kor+eng+math
		avg = total/3
		s_list = [name,kor,eng,math,total,avg]
		# insert,update,delete 했을 경우 => conn.commit() 꼭 해야 반영됨!
		cursor = conn.cursor()
		sql = "insert into students values(stu_seq.nextval,:1,:2,:3,:4,:5,:6,0,sysdate)"
		cursor.execute(sql,s_list)
		# sql = "insert into students values(stu_seq.nextval,:name,:kor,:eng,:math,:kor+:eng+:math,(:kor+:eng+:math)/3,0,sysdate)"
		# cursor.execute(sql,name=name,kor=kor,eng=eng,math=math)
		conn.commit()
		conn.close()
		print("학생성적이 저장되었습니다.")
		print()

	elif choice == '2':
		print("  [ 학생 성적 출력 ]")
		# 학생 성적 출력
		conn = connects()
		cursor = conn.cursor()
		sql = "select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy.mm.dd') from students"
		cursor.execute(sql)
		rows = cursor.fetchall()
		if len(rows) < 1:
			print("데이터가 없습니다.")
			continue

		# s_title 출력
		for t in s_title:
			print(t,end='\t')
		print()
		print("ㅡ"*50)

		for row in rows:
			for i,r in enumerate(row):
				if i == 1:
					print(f"{r:12}",end='\t')
					continue
				print(r,end='\t')
			print()
		print()
		print("데이터 출력 완료")
		conn.close()

	elif choice == '3':
		print("  [ 학생 성적 검색 ]")
		print("1. 이름으로 검색")
		print("2. 합계순 검색")
		choice = input("원하는 번호 입력 >> ")
		if choice == '1':
			print()
			print("  [ 이름으로 검색 ]")
			search = input("찾고자 하는 이름 입력 >>")
			search = '%'+search+'%'
			
			# s_title 출력
			for t in s_title:
				print(t,end='\t')
			print()
			print("ㅡ"*50)

			# 학생 성적 출력
			conn = connects()
			cursor = conn.cursor()
			sql = "select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy.mm.dd') from students where name like :search"
			cursor.execute(sql,search=search)
			rows = cursor.fetchall()
			if len(rows) < 1:
				print("데이터가 없습니다.")
				continue
			for row in rows:
				for i,r in enumerate(row):
					if i == 1:
						print(f"{r:12}",end='\t')
						continue
					print(r,end='\t')
				print()
			print()
			print("데이터 출력 완료")
			conn.close()
		
	elif choice == '4':
		print("  [ 학생 성적 정렬 ]")
		print("1. 이름 순차정렬")
		print("2. 이름 역순정렬")
		print("3. 합계 순차정렬")
		print("4. 합계 역순정렬")
		choice = input("원하는 번호 입력 >> ")
		conn = connects()
		cursor = conn.cursor()
		if choice == '1':
			sql = "select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy.mm.dd') from students order by name"
			cursor.execute(sql)
			print("이름으로 순차정렬 되었습니다.")
			rows = cursor.fetchall()
			if len(rows) < 1:
				print("데이터가 없습니다.")
				continue
			# s_title 출력
			for t in s_title:
				print(t,end='\t')
			print()
			print("ㅡ"*50)

			for row in rows:
				for i,r in enumerate(row):
					if i == 1:
						print(f"{r:12}",end='\t')
						continue
					print(r,end='\t')
				print()
			print()
			print("데이터 출력 완료")
			conn.close()

		elif choice == '2':
			sql = "select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy.mm.dd') from students order by name desc"
			cursor.execute(sql)
			print("이름으로 역순정렬 되었습니다.")
			rows = cursor.fetchall()
			if len(rows) < 1:
				print("데이터가 없습니다.")
				continue
			# s_title 출력
			for t in s_title:
				print(t,end='\t')
			print()
			print("ㅡ"*50)

			for row in rows:
				for i,r in enumerate(row):
					if i == 1:
						print(f"{r:12}",end='\t')
						continue
					print(r,end='\t')
				print()
			print()
			print("데이터 출력 완료")
			conn.close()

		elif choice == '3':
			sql = "select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy.mm.dd') from students order by total"
			cursor.execute(sql)
			print("합계로 순차정렬 되었습니다.")
			rows = cursor.fetchall()
			if len(rows) < 1:
				print("데이터가 없습니다.")
				continue
			# s_title 출력
			for t in s_title:
				print(t,end='\t')
			print()
			print("ㅡ"*50)

			for row in rows:
				for i,r in enumerate(row):
					if i == 1:
						print(f"{r:12}",end='\t')
						continue
					print(r,end='\t')
				print()
			print()
			print("데이터 출력 완료")
			conn.close()

		elif choice == '4':
			sql = "select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy.mm.dd') from students order by total desc"
			cursor.execute(sql)
			print("합계로 역순정렬 되었습니다.")
			rows = cursor.fetchall()
			if len(rows) < 1:
				print("데이터가 없습니다.")
				continue
			# s_title 출력
			for t in s_title:
				print(t,end='\t')
			print()
			print("ㅡ"*50)

			for row in rows:
				for i,r in enumerate(row):
					if i == 1:
						print(f"{r:12}",end='\t')
						continue
					print(r,end='\t')
				print()
			print()
			print("데이터 출력 완료")
			conn.close()

		

	elif choice == '5':
		print("  [ 학생 등수 처리 ]")
		sql = "update students a set rank = (select ranks from(select no, rank() over(order by avg desc) ranks from students) b where a.no=b.no)"
		conn = connects()
		cursor = conn.cursor()
		cursor.execute(sql)
		conn.commit()
		print("등수처리가 완료되었습니다.")
		print()
		# --------------------------------------------------------------------------------------------
		sql = "select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy.mm.dd') from students"
		cursor.execute(sql)
		rows = cursor.fetchall()
		if len(rows) < 1:
			print("데이터가 없습니다.")
			continue

		# s_title 출력
		for t in s_title:
			print(t,end='\t')
		print()
		print("ㅡ"*50)

		# 학생 성적 출력
		for row in rows:
			for i,r in enumerate(row):
				if i == 1:
					print(f"{r:12}",end='\t')
					continue
				print(r,end='\t')
			print()
		print()
		print("데이터 출력 완료")
		conn.close()

	elif choice == '0':
		print("-- 프로그램 종료 --")
		break