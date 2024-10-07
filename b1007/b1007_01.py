students = []
s_title = ['번호','이름','국어','영어','수학','총점','평균','등수']
choice = 0
stuNo = 0   #학생번호 생성
stuNo = len(students) #리스트에 학생이 있으면, 그 인원으로 변경
chk = 0 	  # 체크 변수
count = 1   # 성적처리
no = 0; name = ""; kor = 0; eng = 0; math = 0; total = 0; avg = 0; rank = 0; #성적처리변수

while True:
	print("[학생 성적 프로그램]")
	print("ㅡ"*33)
	print("1. 학생 성적 입력")
	print("2. 학생 성적 출력")
	print("3. 학생 성적 수정")
	print("4. 학생 성적 검색")
	print("5. 학생 성적 삭제")
	print("6. 등수처리")
	print("0. 프로그램 종료")
	print("ㅡ"*33)
	choice = int(input("원하는 번호를 입력하세요.>>"))
	if choice == 1:
		print("[ 학생 성적 입력 ]")
		print()
		while True:
			#학생 성적 직접 입력
			no = stuNo + 1  # 리스트 학생 수
			name = input(f"{no}번째 학생 이름 입력(메뉴로이동 -> 0)>>")
			if name == "0":
				print("성적입력을 취소합니다.")
				print()
				break
			kor = int(input("국어 성적 입력"))
			eng = int(input("영어 성적 입력"))
			math = int(input("수학 성적 입력"))
			total = kor + eng + math
			avg = total/3
			s = [no,name,kor,eng,math,total,avg,rank]
			students.append(s)
			stuNo += 1 #학생수(번호) 1증가
			print(f"{name} 학생의 성적 저장되었습니다.")
			print()

	elif choice == 2:
		print("                        [ 학생 성적 출력 ]")
		print()
		# 상단 타이틀 출력
		for title in s_title:
			print(f"{title}\t",end='')
		print()
		# print(f"{s_title[0]}\t{s_title[1]}\t{s_title[2]}\t{s_title[3]}\t{s_title[4]}\t{s_title[5]}\t{s_title[6]}\t{s_title[7]}\n") #위 세줄이랑 같음
		print("ㅡ"*33)
		print()
		# 학생 성적 출력
		for s in students:
			print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}\n")
			print()

	elif choice == 3:
		print("[ 학생 성적 수정 ]")
		print()
		while True:
			name = input(f"학생 이름 검색(메뉴로이동 -> 0)>>")
			chk = 0
			if name == "0":
				print("메뉴로 이동합니다.")
				print()
				break
			for s in students:
				if s[1] == name:
					print(f"{name} 학생을 찾았습니다.")
					print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}")
					print()
					print("[ 수정 과목 선택 ]")
					print("1. 국어점수 수정")
					print("2. 영어점수 수정")
					print("3. 수학점수 수정")
					print("0. 수정 취소")
					choice = int(input("원하는 항목 번호 입력>>"))
					if choice == 1:
						print("현재 국어점수 : {}".format(s[2]))
						s[2] = int(input("변경할 점수 입력"))
					elif choice == 2:
						print("현재 영어점수 : {}".format(s[3]))
						s[3] = int(input("변경할 점수 입력"))
					elif choice == 3:
						print("현재 수학점수 : {}".format(s[4]))
						s[4] = int(input("변경할 점수 입력"))
					
					s[5] = s[2] + s[3] + s[4]  #합계
					s[6] = s[5]/3							#평균

					print(f"{name} 학생의 성적을 수정하였습니다.")
					print()
					chk = 1
			# 모든 학생 비교가 끝난 후, chk 확인
			if chk == 0:
				print(f"{name}학생 검색 결과 없음")
				print()


	elif choice == 4:
		print("[ 학생 성적 검색 ]")
		print()
		while True:
			name = input(f"학생 이름 검색(메뉴로이동 -> 0)>>")
			chk = 0
			if name == "0":
				print("메뉴로 이동합니다.")
				print()
				break
			for s in students:
				if s[1] == name:
					print(f"{name} 학생을 찾았습니다.")
					print()
					# 상단 타이틀 출력
					for title in s_title:
						print(f"{title}\t",end='')
					print()
					print("ㅡ"*33)
					print()
					# 학생 성적 출력
					print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}\n")
					print()
					chk = 1
			# 모든 학생 비교가 끝난 후, chk 확인
			if chk == 0:
				print(f"{name}학생 검색 결과 없음")
				print()

	elif choice == 5:
		print("[ 학생 성적 삭제 ]")
		print()
		while True:
			name = input(f"학생 이름 검색(메뉴로이동 -> 0)>>")
			chk = 0
			if name == "0":
				print("메뉴로 이동합니다.")
				print()
				break
			for i,s in enumerate(students):
				if s[1] == name:
					chk = 1
					print(f"{name} 학생을 찾았습니다.")
					print()
					choice = input(f"{name} 학생 성적을 삭제하시겠습니까?(삭제 시 복구 불가)\n1.삭제 2.취소")
					if choice == "1":
						del students[i]
						print(f"{name} 학생의 성적을 삭제했습니다.")
					else:
						print("삭제 취소")
						break
			# 모든 학생 비교가 끝난 후, chk 확인
			if chk == 0:
				print(f"{name}학생 검색 결과 없음")
				print()


	elif choice == 6:
		print("[ 등수처리 ]")
		print()
		for s in students:
			count = 1
			for st in students:
				if s[5] < st[5]:
					count += 1
			s[7] = count 				# 등수 입력
		print("등수처리를 완료했습니다.")
		print()


	elif choice == 0:
		print("[ 프로그램 종료 ]")
		print("프로그램을 종료합니다.")
		break