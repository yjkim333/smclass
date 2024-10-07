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
	choice = int(input("항목번호를 입력해주세요. (종료 -> 0)"))

	if choice == 1:
		print("---[ 학생 성적 입력 ]---")
		while True:
			name = input(f"{no}번째 학생 이름>> (메뉴로 이동 : 0)")
			if name == '0':
				print("메뉴로 이동합니다.")
				break
			kor = int(input("국어 점수 입력>>"))
			eng = int(input("영어 점수 입력>>"))
			math = int(input("수학 점수 입력>>"))
			total = kor + eng + math
			avg = total/3
			rank = 0
			s = [no,name,kor,eng,math,total,avg,rank]
			print(f"번호 : {s[0]} 이름 : {s[1]} 국어 : {s[2]} 수학 : {s[3]} 영어 : {s[4]} 총점 : {s[5]} 합계 : {s[6]:.2f} 평균 : {s[7]}")
			students.append(s)
			no += 1

	elif choice == 2:
		print("---[ 학생 성적 출력 ]---")
		for t in s_title:
			print(t,end='\t')
		print()
		print("ㅡ"*33)

		for s in students:
			print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}")
		
	elif choice == 3:
		print("---[ 학생 성적 수정 ]---")
		name = input("찾는 학생 이름 검색>>")
		count = 0
		for s in students:
			if s[1] == name:
				print(f"{name}학생을 찾았습니다.")
				print(f"번호 : {s[0]} 이름 : {s[1]} 국어 : {s[2]} 수학 : {s[3]} 영어 : {s[4]} 총점 : {s[5]} 합계 : {s[6]:.2f} 평균 : {s[7]}")
				print()
				print("1. 국어 점수 수정")
				print("2. 영어 점수 수정")
				print("3. 수학 점수 수정")
				print("0. 성적 수정 취소")
				choice = int(input("항목 번호 선택"))
				if choice == 1:
					print("국어 점수를 수정합니다. 현재 점수 :",s[2])
					s[2] = int(input("변경할 점수 입력>>"))
				elif choice == 2:
					print("영어 점수를 수정합니다. 현재 점수 :",s[3])
					s[3] = int(input("변경할 점수 입력>>"))
				elif choice == 3:
					print("수학 점수를 수정합니다. 현재 점수 :",s[4])
					s[4] = int(input("변경할 점수 입력>>"))
				elif choice == 0:
					print("성적 수정을 취소합니다.")
					count = 1
				if count != 1:		
					s[5] = s[2]+s[3]+s[4]
					s[6] = s[5]/3
					print(s[1]," 학생 성적을 변경했습니다.")


		pass
	elif choice == 4:
		print("---[ 학생 성적 검색 ]---")
		name = input("찾는 학생 이름 검색>>")
		count = 0
		for s in students:
			if s[1] == name:
				print(f"{name}학생을 찾았습니다.")
				print(f"번호 : {s[0]} 이름 : {s[1]} 국어 : {s[2]} 수학 : {s[3]} 영어 : {s[4]} 총점 : {s[5]} 합계 : {s[6]:.2f} 평균 : {s[7]}")
				count = 1
		if count == 0:
			print("---검색 결과 없음---")
	elif choice == 5:
		pass
	elif choice == 6:
		pass
	elif choice == 0:
		print("프로그램을 종료합니다.")
		print("---프로그램 종료---")
		break