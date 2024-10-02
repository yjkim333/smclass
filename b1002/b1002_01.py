# 문자열

# 문자열숫자
a = "123"
print(type(a))         #str
print(type(int(a)))    #int
print(type(float(a)))  #float

b = "12.3"
#print(type(int(b)))  -> 에러 - 소수점이 있는 문자열 숫자는 float으로 변경해야함
print(type(float(b))) #float

# 문자열 연결연산자
s1 = "안녕"
s2 = "안녕하세요"
print(s1+s2)
print(a+b)   #-> 문자열 연결연산자 +
#print(a*b)   -> 에러 - 문자열은 -,*,/ 불가

# 문자열 * 2  -> 문자열 반복연산자
print("안녕"*10) 
print("ㅡ.."*10)

# 문자열 슬라이싱
str1 = "안녕하세요, 반갑습니다." # 문자열자체를 리스트(배열)의 형태로 본다 ['안''녕''하']
print(str1[7])   # 해당번호 넣으면 해당되는 문자 출력
print(str1[2:5]) # 해당범위 출력 [2:5] [시작 위치점:끝나는점 위치 한칸 뒤]
print(str1[:5])  # [:5] [처음부터:숫자 앞까지]
print(str1[2:])  # [2:] [위치:끝까지]
print(str1[1:10:2])  #[위치:숫자 앞까지의 위치:2칸씩(step2)]
print(str1[1:10:3])  #[위치:숫자 앞까지의 위치:3칸씩(step3)]
print(str1[::-1]) # [처음부터:끝까지:역순으로]

# [] - 배열 : 배열은 한 번 범위가 정해지면 수정이 불가 : c, 자바
# [] - 리스트 (파이썬에선 배열을 리스트라고) : 범위 상관 없음



c = 12.3
print(type(int(c)))  #실수는 int타입으로 변경이 가능
print(int(c))


## if
# 

# input_str = input("글자입력")

# # 문자가 입력되지 않았을 때 if
# if input_str != "":  # != : 같지 않다
#   print("입력문자 : ",input_str)
#   print("프로그램이 종료됩니다.")
# else:
#   print("글자를 입력하셔야 합니다.")

# 자바스크립트 if문
# if(){

# }else{

# }

# and -> 둘 다 참이어야 참, 한 개라도 False 면 False
# or -> 둘 중 하나만 참이어도 참, 둘다 false 면 False
# not -> 부정(반대), 참이면 False, 거짓이면 True