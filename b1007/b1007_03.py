# # 2차원 리스트
# a_list = [
# 	[1,2,3,4],
# 	[5,6,7,8],
# 	[9,10,11,12]
# ]

# # 2차원리스트 -> for문을 2번 사용
# for i in a_list:
# 	for j in i:
# 		print(j)


# 1~9를 b_list에 for문을 사용해서 1차원 리스트로 추가하시오
# b_list = []
# for i in range(1,10):
# 	b_list.append(i)
# print(b_list)


# [3,3] 리스트 [1,2,3],[4,5,6],[7,8,9]
# 1~9를 a_list에 for문을 사용해서 2차원 리스트로 추가하시오
# a_list = []
# for i in range(0,3):
# 	a = []
# 	for j in range(0,3):
# 		a.append(3*i+j+1) #3x+y
# 	a_list.append(a)
# print(a_list)


# for문을 2번 써서 1~25 수를 5,5 리스트를 생성하세요.
a_list = []
for i in range(0,5):
	a = []
	for j in range(5):
		a.append(5*i+j+1)
	a_list.append(a)
print(a_list)





# print(a_list)