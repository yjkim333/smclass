from urllib import request

target = request.urlopen("http://www.google.com")
output = target.read()

print(output)



# # from SS import *
# import SS
# # import math
# # from math import *
# import math as m  # as 닉네임

# students = [
# 	{"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
# 	{"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
# 	{"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
# 	{"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
# 	{"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
# ]


# # SS모듈 함수 호출
# SS.stu_output(students)
# print(SS.s_title)  # s_title이 이 파일에 없어도 SS에서 import로 다 가져와있는 상태라 출력됨

# # print(math.floor(1.23))
# print(m.ceil(1.23))   # 올림
# print(m.floor(1.23))	# 버림
# print(round(1.23))	# 반올림