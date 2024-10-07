# 배열은 동일한 타입만 묶을 수 있다.
# 리스트는 다른 타입도 묶을 수 있다.

# a,b,c,d,e,f,g = 0,0,0,0,0,0,0
# total = 0

# # 변수 a,b,c,d,e 의 변수에 숫자를 입력받아 합계를 출력하시오
# a = int(input("1번째 숫자를 입력하세요"))
# b = int(input("2번째 숫자를 입력하세요"))
# c = int(input("3번째 숫자를 입력하세요"))
# d = int(input("4번째 숫자를 입력하세요"))
# e = int(input("5번째 숫자를 입력하세요"))
# f = int(input("6번째 숫자를 입력하세요"))
# g = int(input("7번째 숫자를 입력하세요"))
# total = a+b+c+d+e+f+g
# print("합계 : ",total)

# 리스트 사용
# # 변수 a,b,c,d,e 의 변수에 숫자를 입력받아 합계를 출력하시오
# a_list = [0,0,0,0,0,0,0]
# total = 0
# for i,a in enumerate(a_list):
# 	a = int(input(f"{i+1}번째숫자를 입력하세요>>"))
# 	total += a
# print("합계 : ",total)


# 리스트 사용 - 리스트변수활용
# # 변수 a,b,c,d,e 의 변수에 숫자를 입력받아 합계를 출력하시오
# a_list = []
# total = 0
# for i in range(10):
# 	j = int(input(f"{i+1}번째 숫자를 입력하세요.>"))
# 	a_list.append(j)
# 	total += j
# print("합계 : ",total)

# 1~100 들어가 있는 리스트 출력
# a_list = []
# total = 0
# for a in range(1,100+1):
# 	a_list.append(a)
# 	total += a
# print("합계 : ",total)


# # 문자열, 숫자-정수 ,숫자-실수, 논리형
# a_list = [1,2,3.0,"안녕",True,False]
# print(a_list[0])
# print(a_list[3])
# print(a_list[-1]) #반대로 => -1 = False, -2 = True, -3 = 안녕 ...


# # 순차 출력
# a_list = [1,2,3,4,5]
# for i in a_list:
# 	print(i)

# # 역순 출력 
# for i in range(5):
# 	print(a_list[-(i+1)])
# # 1 ,2 ,3 ,4 ,5
# # -5,-4,-3,-2,-1
# for i in range(1,5+1):
# 	print(a_list[-i])

# for i in range(len(a_list)):
# 	print(a_list[-(i+1)])

# for i in range(1,len(a_list)):
# 	print(a_list[-i])


# #깊은 복사, 얕은 복사

# a_list = [1,2,3,4,5]
# b_list = a_list  			## 얕은 복사 -> a_list 수정시 b_list 값에도 영향
# a_list[0] = 100
# print(a_list)
# print(b_list)
# print("-"*15)

# a_list = [1,2,3,4,5]
# b_list = a_list[:]  	## 깊은 복사 -> a_list 수정시 b_list 값에도 영향이 없음
# a_list[0] = 100
# print(a_list)
# print(b_list)
# print("-"*15)

# a_list = [1,2,3,4,5]
# b_list = [*a_list]  	## 깊은 복사 -> a_list 수정시 b_list 값에도 영향이 없음
# a_list[0] = 100
# print(a_list)
# print(b_list)
# print("-"*15)

# 리스트 역순 생성
# a_list = [1,2,3,4,5]
# b_list = a_list[::-1]   ### a_list[::-1] 이렇게 쓰면 a_list 와 다른 새로운 주소로 되는 것. a_list의 값을 바꿔도 a_list[::-1]에는 영향이 없음
# a_list[0] = 100
# print(a_list)
# print(b_list)


# # 리스트 출력 방법
# a_list = [1,2,3,4,5] 
# b_list = [50,100]
# print(a_list[3])      # 3째 출력 -> 4
# print(a_list[0:3])		# 0~2번째(3앞)까지 출력 -> 1,2,3
# print(a_list[2:4])		# 2~3번째(4앞)까지 출력 -> 3,4
# print(a_list[:3]) 		# 0~2번째(3앞)까지 출력 -> 1,2,3
# print(a_list[3:]) 		# 3~끝까지 출력 -> 4,5
# print(a_list+b_list)  # -> [1, 2, 3, 4, 5, 50, 100]
# print(b_list * 3)     # b_list 3번 반복 출력 -> [50, 100, 50, 100, 50, 100]
# print(a_list[::2])    # step 2 -> [1, 3, 5]
# print(a_list[::-2])   # 역순 step 2 -> [5, 3, 1]
# print(a_list[::-1])		# 역순 출력 -> [5, 4, 3, 2, 1]
# print(a_list[:])			# 전체 출력 -> [1, 2, 3, 4, 5]
# print(a_list)					# 전체 출력 -> [1, 2, 3, 4, 5]


# # 리스트 수정 방법
# a_list = [1,2,3,4,5,6,7]
# a_list[3] = 50				 # 1개 변경
# a_list[1:2] = [20,30]  # 2개 변경 [1:2] -> (1,2번 변경) = [20,30]
# a_list[4] = [10,20]		 # 리스트 안에 리스트로 변경
# # 리스트 안에 리스트 = 2차원 리스트
# print(a_list)


# # 리스트 삭제 명령어 사용 - del
# a_list = [1,2,3,4,5]
# del a_list[0]				# 0번째 리스트 삭제 -> [2, 3, 4, 5]
# print(a_list)

# 리스트 삭제
# a_list = [1,2,3,4,5]
# a_list = []					# 전체 삭제(가장 많이 씀)
# a_list = None				# 전체 삭제
# del(a_list)  				# a_list 자체를 삭제 -> 프린트 할 수 없음
# a_list[1:3] = []    # 2개 삭제 시(1~2번째) -> [2, 5]
# print(a_list)

# 리스트 함수
# a_list = [1,2,3,4,3,5,60,3,70,3]
# 리스트 함수 - 추가
# a_list.append(200)				 # 맨 뒤에 값 추가
# a_list.insert(0,100)  		 # index 위치에 해당 값 저장

# 리스트 함수 - 삭제
# a_list.pop(2)   					 # 해당 index의 위치 삭제
# del a_list[3]							 # 해당 위치의 리스트 삭제
# a_list.remove(5)		 			 # 입력된 값의 리스트 삭제
# a_list.clear()   					 # 전체 삭제

# print(len(a_list)) 				 # 리스트 갯수  -> 7
# print(a_list.remove(5))		 # remove()출력 못함
# print(a_list.count(3))		 # 입력된 값의 존재 갯수 확인
# print(a_list)
