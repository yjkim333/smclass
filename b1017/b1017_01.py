# subject = ["국어","영어"]

# ##함수선언##
# def output(subject):
# 	# 출력
# 	print("[ 과 목 ]")
# 	print("ㅡ"*10)
# 	for s in subject:
# 		print(s)


# while True:
# 	print("[ 과목 생성 프로그램 ]")
# 	s_input = input("원하는 과목 입력 >> ")
# 	# list - append
# 	subject.append(s_input)
# 	output(subject)    # 함수호출



# #변수를 넘길때 안넘길때

# a = 10  # 전역변수
# # 함수선언
# def func(a):
# 	# global a		# 전역변수를 가져옴
# 	# a = 50	  # 지역변수 - 함수 종료 시 모두 제거됨
# 	print("함수 안 a 값:",a)
# 	a += 50
# 	return a

# # 함수호출
# a = func(a)
# print("함수 밖 a 값:",a)


# a = 10
# b = 20
# sum = 0
# # 함수선언
# def add(a,b):
# 	return a+b

# sum = add(a,b)  # 함수호출
# print("a+b의 합계 :",sum)


# a = 10
# b = 20
# c = 30

# def add(a,b,c):
# 	return a+b+c

# a = add(a,b,c)
# print(a)


subject = ["국어","영어"]
score = []

while True:
	print("1.과목추가")
	print("0.종료")
	choice = int(input("번호 입력 >> "))
	if choice == 1:
		s_input = input("추가 과목 입력>")
		subject.append(s_input)
	elif choice == 0:
		break

for i in range(len(subject)):
	score.append(int(input(f"{subject[i]}점수 입력 >> ")))
sum = 0
for i in range(len(subject)):
	print(f"{subject[i]} : {score[i]}")
	sum += score[i]
print('합계 :',sum)

# num1 = int(input("국어점수 입력 >> "))
# num2 = int(input("영어점수 입력 >> "))
# num3 = int(input("수학점수 입력 >> "))
# num4 = int(input("과학점수 입력 >> "))
# num5 = int(input("역사점수 입력 >> "))
# print("국어 :",num1)
# print("영어 :",num2)
# print("수학 :",num3)
# print("과학 :",num4)
# print("역사 :",num5)
# print("합계 :",num1+num2+num3+num4+num5)




# ##함수선언##
# def output(subject):
# 	# 출력
# 	print("[ 과 목 ]")
# 	print("ㅡ"*10)
# 	for s in subject:
# 		print(s)


# while True:
# 	print("[ 과목 생성 프로그램 ]")
# 	s_input = input("원하는 과목 입력 >> ")
# 	# list - append
# 	subject.append(s_input)
# 	output(subject)    # 함수호출
