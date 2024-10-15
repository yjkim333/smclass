# # 구구단

# # 함수선언
# def calc(st,end):
# 	for i in range(st,end+1):
# 		print(f"[ {i} 단 ]")
# 		for j in range(2,10):
# 			print(f"{i}x{j} = {i*j}")

# # 함수
# st = 2
# end = 9
# calc(st,end) # 함수호출
# calc(3,7) # 함수호출
# calc(5,9) # 함수호출



# # # ------------
# # # 2-9단
# # # for문
# # st = 2
# # end = 9
# # for i in range(st,end+1):
# # 	print(f"[ {i} 단 ]")
# # 	for j in range(2,10):
# # 		print(f"{i}x{j} = {i*j}")

# # # 3-7단
# # # for문
# # st = 3
# # end = 7
# # for i in range(st,end+1):
# # 	print(f"[ {i} 단 ]")
# # 	for j in range(2,10):
# # 		print(f"{i}x{j} = {i*j}")

# # # 5-9단
# # # for문
# # st = 5
# # end = 9
# # for i in range(st,end+1):
# # 	print(f"[ {i} 단 ]")
# # 	for j in range(2,10):
# # 		print(f"{i}x{j} = {i*j}")




# 함수 -기본매개변수, 가변매개변수, 키워드매개변수
# def 함수명(매개변수 갯수) - 선언
# 함수명(매개변수 갯수) - 호출
# 선언과 호출의 매개변수의 갯수를 맞춰야 함


# # 1) 함수 - 기본매개변수
# def plus(n1,n2):
# 	sum = n1 + n2
# 	print("합계 :",sum)

# # 함수호출 - 선언과 호출의 매개변수의 갯수를 정확히 맞춰야 함, 아니면 에러
# plus(10,20)


# # 2) 함수 - 가변매개변수
# def plus(a,*n1):    # -> * 매개변수의 갯수 상관없이 들어옴 -> tuple로 넘어감  // (*n1,a) -> 이렇게 넣으면 이미 *n1에 모든것이 들어와서 a에 들어갈 것이 없음 = 에러
# 	print("a :",a)		# -> a에는 첫번째거가 들어옴
# 	for i in n1:
# 		print(i)
# 	print(type(n1))  # -> tuple 형태로 넘어옴

# plus(1,2,3,4,5)


# # 3) 함수 - 키워드매개변수
# def plus(k=10,m=5):
# 	print("k :",k)
# 	print("m :",m)

# plus()  				# 매개변수 갯수를 맞춰주지 않으면 에러지만, 키워드매개변수는 상관없음
# plus(1,2) 			# 매개변수를 주면 그걸 받아감, 매개변수 없으면 함수에 있는 값을 넣어줌
# plus(m=1,k=2) 	# 매개변수를 주면 그걸 받아감, 매개변수 없으면 함수에 있는 값을 넣어줌


# print() 는 가변매개변수, 키워드매개변수 함수
# print(1,2,3,4,5)  # 1 2 3 4 5 -> sep:" "가 기본으로 되어있어서..
# print(1,2,3,4,5,sep="")  # 12345
# print(1,2,3,4,5,sep="",end='\t') 
# print(1)


# 함수 - 가변매개변수,키워드매개변수 동시 사용 경우
# def plus(*n,k=10): 	  # 키워드매개변수는 가변매개변수 뒤에 와야 함.
# 	print("k :",k)
# 	for i in n:
# 		print(i)

# plus(1,2,3,4,5,k=50)	# 가변형매개변수가 먼저, 다음 키워드매개변수 사용해야함.
