no = 1
students = []
s_title = ['번호','이름','국어','영어','수학','총점','평균','등수']
chk = 0
while True:
	print("[ 학생성적프로그램 ]")
	print("-"*60)
	print("1. 학생성적입력")
	print("2. 학생성적출력")
	print("3. 학생성적수정")
	print("4. 학생성적검색")
	print("5. 학생성적삭제")
	print("6. 등수처리")
	print("0. 프로그램 종료")
	print("-"*60)
	choice = int(input("원하는 번호를 입력하세요.(0.종료)>> "))
	if choice == 1:
		print(" [ 학생성적입력 ] ")
		print()
		while True:
			name = input(f"{no}번째 학생 이름 입력(메뉴로 이동 -> 0)")
			if name == '0':
				print("메뉴로 이동합니다.")
				break
			kor = int(input("국어 점수 입력"))
			eng = int(input("영어 점수 입력"))
			math = int(input("수학 점수 입력"))
			total = kor + eng + math
			avg = total/3
			rank = 0
			s = [no,name,kor,eng,math,total,avg,rank]
			print(s)
			students.append(s)
			print(f"{name} 학생 성적 저장 완료")
			no += 1
			

	elif choice ==2:
		print(" [ 학생성적출력 ] ")
		print()
		for t in s_title:
			print(t,end='\t')
		print()
		print("ㅡ"*32)
		for s in students:
			print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}".format(s[0],s[1],s[2],s[3],s[4],s[5],s[6],s[7]),end='\t')
			print()
			print()
			

	elif choice ==3:
		print(" [ 학생성적수정 ] ")
		search = input("학생 이름 검색 (메뉴로 이동 -> 0)>>")
		for s in students:
			if s[1] == search:
				print(f"{search} 학생을 찾았습니다.")
				print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}".format(s[0],s[1],s[2],s[3],s[4],s[5],s[6],s[7]),end='\t')
				print(" [ 수정 과목 선택 ]")
				print("1. 국어점수 수정")
				print("2. 영어점수 수정")
				print("3. 수학점수 수정")
				print("0. 성적 수정 취소")
				choice = int(input("원하는 번호를 입력하세요.>>"))
				if choice == 1:
					print("현재 국어점수")
				elif choice == 2:
					print("현재 국어점수")
				elif choice == 3:
					print("현재 국어점수")
				elif choice == 0:
					print("현재 국어점수")
				
	elif choice == 4:
		print(" [ 학생성적검색 ] ")
		search = input("학생 이름 검색 (메뉴로 이동 -> 0)>>")
		for s in students:
			if s[1] == search:
				print(f"{search} 학생을 찾았습니다.")
				print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}".format(s[0],s[1],s[2],s[3],s[4],s[5],s[6],s[7]),end='\t')
				chk = 1
				break
		if chk == 0:
			print(f"\"{search}\" 검색 결과 없음")
		print()
	
			
	elif choice ==5:
		print(" [ 학생성적삭제 ] ")
	elif choice ==6:
		print(" [ 등수처리 ] ")
	elif choice == 0:
		print("프로그램 종료")
		print("프로그램을 종료합니다.")
		break
		
		