class Student:
	# 변수 3종류
	# 지역변수 : 함수 내에 선언된 변수. 함수 종료되면 사라짐.
	# 인스턴스 변수 - 객체선언 할 때 만들어짐. 각각의 객체 마다 변수가 따로따로 생성됨 -> 각각에 영향을 미치지 않음.
	# 사용방법 - 참조변수명.변수명
	# 클래스 변수 - 객체가 선언되지 않아도 만들어짐. 모든 객체가 공동으로 사용 -> 모든 객체에 영향을 미침.
	# 사용방법 - 클래스명.변수명

	count = 0			 # 클래스 변수
	students = []

	# 함수 2종류
	# 인스턴스 함수 - 객체선언 할 때 만들어짐. 각각의 객체마다 함수가 따로따로 생성됨. -> 각각에 영향을 미치치 않음.
	# 사용방법 - 참조변수명.함명
	# 클래스 함수 - 객체가 선언되지 않아도 만들어짐. 모든 객체가 공동으로 사용
	# @classmethod  -> 클래스 함수 표시
	# 사용방법 - 클래스명.함수명

	def __init__(self,name,kor,eng,math):
		Student.count += 1
		self.__no = Student.count			# 인스턴스 변수
		self.name = name
		self.kor = kor
		self.eng = eng
		self.math = math
		self.total = kor+eng+math
		self.avg = (kor+eng+math)/3
		self.rank = 0
		Student.students.append(self)

	@classmethod
	def stu_print(cls):
		for s in cls.students:
			print(str(s))

	# no_getter를 사용하지않으면 접근 불가
	def get_no(self):
		return self.__no
	def set_no(self,no):
		if no<0 : raise "0이하는 입력을 할 수 없습니다."
		self.__no = no

	def __str__(self):  # 리턴값은 무조건 문자열로!
		return f"{self.__no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg:.2f}\t{self.rank}"

# 1. 학생성적입력
# 이름,국어,영어,수학 -> 번호,국어,영어,수학,합계,평균,등수
# 클래스 1개가 생성이되고
# 클래스의 참조변수(__str__)를 입력해서 출력을 해보세요.

s_title = ['번호','이름','국어','영어','수학','합계','평균','등수']

print("1.학생성적입력")
while True:
	name = input("학생이름입력 >> ")
	score = []
	for s in range(2,4+1):
		score.append(int(input(f"{s_title[s]}성적입력 >> ")))

	# 참조변수명  = 클래스명()  => 객체선언
	s1 = Student(name,*score)
	# 객체선언을 한 참조변수를 출력하면 주소값이 출력됨
	# 참조변수를 원하는대로 출력하려면 __str__써야함
	print(s1)
	# for s in Student.students:
	# 	print(s)
	Student.stu_print()