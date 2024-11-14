fName = ['바나나','오렌지','체리','파인애플','코코넛']
fruit = {"바나나":"banana","오렌지":"orange","체리":"cherry","파인애플":"pineapple","코코넛":"coconut"}

# 바나나를 입력하면 영어로 banana라고 출력
# print(fruit['바나나'])
# print(fruit['오렌지'])
# while True:
# 	search = input("과일 입력>> ")
# 	if search in fruit:
# 		print("영문 :",fruit[search])
# 	else:
# 		print("찾는 과일 없음")



# 

# print("[  영단어 맞추기  ]")
# 	search = input("바나나의 영문을 입력하세요.>> ")
# 	if fruit['바나나'] == search:
# 		print("정답입니다.",fruit['바나나'],search)
# 	else:
# 		print("오답입니다.",fruit['바나나'],search)

# fName에 있는 순서대로 영문퀴즈 시작
# print("[  영단어 맞추기  ]")
# for key in fruit.keys():
# 	search = input(f"{key}의 영문을 입력하세요.>> ")
# 	if fruit[key] == search:
# 		print("정답입니다.","정답:",fruit[key],"나:",search)
# 	else:
# 		print("오답입니다.","정답:",fruit[key],"나:",search)



import random

fName = ['바나나','오렌지','체리','파인애플','코코넛']
fruit = {"바나나":"banana","오렌지":"orange","체리":"cherry","파인애플":"pineapple","코코넛":"coconut"}

# random.shuffle(fName) # 원본이 변경됨 -> 원본이 지켜져야 할 땐 쓰면 안됨
# for i in range(5):
# 	ran = fName[random.randint(0,4)]
# 	print(ran)

# fName 랜덤 순서로 영문퀴즈 시작
# re_fName = random.sample(fName,5)  # -> fName에서 5개 가져올게
# for i in re_fName:
# 	search = input(f"{i}의 영문을 입력하세요.>> ")
# 	if fruit[i] == search:
# 		print("정답입니다.","정답:",fruit[i],"나:",search)
# 	else:
# 		print("오답입니다.","정답:",fruit[i],"나:",search)


fruit = {"바나나":"banana","오렌지":"orange","체리":"cherry","파인애플":"pineapple","코코넛":"coconut"}
# fName = ['바나나','오렌지','체리','파인애플','코코넛']
fName = list(fruit.keys())
print(fName)