import random
lotto = [0]*6+[1]*3
random.shuffle(lotto)
# print(lotto)

a_list = []
for i in range(3):
	a = []
	for j in range(3):
		a.append(lotto[3*i+j])
	a_list.append(a)
# print(a_list)

print("\t0\t1\t2")
print("ㅡ"*16)
for i in range(3):
	print(i,end=' |\t')
	for j in range(3):
		print(a_list[i][j],end='\t')
	print()

code = input("좌표입력 (0.0)>>")
cArr = code.split(".")
# print(cArr)
print(f"좌표의 값 : "{a_list[int(cArr[0])][int(cArr[1])]})
