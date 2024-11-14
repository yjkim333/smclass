# 리스트 타입
# 튜플 타입 - 수정이 불가능함
# 딕셔너리 타입


# ##딕셔너리
# key and value -> json의 구조와 같음
# {key:value, key:value} 사용

dic1 = {"번호":1,"이름":"홍길동","kor":100,"eng":100}
print(dic1)

# 출력방법 - 키를 입력하면 값을 출력 
print(dic1["이름"])
print(dic1.get("이름"))
print(dic1.get("학번"))   #없는 키를 입력하면 None 출력, 에러는 나지 않음
# print(dic1['합계'])     # 없는 키를 출력하면 에러

# 딕셔너리 추가 방법 - 없는 키와 값을 입력하면 추가
dic1["math"] = 90
print(dic1)

# 딕셔너리 값 수정 - 있는 키와 값을 입력하면 수정
dic1["kor"] = 50
print(dic1)

# 딕셔너리 삭제 방법 - del(키) 입력하면 삭제
del(dic1["eng"]) 
print(dic1)

if dic1.get("이름") != None:
	print(dic1.get("이름"))

print(dic1.keys()) #모든 키값을 출력
print(type(dic1.keys()))
# 모든 키 값만 출력 - keys()
for key in dic1.keys():
	print(key,dic1[key])  #키 밸류 출력
	print(dic1[key])			#밸류만 출력

# type : class 객체
print(type(dic1.keys()))
# class 객체를 리스트 타입으로 변경
list(dic1.keys())
print(type(list(dic1.keys())))
print(list(dic1.keys()))
print(list(dic1.keys())[0])
# print(dic1.keys()[0]) - 에러 - 객체타입이기때문

# value 값만 출력 - values()
# values() 의 타입 : class객체
print(dic1.values())
print(list(dic1.values()))

# 키와 값을 모두 출력 - items()  -> 튜플타입으로 나옴 (수정이 불가능)
print(dic1.items())
print(list(dic1.items()))

# key 만 추출
for key in dic1:
	print(key)

# value만 추출 
for key in dic1:
	print(dic1[key])

# key, value 추출
for key,val in dic1.items():
	print(key,val)

# dic1에 '평균'이 없으면 넣어라
if '평균' not in dic1:
	dic1['평균'] = 99.0
print(dic1)



# a_list = [1,'홍길동',100,100,100,300,100.0,1]
# 리스트는 안의 값이 뭔지 잘 모름 -> 딕셔너리 사용

# 리스트
# a_list = [1,2,3,'홍길동']
# 출력방법 위치값
# print(a_list[0])  #-> 1
# 추가
# append(),insert(),extend()