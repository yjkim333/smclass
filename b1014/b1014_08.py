# # 기본매개변수
# def calc(n1,n2,n3):  # -> 매개변수의 갯수만큼 보내야 에러 안생김
# 	print(n1+n2+n3)
# calc(1,2,3)					 # -> 매개변수와 갯수를 맞춰야 함

# # 가변매개변수
# def calc(*n):  # -> * 가변매개변수 -> 튜플로 받음
# 	print(n)
# 	print(len(n))
# calc()		# 가변매개변수는 갯수를 맞출 필요없음

# # 키워드매개변수
# def calc(n1 = 10,n2 = 20):
# 	print(n1)
# 	print(n2)

# calc()				# 아무것도 넣지 않으면 10,20이 나옴
# calc(20)  		# 값이 있으면 값을 넣어 # 20,20 -> 키가 없으면 첫번째에 들어감 -> 앞에는 값이 들어갔지만 뒤에는 없어서 20이 나옴
# calc(n2=100)	# 카가 있으면 키에 값이 전달됨
# 

# print(1,2,3,5,6,8,sep="!",end='\t')  # 가변매개변수 1,2  , 키워드매개변수 end='\t'
# print("안녕")


# 함수 내에 선언된 변수는 외부에서 사용할 수 없다. -> 함수 내 변수사용하려면 return 해줘야함
# def calc(v1,v2):
# 	sum = 0  # 지역변수
# 	for i in range(v1,v2+1):
# 		sum += i
# 	return sum

# sum = calc(1,10)
# print(sum)


# def calc(v1,v2):
# 	global sum		# 전역변수
# 	# sum = 0				# 지역변수
# 	for i in range(v1,v2+1):
# 		sum += i
# 	return sum

# sum = 100  # 외부의 변수를 사용해서 계산하고 싶은 경우 global 전역변수 사용
# sum = calc(1,10)   # 55
# print(sum)				 # 155


# def calc(n1,n2):
# 	s1 = n1 + n2
# 	s2 = n1 - n2
# 	s3 = n1 * n2
# 	s4 = n1 / n2
# 	s5 = [s1,s2,s3,s4]
# 	# return s1,s2,s3,s4
# 	return s5


# # s1,s2,s3,s4 = calc(10,5)
# s5 = calc(10,5)
# # print(s1)
# # print(s2)
# # print(s3)
# # print(s4)
# # print(s1,s2,s3,s4)
# print(s5)

# print("프로그램 종료")



# 매개변수가 일반변수(문자열,숫자형,논리형 값 1개)일 경우 return 하지않으면 변수 값 변동 없음
# hh = 100 
# def add(hh):
# 	hh = hh + 100
# add(hh)
# print(hh)

# # 매개변수가 복합변수(여러값 저장)일 경우
# hong = [1,2,3,4,5]
# # 복합변수가 매개변수로 전달이 되면, return이 없어도 값이 변경되어 전달됨.
# def add(h):
# 	for i in range(len(h)):
# 		h[i] = h[i] + 100
# add(hong)
# print(hong)


# 전역변수인 경우 함수 내에서도 사용이 가능하고
# 함수 외부에서도 사용이 가능함

# 지역변수는 return 없이는 값이 함수 밖으로 나오지 못함

# def calc():
# 	global sum   # 전역변수인 경우, 함수에서 변경시 return 없이도 외부에서도 같이 변경됨.
# 	sum = 100

# sum = 10
# calc()				# 함수에서 sum이 100으로 변경이 됨
# print(sum)		# 그래서 결과값이 100



# 얕은 복사
# kim = []
# kim = hong
# kim[0] = 100
# print(hong)  #[100, 2, 3, 4, 5]




# num = int(input("숫자1 입력>> "))
# num2 = int(input("숫자2 입력>> "))

# def calc(num,num2):
# 		print(f"두 수 더하기 : {num+num2}")
# 		print(f"두 수 빼기 : {num-num2}")
# 		print(f"두 수 곱하기 : {num*num2}")
# 		print(f"두 수 나누기 : {num/num2}")

