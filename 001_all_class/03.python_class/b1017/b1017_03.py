
# try-except 예외처리  => try에 에러가 발생하면 except를 실행
# try-except-else  => else는 try구문에 에러가 없으면 실행
# try-except-finally  => try가 에러 발생여부에 상관없이 finally 무조건 실행

# print("파일 open")
# try:
# 	print("글쓰기1")
# 	print("글쓰기2")
# 	print("글쓰기3")
# 	print("str - > 딕셔너리 입력 4")  #에러
# 	print("글쓰기5")
# 	print("글쓰기6")
# 	# print("파일 close")
# except:
# 	print("잘못된 타입이 들어왔습니다.")
# 	# print("파일 close")
# finally:
# 	print("파일 close")

# print("프로그램 종료")


# f =  open('C:/workspace/smclass/b1017/a.txt','w',encoding='utf-8')
# try:
# 	f.write("안녕하세요1\n")
# 	f.write("안녕하세요2\n")
# 	f.write("안녕하세요3\n")
# 	f.write({"a":1})
# 	f.write("안녕하세요4\n")
# except Exception as e:
# 	print(e)
# finally:
# 	f.close()





numbers = [52,273,32,103,90,10,275,1,2,1,2,12]
try:
	print(numbers.index(52))
	print(numbers.index(1))
	print(numbers.index(3))
	print(numbers.index(32))
	print(numbers.index(90))
except Exception as e:
	print("찾는 번호가 없습니다.",type(e))




# print("1")
# try:	# try 구문에 에러가 발생해야 except를 실행시킴
# 	print("2")
# 	# print(3/0)
# 	print("3")
# 	print("4")
# except:
# 	print("5")
# 	print("6")
# else:
# 	print("에러가 발생하지 않으면 실행")
# finally:
# 	print("finally 실행됨")

# print("7")
# print("8")


# print("1")
# try:	# try 구문에 에러가 발생해야 except를 실행시킴
# 	print("2")
# 	# print(3/0)
# 	print("3")
# 	print("4")
# except:
# 	print("5")
# 	print("6")
# else:
# 	print("에러가 발생하지 않으면 실행")

# print("7")
# print("8")


# list_a = [1,2,3,4,5,'홍길동']
# list_b = []

# # 숫자에 *2를 하는 프로그램을 구현하시오
# try:
# 	for a in list_a:
# 		list_b.append(a**2)
# except Exception as e:
# 	print(e)

# print(list_b)



# print("프로그램 시작")
# try:
# 	# print("프로그램 시작)  #구문오류 - 프로그램 실행전에 오류
# 	print(list_a)   #런타임오류 - 프로그램 실행중에 오류

# except:
# 	print("에러 발생!")

# print("프로그램 종료")
# n_str = input("반지름를 입력하세요.>> ")
# try:
# 	num = int(n_str)

# 	# 원의 넓이, 원 둘레 
# 	print("원의 넓이 :",(num**2)*3.14)
# 	print("원의 둘레 :",num*2*3.14)
# except Exception as e :
# 	print("정수가 아님. 다시 입력하세요.",e)


# if n_str.isdigit():
# 	num = int(n_str)

# 	num = int(input("반지름를 입력하세요.>> "))

# 	# 원의 넓이, 원 둘레 
# 	print("원의 넓이 :",(num**2)*3.14)
# 	print("원의 둘레 :",num*2*3.14)
# else:
# 	print("정수가 아님. 다시 입력하세요.")