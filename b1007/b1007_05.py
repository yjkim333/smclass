import random

# 1~25까지 랜던숫자 25개를 중복 없이 추출해서
# (5,5)2차원 리스트에 입력해서 출력

#####다시#####
# a_list = []
# for i in range(25):
# 	a_list.append(i+1)
# b_list = random.sample(a_list,25)
# print(b_list)

# c_list = []
# for i in range(0,len(b_list),5):
# 	c_list.append(b_list[i:i+5])
# print(c_list)


# a_list = []
# while len(a_list)<25:
# 	num = random.randint(1,25)
# 	if num not in a_list:
# 		a_list.append(num)

# b_list = []
# for i in range(5):
# 	a = []
# 	for j in range(5):
# 		a.append(a_list[5*i+j]) # 0,1,2,3,4
# 	b_list.append(a)
# print(b_list)


a_list = []
for i in range(25):
	a_list.append(i+1)
print(a_list)

random.shuffle(a_list)  # 리스트에 있는걸 랜덤으로 섞어준다
print(a_list)

# 0~25까지 5씩 증가 -> (0,25,5)
b_list = []
for i in range(0,len(a_list),5):
	b_list.append(a_list[i:i+5])
print(b_list)

# b_list 랜덤으로 섞어서 1~25 까지 [5,5] 2차원 리스트
while True:
	print("\t0\t1\t2\t3\t4")
	print("-"*50)
	for i in range(5):
		print(i,end='ㅣ\t')
		for j in range(5):
			print(b_list[i][j],end = '\t')
		print()
	input1 = input("좌표입력[0,1]>>")
	input2 = input1.split(",")
	print(input2)
	print(f"{input1}좌표의 값 : ",b_list[int(input2[0])][int(input2[1])])