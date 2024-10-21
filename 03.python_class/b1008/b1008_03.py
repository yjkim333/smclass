# 25개 1차원 리스트 -> 1~25까지 입력, 그 후 랜덤으로 다시 출력
# 5x5 2차원 리스트에 입력 후 출려
import random

aArr=[]
for i in range(25):
	aArr.append(i+1)
random.shuffle(aArr)
print(aArr)

a_list = []
for i in range(5):
	a=[]
	for j in range(5):
		a.append(aArr[5*i+j])
	a_list.append(a)
print(a_list)

# 5*5 리스트 출력
while True:
	print("\t0\t1\t2\t3\t4")
	print("ㅡ"*25)
	for i in range(5):
		print(i,end='|\t')
		for j in range(5):
			print(a_list[i][j],end='\t')
		print()

	# re = input("좌표 입력 (0.0) >>")
	# result = re.split(".")
	# print(f"{re} 좌표 값 : ",a_list[int(result[0])][int(result[1])])

	# 값을 입력하면, 해당 좌표를 출력하시오
	re = int(input("숫자 입력(1~25)>>"))
	if  1 > re or re > 25:
		print("1~25사이의 숫자만 입력하세요.")
		continue
	for i in range(5):
		for j in range(5):
			if a_list[i][j] == re:
				print(f"좌표값 : [{i,j}]")
				a_list[i][j] = 0
				break