# numStr = input("숫자1 입력(12,5)>> ")		# 문자열타입
# n = numStr.split(",")
# num = int(n[0])		# 문자열타입 -> 숫자형타입
# num2 = int(n[1])
# calc(num,num2)


# 3개의 숫자를 입력받아...
# def calc(num,num2,num3):
# 		print(f"두 수 더하기 : {num+num2+num3}")
# 		print(f"두 수 빼기 : {num-num2-num3}")
# 		print(f"두 수 곱하기 : {num*num2*num3}")
# 		print(f"두 수 나누기 : {num/num2/num3}")	

# i_num = input("숫자입력(0,0,0) >> ")
# n = i_num.split(",")
# num = int(n[0])
# num2 = int(n[1])
# num3 = int(n[2])
# calc(num,num2,num3)

# def calc(n2):   #배열
# 	s1 = 0
# 	s2 = 0 
# 	s3 = 1 # 곱하기는 0으로 시작하면 안되니까
# 	s4 = 1 # 나누기는 0으로 시작하면 안되니까
# 	for i in range(len(n2)):
# 		s1 += n2[i]
# 		s2 -= n2[i]
# 		s3 *= n2[i]
# 		s4 /= n2[i]
# 	print(f"더하기 : {s1}")
# 	print(f"빼기 : {s2}")
# 	print(f"곱하기 : {s3}")
# 	print(f"나누기 : {s4}")

# i_num = input("숫자입력(0,0,0) >> ")
# n = i_num.split(",")
# n2 = [int(i) for i in n]  # 리스트내포
# print(n2)
# calc(n2)





# def calc(num,num2):
# 		print(f"두 수 더하기 : {num+num2}")
# 		print(f"두 수 빼기 : {num-num2}")
# 		print(f"두 수 곱하기 : {num*num2}")
# 		print(f"두 수 나누기 : {num/num2}")

# num = int(input("숫자1 입력>> "))
# num2 = int(input("숫자2 입력>> "))
# calc(num,num2)


# 함수사용
# def calc(num,num2):
# 	print(f"두 수 더하기 : {num+num2}")
# 	print(f"두 수 빼기 : {num-num2}")
# 	print(f"두 수 곱하기 : {num*num2}")
# 	print(f"두 수 나누기 : {num/num2}")

# num = [10,20,30]
# num2 = [5,7,3]

# for i in range(len(num)):
# 	calc(num[i],num2[i])

# # for문을 활용한 계산
# num = [10,20,30]
# num2 = [5,7,3]

# for i in range(len(num)):
# 	print(f"두 수 더하기 : {num[i]+num2[i]}")
# 	print(f"두 수 빼기 : {num[i]-num2[i]}")
# 	print(f"두 수 곱하기 : {num[i]*num2[i]}")
# 	print(f"두 수 나누기 : {num[i]/num2[i]}")



# for i in num:
# 	for j in num2:
# 		print(f"두 수 더하기 : {i+j}")
# 		print(f"두 수 빼기 : {i-j}")
# 		print(f"두 수 곱하기 : {i*j}")
# 		print(f"두 수 나누기 : {i/j}")

# print(f"두 수 더하기 : {num+num2}")
# print(f"두 수 빼기 : {num-num2}")
# print(f"두 수 곱하기 : {num*num2}")
# print(f"두 수 나누기 : {num/num2}")

# num = 20
# num2 = 7
# print(f"두 수 더하기 : {num+num2}")
# print(f"두 수 빼기 : {num-num2}")
# print(f"두 수 곱하기 : {num*num2}")
# print(f"두 수 나누기 : {num/num2}")

# num = 30
# num2 = 3
# print(f"두 수 더하기 : {num+num2}")
# print(f"두 수 빼기 : {num-num2}")
# print(f"두 수 곱하기 : {num*num2}")
# print(f"두 수 나누기 : {num/num2}")