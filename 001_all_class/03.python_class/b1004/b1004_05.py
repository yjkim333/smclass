# for문을 출력
for k in range(1,10):
	print(f"[ {k} 단 ]",end='\t')
print()

for i in range(2,10):
	for j in range(1,10):
		print(f"{j} x {i} = {j*i}",end="\t")
	print()

# # for문을 출력
# for i in range(2,10):
# 	print(f"[ {i}단 ]")
# 	for j in range(1,10):
# 		print(f"{i} x {j} = {i*j}",end=" ")
# 	print()


# 000, 001,...,999까지 출력
# for i in range(0,10):
# 	print(f"00{i}")
# for j in range(11,100):
# 	print(f"0{j}")
# for k in range(101,1000):
# 	print(k)

# for i in range(10):
# 	for j in range(10):
# 		for k in range(10):
# 			print(f"{i:03d},{j:03d},{k}")

# for i in range(1000):
# 	print(f"{i:03d}")

# # 구구단 입력한 단까지 출력 3->1,2,3
# num = int(input("몇 단까지?"))
# print("[1단 ~",num,"단]")
# for i in range(1,num+1):
# 	for j in range(1,9+1):
# 		print(f"{i}x{j} = {i*j}")
# 	print("ㅡ"*5)
