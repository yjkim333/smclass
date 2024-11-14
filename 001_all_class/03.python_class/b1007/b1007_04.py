import random

# 1~25 사이의 랜덤 숫자를 생성해서 출력하시오
# num = int(random.random()*25)+1
# num = random.randint(1,25)
# a_list = []
# 1~25 사이의 랜던 숫자를 a_list에 입력, 중복 제외
# 25번 반복
# a_list = []
# 중복제외 숫자 25개 넣기
# while True:
# 	for i in range(25):
# 		num = random.randint(1,25)
# 		if num not in a_list:
# 			a_list.append(num)
# 	if len(a_list) == 25:
# 		break
# print(a_list)

# 중복제외 숫자 25개 넣기
# while len(a_list)<25:
# 	for i in range(25):
# 		num = random.randint(1,25)
# 		if num not in a_list:
# 			a_list.append(num)		
# print(a_list)

# 중복 제외 랜덤 숫자 넣기
# for i in range(25):
# 	num = random.randint(1,25)
# 	if num not in a_list:
# 		a_list.append(num)		
# print(a_list)


# 1~25 사이 랜덤으로 배치 - 
# random.sample() - 범위리스트,25개 추출(중복 추출 안됨)
a_list = []
for i in range(25):
	a_list.append(i+1)

# random.sample()
# b_list = random.sample(a_list,25) # a_list 에 있는 숫자 25개를 랜덤으로 뽑아라
# print(b_list)

# 1~25 사이 랜덤으로 배치 - random.choices()
# 범위리스트,25개 추출(중복)
b_list = random.choices(a_list,k=25)
print(b_list)