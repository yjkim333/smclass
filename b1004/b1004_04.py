# a = [1,2,3,4,5]
# b = [*a] # a 복사
# c = a

# c = 100
# d = c

# d = 1

# b[1] = 100

# print(a)
# print(c)

# 두 수를 입력받아 두 수사이 숫자의 합계를 구하시오
# # 1) if문 사용
# num = int(input("숫자1 : "))
# num2 = int(input("숫자2 : "))
# min_num = num; max_num = num2
# if num>num2:
# 	min_num = num2
# 	max_num = num

# sum = 0
# for i in range(min_num,max_num+1):
# 	sum += i
# print(sum)


# # 2) min,max 함수 사용
# num = int(input("숫자1 : "))
# num2 = int(input("숫자2 : "))
# # min_num = min(num,num2); max_num = max(num,num2)
# sum = 0
# # for i in range(min_num,max_num+1):
# # 	sum += i
# # print(sum)
# for i in range(min(num,num2),max(num,num2)+1):
# 	sum += i
# print(sum)


# # 3)if문 사용
# num = int(input("숫자1 : "))
# num2 = int(input("숫자2 : "))
# if num>num2:
#  num,num2 = num2,num # 파이썬만 가능 -두 개의 변수 치환 가능

# sum = 0
# for i in range(num,num2+1):
# 	sum += i
# print(sum)

# # 3-1)if문 사용 - 다른 언어에서는 이렇게 파이썬도 가능
# num = int(input("숫자1 : "))
# num2 = int(input("숫자2 : "))
# c = 0
# if num>num2:
# 	c=num
# 	num=num2
# 	num2=c

# sum = 0
# for i in range(num,num2+1):
# 	sum += i
# print(sum)




# 1~100까지 숫자의 합을 구하시오
# sum = 0
# for i in range(1,100+1):
# 	sum += i
# print("합계",sum)

# 1,3,5,7,9,...99 합계
# 1)
# sum =0
# for i in range(1,99+1):
# 	if i%2 != 0:
# 		sum += i
# print(sum)
# 2)
# sum = 0
# for i in range(1,99+1,2):
# 	sum += i
# print(sum)



# 0:안녕하세요,1:안녕하세요...
# for i in range(3):
# 	print(f"{i}:안녕하세요")

# for _ in range(3):
# 	print("안녕하세요.")

# for i in [1,2,3]:
# 	for j in range(i):
# 		print("안녕하세요")
# 	print("-")

# for i in [1,2,3]:
# 	print("안녕하세요.\n"*i,end="")
# 	print("-")

# for i in range(2):
# 	print(i)

# for문 사용으로 *,**,***,****,*****
# for i in range(5,0,-1): # -1씩 감소 -> 반대로
# 	print("*"*i)

# for i in range(1,5+1):
# 	print("*"*i)

# for i in range(1,5+1):
# 	for j in range(5):
# 		print("*"*5)


# 구구단 1,3,5,7,9 출력
# for i in range(1,9+1,2): # range(시작값,끝값+1,증가값)
# 	print(f"[ {i}단 ]")
# 	for j in range(1,9+1):
# 		print(f"{i}x{j} = {i*j}")
# 	print("*"*10)
 
# for i in range(1,9+1):
# 	if i%2 != 0:
# 		print(f"[ {i}단 ]")
# 	for j in range(1,9+1):
# 		print(f"{i}x{j} = {i*j}")
# 	print("*"*10)

# 구구단을 출력하시오.
# for i in range(2,9+1):
# 	print(f"[ {i}단 ]")
# 	for j in range(1,9+1):
# 		print(f"{i}x{j} = {i*j}")
# 	print("ㅡ"*4)

# 1,3,5,7,9 까지 출력하시오.
# for i in range(1,10,2):
# 	print(i)

# for i in range(10):
# 	if i%2 != 0:
# 		print(i)

# 1에서 10까지 for문으로 출력
# for i in range(1,10+1):
# 	print(i)