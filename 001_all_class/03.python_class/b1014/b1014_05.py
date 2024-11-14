# # 구구단 출력
# def gugudan(n1,n2):
# 	for i in range(n1,n2+1):
# 		print(i,"단")
# 		for j in range(1,9+1):
# 			print(f"{i} x {j} = {i*j}")

# # 2~5단
# print("[ 2~5단 ]")
# gugudan(2,5)

# # for i in range(2,5+1):
# # 	print(i,"단")
# # 	for j in range(1,9+1):
# # 		print(f"{i} x {j} = {i*j}")

# # # 3~9단
# # print("[ 3~9단 ]")
# # for i in range(3,9+1):
# # 	for j in range(1,9+1):
# # 		print(f"{i} x {j} = {i*j}")

# # # 5~8단
# # print("[ 5~8단 ]")
# # for i in range(5,8+1):
# # 	for j in range(1,9+1):
# # 		print(f"{i} x {j} = {i*j}")


# 배열 활용
# # 구구단 출력
# def gugudan(n):
# 	for i in range(2,n+1):
# 		print(i,"단")
# 		for j in range(1,9+1):
# 			print(f"{i} x {j} = {i*j}")

# nArr = [9,5,7]
# # 2단 부터 배열에 있는 숫자까지 구구단 출력
# for n in nArr:
# 	gugudan(n)
# 	print("."*20)



subName = ['국어','영어','수학']
score = {'국어':100,'영어':95,'수학':80}
# print(score)
# print(score['국어'])
# print(subName[0])
# print(score[subName[0]])
for i in subName:
	print(f"{i} : {score[i]}")

for k,v in score.items():
	print(k,":",v)