students = []
no = 1
while True:
	print("                        [학생 성적 프로그램]  ")
	print("ㅡ"*33)
	print("1. 학생 성적 입력")
	print("2. 학생 성적 출력")
	print("3. 학생 성적 수정")
	print("0. 프로그램 종료")
	print("ㅡ"*33)
	choice = input("항목번호를 입력해주세요. (종료 -> 0)")
	if choice == '1':
		print(" [ 학생 성적 입력 ] ")
		while True: 
			name = input("이름 입력 (메뉴로 이동->0)")
			if name == '0':
				print("---메뉴화면으로 이동합니다---")
				break
			kor = int(input("국어 점수"))
			eng = int(input("영어 점수"))
			math = int(input("수학 점수"))
			total = kor+eng+math
			avg = total/3
			rank = 0
			print(f"번호: {no}, 이름: {name}, 국어: {kor}, 영어: {eng}, 수학: {math}, 합계: {total}, 평균: {avg:.2f}")
			# s = [no,name,kor,eng,math,total,avg] -> s: 리스트 타입
			s = [no,name,kor,eng,math,total,avg,rank]
			students.append(s)
			no += 1


	elif choice == '2':
		print(" [ 학생 성적 출력 ] ")
		####
		print()
		s_title = ['번호','이름','국어','영어','수학','합계','평균','등수']

		# 상단 출력
		for s in s_title:
			print(s,end='\t')
		print()
		print("ㅡ"*32)

		# 학생 성적 출력
		for s in students:
			print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}")
		print()


	elif choice == '3':
		print(" [ 학생 성적 수정 ] ")
		print()
	elif choice =='0':
		print("프로그램을 종료합니다.")
		print("----프로그램 종료----")
		break
