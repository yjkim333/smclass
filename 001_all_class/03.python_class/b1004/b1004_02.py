import random
# 랜덤숫자 : 1-100
# random.randint(1,100)

# 10번 도전에서 입력한 숫자가 더 크면 작은수 입력하세요. 더 작으면 더 큰수 입력하세요. 10번 도전 실패하면 10 번도전에 실패 했습니다. 정답: ,도전 성공 도전에 성공했습니다.

r_num = random.randint(1,100)
i = 0
trial = 10
while i<10:
	i_num = int(input(f"숫자를 입력하세요."))
	if i_num < r_num:
		print(i+1,"번째 도전 -> 더 큰 수를 입력해보세요.")
		i += 1
	elif i_num > r_num:
		print(i+1,"번째 도전 -> 더 작은 수를 입력해보세요.")
		i += 1
	else:
		print("도전에 성공했습니다!")
		break
if i >= 10:
	print("도전에 실패했습니다. 정답은 ",r_num)
	
