#변수 bool(불형(boolean), true, false), int(정수), float(실수), str(문자열)
#대소문자 구분, 문자, 숫자, _(언더바)만 쓸 수 있지만, 숫자로 시작할 수 없다.

# name,kor,eng,math,total,avg 출력
#홍길동,100,100,99를 input으로 입력 받아합계,평균(소수점 둘 째 자리)을 한 줄에 출력
#format, f함수 사용

name = input("이름을 입력하세요.")
kor = input("국어점수 입력하세요.")
#kor = int(input("국어점수 입력하세요."))
eng = input("영어점수 입력하세요.")
math = input("수학점수 입력하세요.")
total = int(kor)+int(eng)+int(math)
avg = total/3
print(f"{name},{kor},{eng},{math},{total},{avg:.2f}")
print("{},{},{},{},{},{}".format(name,kor,eng,math,total,avg))





# a = '100'
# b = "200"
# print(type(a))
# print(type(b))

# print(a+b) #문자 연결 연산자 100200
# print(int(a)+int(b)) # 타입변경
# name = "홍길동"
# #print(int(name)) #에러.문자를 숫자로 변경 불가능 / 문자정수는 변경가능
# c = "3.14"
# print(int(float(c))) #문자숫자를 실수형으로 변경후 정수형으로 변경
# #print(int(c)) #에러.문자실수형은 정수로 바로 변경은 불가

# d = 3.14
# print(str(d))  #실수형을 문자열로 변경

# e = "True"
# print(bool(e)) #문자 불형을 불형으로 변경

# #타입 변경 - str, float, int, bool


# name = "홍길동"
# print(type(name)) #타입체크

# level = '3레벨'
# print(type(level))

# n = 3.14
# print(type(n))

# num = 100
# print(type(num))

# a_bool = True # True, False : 대문자T,F로 넣어야 함**(파이썬만)
# print(type(a_bool))

#var1 = 100
#var2 = var1
#var3 = var2
#var4 = var3
#print(var4)

#v4 = v3 = v2 = v1 =10
#print(v4)