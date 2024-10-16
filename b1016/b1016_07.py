# 예외처리
# 오류 
# 구문오류 - 프로그램실행 전 발생하는 오류
# 런타임오류/예외 - 프로그램 실행 중 발생하는 오류

# while True:
# 	print("안녕, 숫자입력해줘")
# 	nstr = input("숫자만 입력가능 >> ")

# 	if nstr.isdigit():
# 		# print("숫자로 변환 가능")
# 		num = int(nstr)
# 		print("입력숫자 :",num)
# 	else:
# 		print("숫자로 변환 불가능")
# 	# num = int(input("숫자만 입력가능 >> "))




## try, except - 프로그램 예외를 처리하는 명령어
# try - 예외가 발생할 가능성이 있는 코드
# except - 예외가 발생했을 때 실행할 코드

# while True:
# 	score = 100
# 	print("[나눗셈 프로그램]")
# 	nstr = input("숫자만 입력가능 >> ")

# 	# 숫자가 아닌 것을 입력하면 에러
# 	# 0을 입력하면 에러
# 	try:
# 		num = int(nstr)
# 		print("입력된 숫자로 100을 나눔 :",score/num)
# 		# 나눗셈은 0으로 나누면 에러남
# 	except:
# 		print("숫자로 변환 불가능")
# 	# num = int(input("숫자만 입력가능 >> "))


try:
	print("입력 숫자 :",int(input("숫자 입력 >> ")))
except:
	pass