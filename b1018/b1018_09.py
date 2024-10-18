class Student:
	students = []
	count = 0

	@classmethod
	def stu_print(cls):
		for s in cls.students:
			print(str(s))
			

	def __init__(self,name,kor,eng,math):
		Student.count += 1
		self.no = Student.count
		self.name = name
		self.kor = kor
		self.eng = eng
		self.math = math
		self.total = kor+eng+math
		self.avg = (kor+eng+math)/3
		self.rank = 0
		Student.students.append(self)
	
	def __str__(self):
		return f"{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg:.2f}\t{self.rank}"


s_title = ['번호','이름','국어','영어','수학','합계','평균','등수']

while True:
	print("[학생성적프로그램]")
	print("1. 학생 성적 입력")
	print("2. 학생 성적 출력")
	print("3. 학생 성적 수정")
	choice = int(input("원하는 번호 입력 >> "))
	if choice == 1:
		while True:
			print("[학생성적입력]")
			name = input("학생이름입력(0.메뉴) >> ")
			if name == '0':
				break
			score = []
			for s in range(2,4+1):
				score.append(int(input(f"{s_title[s]} 점수 입력 >> ")))
			s1 = Student(name,*score)
			print(f"{s1.name} 학생이 입력되었습니다.")
	elif choice == 2:
		print("[학생성적입력]")
		Student.stu_print()
	elif choice == 3:
		print("[학생성적수정]")
		name = input("학생이름입력(0.메뉴) >> ")
		flag = 0
		for s in Student.students:
			if s.name == name:
				flag = 1
				print("과목선택")
				print("1.국어")
				print("2.영어")
				print("3.수학")
				choice = int(input("원하는 번호 입력 >> "))
				if choice == 1:
					print(f"현재 국어점수 : {s.kor}")
					s.kor = int(input("변경할 점수 >> "))
				elif choice == 2:
					print(f"현재 영어점수 : {s.eng}")
					s.eng = int(input("변경할 점수 >> "))
				if choice == 3:
					print(f"현재 수학점수 : {s.math}")
					s.math = int(input("변경할 점수 >> "))
				s.total = s.kor+s.eng+s.math
				s.avg = s.total/3
				print("수정되었습니다.")
		if flag == 0:
			print("검색결과 없음")




