# def func(v):
# 	return v*2

# lambda v:v*2  # 위 함수와 같다, 한줄일경우만 가능

# print(func(2))

# 기본적인 함수사용
# aArr = [1,2,3,4]
# bArr = []
# for a in aArr:
# 	bArr.append(func(a))

# print(bArr)


# 리스트내포
# aArr = [1,2,3,4]
# bArr = [a*2 for a in aArr]
# print(bArr)


# # map 함수    map(함수,리스트) : 리스트의 내용을 한개씩 함수에 전달해서 결과값을 리스트로 저장
# aArr = [1,2,3,4]
# bArr = list(map(func,aArr))    # aArr에 있는 값을 1개씩 func에 넣어 적용해서 bArr로 넣어준다
# print(type(bArr)) 						 #  -> type이 map 이라 리스트로 타입변경!
# print(bArr)

# # lambda
# bArr = list(map(lambda x:x*2,aArr))
# print(bArr)



# filter(함수,반복가능한 자료형 리스트) => 반복가능한 자료형 리스트-리스트,튜플,딕셔너리


# def func(v):
# 	if v%2 == 0:
# 		return v
# 	else:
# 		return

# 기본함수사용방법
# aArr 값 중에 2의 배수인 경우만 리턴
# aArr = [1,2,3,4]
# bArr = []
# for i in aArr:
# 	if func(i) != None:
# 		bArr.append(func(i))
# print(bArr)


# filter함수 사용
# def func(v):
# 	if v%2 == 0:
# 		return True
# 	else:
# 		return False
	
# aArr 값 중에 2의 배수인 경우만 리턴
# aArr = [1,2,3,4]
# bArr = list(filter(func,aArr))  # 조건에 맞는 부분(True)만 데이터를 bArr에 넣어줌
# print(bArr)

# filter함수 사용, lambda식 사용
# aArr 값 중에 2의 배수인 경우만 리턴
# aArr = [1,2,3,4]
# bArr = list(filter(lambda x:x%2==0,aArr))
# print(bArr)


# zip함수 - 2개의 리스트를 1개로 합침
# a = [1,2,3,4]
# b = [10,20,30,40]
# print(list(zip(a,b)))  
# print(dict(zip(a,b)))  


# lambda
# num1 = 1
# num2 = 1
# h = lambda num1,num2:num1+num2


# def func(v1,v2):
# 	return v1*v2

# lambda v1,v2:v1*v2


a = [1,2,3,4]
b = [10,20,30,40]

# a+b = [11,22,33,44]

# 기본함수사용
# 1
# def func(a,b):
# 	aArr = [i+j for i,j in zip(a,b)]
# 	return aArr

# 2
# aArr = []
# def func(a,b):
# 	for i,j in zip(a,b):
# 		aArr.append(i+j)
# 	return aArr
# print(func(a,b))


# def func(a):
# 	for i in a:
# 		aArr.append(i*i)
# 		return aArr
# print(func(a))

# # 리스트내포
# aArr = [i+j for i,j in zip(a,b)]
# print(aArr)

# # lambda식
# # map(lambda 매개변수1,매개변수2:return값(수식),복합자료형1,복합자료형2)
# aArr = list(map(lambda i,j:i+j,a,b))
# print(aArr)


# 퀴즈
a = [1,2,3,4,5]
# a 리스트에 10을 모두 더해서 출력하시오
# 리스트내포, 람다식사용
# 리스트내포
b = [i+10 for i in a]
print(b)
# 람다식
# map - 리스트 모두에 동일한 형태를 적용시킬때 사용
b = list(map(lambda x:x+10,a))
print(b)

# 4*3*2*1
result = 1
for i in range(1,5):
	result *= i