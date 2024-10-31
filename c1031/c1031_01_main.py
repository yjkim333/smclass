import func


while True:
	## 시작화면 함수 호출
	choice = func.screen()

	## 1. 로그인 함수 호출
	if choice == '1':
		func.memLogin()

	## 2. 비밀번호 찾기 함수 호출
	elif choice == '2':
		func.search_pw()

	elif choice == '3':
		print("  [  회원가입  ]  ")
		


	elif choice == '0':
		print("  --- 프로그램 종료 ---  ")
		break
	