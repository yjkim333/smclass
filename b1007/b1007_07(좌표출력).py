import random
lotto = [0]*6+[1]*3
random.shuffle(lotto)

a_list = [
	[0,1,0],
	[0,0,1],
	[1,0,0]
]
for i in range(3):
	for j in range(3):
		a_list[i][j] = lotto[3*i+j]
		

aa_list = [
	["로또","로또","로또"],
	["로또","로또","로또"],
	["로또","로또","로또"]
]

while True:
	my_money = int(input("얼마 배팅할래?>>"))

	print("        [i,j 좌표]")
	print("\t0\t1\t2")
	print("ㅡ"*14)
	for i in range(3):
		print(i,end=' |\t')
		for j in range(3):
			print(aa_list[i][j],end='\t')
		print()
	
	print()
	code = input("좌표를 입력하세요(0.0)>>")
	codeArr = code.split(".")  #codeArr[0] 와 codeArr[1]
	print(f"{codeArr} 좌표값 : ",a_list[int(codeArr[0])][int(codeArr[1])])
	print()
	if a_list[int(codeArr[0])][int(codeArr[1])] == 1:
		aa_list[int(codeArr[0])][int(codeArr[1])] = "당첨"
		print(f"당첨!! 당첨금 - {my_money*10:,d}")
	else:
		aa_list[int(codeArr[0])][int(codeArr[1])] = "꽝"
		print(f"꽝..다음기회에...더 투자하세요. 날린 돈 : {my_money}")
	print()


	