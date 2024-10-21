# students 리스트 타입
students = [
	{"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
	{"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
	{"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
	{"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
	{"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
]
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수'] #전역변수
choice = 0 # 전역변수
chk = 0    # 체크변수
count = 1  # 성적처리
stuNo = len(students)  # 리스트에 학생이 있으면, 그 인원으로 변경
no=0;name="";kor=0;eng=0;math=0;total=0;avg=0;rank=0 #성적처리변수
stuNo = len(students)

### 메뉴함수 선언 ###
def program_menu(choice):
	print("[ 학생성적프로그램 ]")
	print("-"*60)
	print("1. 학생성적입력")
	print("2. 학생성적출력")
	print("3. 학생성적수정")
	print("4. 학생성적검색")
	print("5. 학생성적삭제")
	print("6. 등수처리")
	print("7. 학생성적정렬")
	print("0. 프로그램 종료")
	print("-"*60)
	choice = int(input("원하는 번호를 입력하세요.(0.종료)>> "))
	return choice
###---

### 1.학생성적입력함수 선언 ###
def stu_input(stuNo):
	print("[  학생 성적 입력  ]")
	while True:
		no = stuNo +1
		name = input(f"{no}번 학생 이름 입력(메뉴로 이동->0) >>")
		if name == '0':
			print("-메뉴로 이동합니다.-")
			break
		score = []
		total = 0
		for i in range(3):
			sc = int(input(f"{s_title[i+2]}성적 입력 >> "))
			total += sc
			score.append(sc)
		avg = total/3
		rank = 0
		ss = {'no':no,'name':name,'kor':score[0],'eng':score[1],'math':score[2],'total':total,'avg':avg,'rank':rank}
		students.append(ss)
		stuNo += 1
		print(f"{name} 학생의 성적을 입력했습니다.")
###---

### 2.학생성적출력함수 선언 ###
def stu_output(students):
	print("[  학생 성적 출력  ]")
	print()
	# 상단타이틀
	for t in s_title:
		print(t,end='\t')
	print()
	print("ㅡ"*33)
	# 학생성적출력
	for s in students:
		print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
		print()
###---

### 3.학생성적수정함수 선언 ###
def stu_update(students):
	print("[  학생 성적 수정  ]")
	print()
	name = input(f"학생 이름 검색 >>")
	flag = 0
	for s in students:
		if s['name'] == name:
			print()
			print(f"{name} 학생을 찾았습니다.")
			print("[ 수정 과목 선택 ]")
			print("1. 국어")
			print("2. 영어")
			print("3. 수학")
			choice = int(input("원하는 과목의 번호 입력 >> "))
			if choice == 1:
				print("현재 국어 점수 :",s['kor'])
				s["kor"] = int(input("수정할 점수 입력 >> "))
			if choice == 2:
				print("현재 영어 점수 :",s['eng'])
				s["eng"] = int(input("수정할 점수 입력 >> "))
			if choice == 3:
				print("현재 수학 점수 :",s['math'])
				s["math"] = int(input("수정할 점수 입력 >> "))
			s["total"] = s["kor"] + s["eng"] + s["math"]
			s["avg"] = s["total"]/3
			print("성적이 수정되었습니다.")
			stu_output([s])
			flag = 1
	if flag == 0:
		print(f"{name} 학생 검색 결과 없음")


while True:
	choice = program_menu(choice)     # 메뉴함수 호출

	if choice == 1:
		stu_input(stuNo)								# 1.학생성적입력함수 호출

	elif choice == 2:
		stu_output(students)            # 2.학생성적출력함수 호출

	elif choice == 3:
		stu_update(students)
		
	elif choice == 4:
		print("[  학생 성적 검색  ]")
		print()
		name = input(f"학생 이름 검색 >>")
		flag = 0
		for s in students:
			if s['name'] == name:
				print()
				print(f"{name} 학생을 찾았습니다.")
				stu_output([s])
				flag = 1
		if flag == 0:
			print("")

	elif choice == 5:
		pass
	elif choice == 6:
		pass
	elif choice == 7:
		pass
	elif choice == 0:
		print("프로그램을 종료하니다.")
		print("[  프로그램 종료  ]")
		break