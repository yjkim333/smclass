# 함수 - 매개변수(일반변수, 복합변수)

# # ***1) 함수 일반매개변수
# # return이 아니면 값이 함수 밖으로 나올 수 없음.

# def calc(hh):
# 	hh += 100
# 	return hh

# h = 20
# calc(h) # 함수호출 - 호출만하고 일반변수 값을 넣어주지 않으면 값이 변경되지 않음
# h = calc(h) # 함수호출한 값을 다시 h에 넣어줘야 h의 값이 변경됨
# print(h)


# # 2) 전역변수 - 일반매개변수 - return 없이 함수 밖 값 사용
# def calc():
# 	global h
# 	h += 100

# h = 20  # 전역변수 global h에서 바로 넘어와서 return 없이 값이 변경됨  -> 언제 누가 값을 변경했는지 알 수 없어서 잘 안씀 (거의 1)번을 씀)
# calc()
# print(h)

# def calc(hh):
# 	global n
# 	n += 100
# 	return n

# n = 20
# calc(n)
# print(calc(n))


# # 3) 함수 복합매개변수 - return 없이 값을 함수 밖에서 사용
# def calc(hArr):
# 	for i in range(len(hArr)):
# 		hArr[i] += 100

# hArr = [1,2,3,4,5]  # 복합변수 - 변수에 주소값이 저장됨.
# calc(hArr)
# print(hArr)


a = 10  # 전역변수
def calc(a):
	a += 10
	print(a)
calc(a)