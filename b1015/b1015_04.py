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

#### 학생성적출력함수 선언 ####
def stu_output(s_title,students):
	print("[ 학생성적 출력 ]")
	print()

	# 상단출력
	for st in s_title:
		print(st,end="\t")
	print(); print("-"*60)

	# 학생성적출력
	for s in students:
		print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
	print()


#### 학생성적 수정 함수선언 ####
def stu_update(s_title,students):
	print("[ 학생성적수정 ]")
	name = input("찾고자 하는 학생의 이름을 입력하세요.")
	
	# 전체학생과 비교
	flag = 0
	for s in students:
		if s['name'] == name:
			print()
			print(f"{name} 학생을 찾았습니다.")
			print("[ 수정 과목 선택 ]")
			print("1. 국어점수")
			print("2. 영어점수")
			print("3. 수학점수")
			choice = int(input("원하는 번호를 입력하세요.>> "))
			if choice == 1:
				print("현재 국어점수 : {}".format(s['kor']))
				s['kor'] = int(input("변경 국어점수 >> "))
			elif choice == 2:
				print("현재 영어점수 : {}".format(s['eng']))
				s['eng'] = int(input("변경 영어점수 >> "))
			elif choice == 3:
				print("현재 수학점수 : {}".format(s['math']))
				s['math'] = int(input("변경 수학점수 >> "))

			s['total'] = s['kor'] + s['eng'] + s['math']
			s['avg'] = s['total']/3

			print(f"{name} 학생 성적이 수정되었습니다.")

			
			
			# 수정된 학생의 성적 출력 - 학생성적출력함수 재사용
			stu_output(s_title,[s])  # s 는 리스트타입으로 보내야함

			flag = 1

		# 학생이 검색되지 않았을 때
	if flag == 0:
		print(f"{name} 학생 검색 결과 없음")

#----------------------



print("3. 학생성적수정")
choice = int(input("원하는 번호 입력 >> "))

if choice == 3:
	stu_update(s_title,students)