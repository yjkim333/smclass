students = []
no =1
s_title = ['번호','이름','국어','영어','수학','총점','평균','등수'] #전역변수

# 학생성적프로그램
while True:
	print("                        [학생 성적 프로그램]  ")
	print("ㅡ"*33)
	print("1. 학생 성적 입력")
	print("2. 학생 성적 출력")
	print("3. 학생 성적 수정")
	print("4. 학생 성적 검색")
	print("5. 학생 성적 삭제")
	print("6. 등수 처리")
	print("0. 프로그램 종료")
	print("ㅡ"*33)
	choice = input("항목번호를 입력해주세요. (종료 -> 0)")
	
	if choice == '1':
		print("[ 학생 성적 입력 ]")
		while True:
			name = input(f"{no}번째 학생 이름 입력 (메뉴로 이동 -> 0)")
			if name == '0':
				print("---메뉴로 이동합니다.---")
				break
			kor = int(input("국어점수 입력"))
			eng = int(input("영어점수 입력"))
			math = int(input("수학점수 입력"))
			total = kor + eng + math
			avg = total/3
			rank = 0
			print(f"번호 :{no} 이름 :{name} 국어점수 :{kor} 영어점수 :{eng} 수학점수 :{math} 총점 :{total} 평균 :{avg} 등수 :{rank} ")
			s = [no,name,kor,eng,math,total,avg,rank]
			students.append(s)
			no += 1

	elif choice == '2':
		print("[ 학생 성적 출력 ]")
		s_title = ['번호','이름','국어','영어','수학','총점','평균','등수']
		# 상단제목
		for st in s_title:
			print(st,end='\t')
		print()
		print("ㅡ"*32)

		# 성적 출력
		for s in students:
			print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}")
			print()

	elif choice == '3':
		print("[ 학생 성적 수정 ]")
		#홍길동,유관순,이순신
		# 유관순학생성적 수정 -> 1)유관순 찾기(검색)
		name = input("수정하고자 하는 학생 이름 검색 >>")
		count = 0
		# students에 10명이 있다고 가정
		for s in students:
			if s[1] == name:
				print(f"{name}학생을 찾았습니다.")
				print("[ 과목선택 ]")
				print("1. 국어점수")
				print("2. 영어점수")
				print("3. 수학점수")
				print("0. 성적수정 취소")
				choice = int(input("항목번호 입력>>"))
				if choice == 1:
					print("현재 국어점수 : ",s[2])
					s[2] = int(input("변경할 점수 입력>>"))
				elif choice == 2:
					print("현재 영어점수 : ",s[3])
					s[3] = int(input("변경할 점수 입력>>"))
				elif choice == 3:
					print("현재 수학점수 : ",s[4])
					s[4] = int(input("변경할 점수 입력>>"))
				elif choice == 0:
					print("성적 수정을 취소합니다.")
					print()
					count = 1
				
				if choice != 0:
					s[5] = s[2]+s[3]+s[4] #합계 변경
					s[6] = s[5]/3					#평균 변경
					print(f"{name} 학생의 성적이 변경되었습니다.")
					count = 1

		# 검색결과 없을 때(for문 빠져나와서 있어야함)
		if count == 0:
			print("---검색 결과 없음---")


	elif choice == '4':
		print("[ 학생 성적 검색 ]")
		name = input("학생 이름 검색 >>")
		count = 0
		# students에 10명이 있다고 가정
		for s in students:
			if s[1] == name:
				print(f"{name}학생을 찾았습니다.")
				# 찾은 학생의 데이터를 출력
				# 상단제목
				for st in s_title:
					print(st,end='\t')
				print()
				print("ㅡ"*32)

				# 성적 출력
				print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}")
				print()
				count = 1
				break
		if count == 0:
			print("---검색 결과 없음---")


	elif choice == '0':
		print("프로그램 종료합니다.")
		print("---프로그램 종료---")
		break