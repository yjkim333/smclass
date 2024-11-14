# a = 1
# b = 2

# a_list = [a,b]
# print(a_list)
# print(type(a_list))

# b_list = [b]
# print(type(b_list))


# a_tuple = (a,b)
# print(type(a_tuple))

# 튜플을 한개만 지정할 때는 뒤에 , 넣어야 함.
# b_tuple = (a)  # -> int 타입     -> , 하나 붙이면 튜플 타입됨
# c_tuple = (a,) # -> 튜플 타입
# print(type(b_tuple))
# print(c_tuple)
# print(type(c_tuple))

# -----------------------------------------------------------------------------------

# sql = "select * from employees where emp_name like '%a%"

# name = '홍길동'
# # 문자 변수 출력
# print('안녕하세요. 이름은 %s입니다.'%name)
# # format함수
# print("Hi. My name is {}".format(name))
# # 문자 f 함수
# print(f"Hi. My name is {name}")

# -----------------------------------------------------------------------------------

title = ['e_id','e_name','salary']
aa = [
	(185, 'Alexis Bull', 4100.0),
	(107, 'Diana Lorentz', 4200.0),
	(184, 'Nandita Sarchand', 4200.0),
	(106, 'Valli Pataballa', 4800.0),
	(105, 'David Austin', 4800.0)
]

a_list = []
for a in aa:
	s = (dict(zip(title,a)))
	# print(s)
	a_list.append(s)

print(a_list)


a_list = [dict(zip(title,a)) for a in aa]
print(a_list)
  


