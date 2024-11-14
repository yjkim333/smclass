# try-except-else-finally

# 리스트의 범위 밖 호출 에러 : IndexError
# 입력된 값의 변환 에러 : ValueError

# list1 = [52,273,132,72,100]

# try:
# 	n_input = int(input("리스트 순번 값 입력 >> "))
# 	print(f"{n_input}번째 리스트의 값 : {list1[n_input]}")
# except IndexError as e:
# 	print("번호가 범위를 벗어났습니다.")
# 	print(type(e))
# 	print("e :",e)
# except ValueError as e:
# 	print("정수가 입력되지 않았습니다.")
# 	print(type(e))
# 	print("e :",e)
# except Exception as e:						#index,value 에러 밖의 에러가 발생 할 수 있기 때문에 마지막에 넣어둔다. 
# 	print("모든 예외 처리의 부모")		# Exception은 모든 에러의 부모
# finally:
# 	pass


# raise 키워드  -  강제 예외 발생

print("program start")
print("1")
print("2")
try:
	print("3")
	print("4")
	# 강제 에러 발생  ->  개발 중 아직 미구현된 부분을 나중에 잊지 않고 할 수 있게 만듦
	raise NotImplementedError("!!프로그램 구현해야함!!")  # 프로그램이 구현되어 있지 않음
	# print(10/0)  # 강제 에러 발생
	print("5")
except Exception as e:
	print(e)
	print("6")
	print("7")
finally:
	print("8")
	print("9")
print("10")
print("program end")