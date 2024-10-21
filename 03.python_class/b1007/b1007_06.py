import random

# 25개의 1차원 리스트

# 25개 중 1을 5개 나머지는 0으로 입력해서 출력하시오
a_list = [0]*20+[1]*5
random.shuffle(a_list)
print(a_list)

# [5,5] 2차원 리스트에 a_list의 값을 입력한 후 출력하시오
b_list = []
for i in range(5):
	a = []
	for j in range(5):
		a.append(a_list[5*i+j])   # a_list 5개를 a 리스트에 추가 -> 0,1,2,3,4,----,23,24
	b_list.append(a)						# a 리스트를 b_list 에 추가
print(b_list)

# b_list = []
# for i in range(0,len(a_list),5):
# 	b_list.append(a_list[i:i+5])
# print(b_list)

# [5,5] 출력
while True:
	print("\t0\t1\t2\t3\t4")
	print("ㅡ"*22)
	for i in range(5):
		print(i,end='\t')
		for j in range(5):
			print(b_list[i][j],end='\t')
		print()

	num = input("좌표 입력(0,0)>>")
	num2 = num.split(",")
	print(f"{num} 좌표의 값 : {b_list[int(num2[0])][int(num2[1])]}")



# 0:20개 1:5개 생성

# a_list = []
# for i in range(25):
# 	if i < 5:
# 		a_list.append(1)
# 	else:
# 		a_list.append(0)
# print(a_list)