a = ['1', '홍길동', '100', '100', '99', '299', '99.67', '0']
b = ['1', '100', '100', '99', '299', '99.67', '0']
t_title = ['no','name','kor','eng','math','total','avg','rank']
students = []

def f_float(value):
	if value.isdigit():  # 정수인지, 실수나문자열인지
		return int(value) # 정수일때는 정수로 변환
	else:
		try:
			return float(value) # 실수일때는 실수로 변환
		except:
			return value # 문자열 일때 문자열 그대로 리턴


c = []
for idx,value in enumerate(a):
	c.append(f_float(value))

students.append(dict(zip(t_title,c)))
print(students)



# for idx,value in enumerate(b):
# 	# isdigit()  -> 정수이면 True, 실수이면 False
# 	if value.isdigit():
# 		print(f"{idx}번째 {type(int(value))}")
# 	else:
# 		print(f"{idx}번째 {type(float(value))}")



# b의 리스트 float 변경
# b의 형태가 모두 숫자기 때문에 -> float 변경
# for i in b:
# 	c.append(float(i))
# print(c)


# # try-except 구문을 사용해서 정수,실수 구분
# def t_float(n):
# 	try:
# 		int(n)
# 		return True
# 	except:
# 		return False
	

# # 문자열 인지 아닌지 구분
# for idx,i in enumerate(a):
# 	if i.isdigit():
# 		print(f"{idx}번째 {i}는 숫자 입니다.")
# 	else:
# 		print(f"{idx}번째 {i}는 문자입니다.")


# # 정수로 변경
# for i in b:
# 	if t_float(i):
# 		i = int(i)
# 	else:
# 		i = float(i)
# 	c.append(i)

# print(c)