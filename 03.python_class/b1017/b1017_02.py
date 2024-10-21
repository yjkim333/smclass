subject = ["이름","국어","영어","수학","합계","평균"]
students = []
score = []

### 함수선언 ###

# 
def stuScore_update(choice,k_title,s_title,s):
	print(f"현재 {k_title} 점수 : {s[s_title]}")
	s[s_title] = int(input("변경할 점수 입력 >> "))
	print()

# -------------


while True:
	print("1. 학생성적 입력")
	print("2. 학생성적 출력")
	print("3. 학생성적 수정")
	choice = int(input("원하는 번호 입력 >> "))
	if choice == 1:
		name = input("학생 이름 입력 >> ")
		score = []
		sum = 0
		for i in range(3):
			num = int(input(f"{subject[i+1]}점수 입력 >> "))
			score.append(num)
			sum += num
		avg = sum/len(score)
		stu = {'name':name,'kor':score[0],'eng':score[1],'math':score[2],'total':sum,'avg':avg}
		students.append(stu)
		print(students)

	elif choice == 3:
		search = input("검색할 학생 입력 >>")
		for s in students:
			if s['name'] == search:
				print("[수정과목선택]")
				print("1.국어")
				print("2.영어")
				print("3.수어")
				print("0.취소")
				choice = int(input("원하는 번호 입력 >> "))
				if choice == 1:
					stuScore_update(choice,'국어','kor',s)
				elif choice == 2:
					stuScore_update(choice,'영어','eng',s)
				elif choice == 3:
					stuScore_update(choice,'수학','math',s)
				elif choice == 0:
					break

	elif choice == 0:
		break