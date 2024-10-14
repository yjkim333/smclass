# def num_sum(start,end): # (매개변수,매개변수)
# 	sum = 0  # 지역변수
# 	for i in range(start,end+1):
# 		sum += i
# 	print("합계 :",sum)

# # # 전역변수
# # sum = 0

# # # 1~10까지 합계 출력
# # num_sum(1,10)

# # # for i in range(1,10+1):
# # # 	sum += i  # sum = sum + i
# # # print("합계 :",sum)


# # # 1~100까지 합계 출력
# # num_sum(1,100)

# # # for i in range(1,100+1):
# # # 	sum += i
# # # print("합계 :",sum)


# # # 2~50까지 합계 출력
# # num_sum(2,50)

# # # for i in range(2,50+1):
# # # 	sum += i
# # # print("합계 :",sum)


# # # 100~1000까지 합계 출력
# # num_sum(100,1000)

# # # for i in range(100,1000+1):
# # # 	sum += i
# # # print("합계 :",sum)



# # 두개의 숫자를 입력받아 그 사이의 숫자 합을 구하시오
# # num1, num2 변수 & 함수 사용하시오
# def n_sum(num1,num2):
# 	sum = 0
# 	for i in range(num1,num2+1):
# 		sum += i
# 	print("합계 :",sum)

# num1 = int(input("숫자1 입력>> "))
# num2 = int(input("숫자2 입력>> "))
# n_sum(num1,num2)



# def num_sum(st,end):
# 	sum = 0
# 	for i in range(st,end+1):
# 		sum += i
# 	return sum # 호출하는 곳으로 return 해준다

# num1 = int(input("숫자1 입력>> "))
# num2 = int(input("숫자2 입력>> "))
# print(num_sum(num1,num2))

# total = 0
# num_sum(1,10)
# num_sum(1,100)
# total = num_sum(1,10) + num_sum(1,100)
# # 1~10까지 합과 1~100까지 합의 총합을 출력하시오
# print("합계 :",total)

# print("프로그램 종료")



# 2~50 3~7 5~50 사이의 값을 모두 더해서 출력하시오
# def num_sum(st,end):
# 	sum = 0
# 	for i in range(st,end):
# 		sum += i
# 	return sum

# total = 0	
# print("2~50까지의 합 : {:,d}".format(num_sum(2,51)))
# print(f"3~7까지의 합 : {num_sum(3,8):,d}")
# num_sum(5,51)
# total = num_sum(2,51) + num_sum(3,8) + num_sum(5,51)
# print("합계 : {:,d}".format(total))



# def plus(n1,n2):
# 	result = n1 + n2
# 	return result
# # def plus(n1,n2):
# # 	return n1 + n2

# print(plus(1,2))
# print(plus(55,45))
# print(plus(50,50))



# 두 수를 입력받아 두 수의 더하기를 출력하시오.
def plus(n1,n2):
	result = n1 + n2
	return result

n1 = int(input("숫자1>> "))
n2 = int(input("숫자2>> "))
print("합계 :",plus(n1,n2))
