# students 리스트 타입
students = [
	{"no":1,"name":"홍길동"},
	{"no":2,"name":"유관순"},
	{"no":3,"name":"이순신"}
]
stuNo  = len(students)

def stu_input(stuNo,students):
	while True:
		# no = len(students)+1
		# print("no :",no)
		no = stuNo + 1
		# print("no :",no)
		name = input(f"{no}번째 학생 이름 입력 (0->이전페이지 이동) >> ")
		if name == '0':
			break
		students.append({"no":no,"name":name})
		stuNo += 1
	return stuNo

# 학생성적입력 호출
stuNo = stu_input(stuNo,students)
print("stuNo",stuNo)
print(students)