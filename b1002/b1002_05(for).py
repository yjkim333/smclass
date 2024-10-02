students = [
  [1,'홍길동',100,90,99],
  [2,'유관순',100,100,99],
  [3,'이순신',100,100,99]
]

# print(students)
# print(len(students))

# 반복문
for i in range(10): # 시작 : 0 에서 10번 반복
  print(i)

for i in range(2,5): # 시작 : 2 부터 5 이전(4)까지 반복
  print(i)

for i in range(1,10,2): # 시작 :1 부터 10이전까지 step2로 출력
  print(i)

aArr = [1,2,5,7,8] # list의 값을 1개씩 가져와서 출력
for i in aArr:
  print(i)

# enumerate -> index 번호를 추가해서 가져올 수 있음.
for i,data in enumerate(aArr):  # list에 있는 값과 index번호를 함께 출력  aArr의 index는 i에, 데이터는 data
  print(i,":",data)

aStr = "안녕하세요"
for i in aStr: # 문자열의 값을 1개씩 가져와서 출력
  print(i)

for idx,data in enumerate(aStr):
  print(idx,":",data)


  



# #번호,이름,국어,영어,수학
# s = [4,'강감찬',100,90,99]
# # s 리스트에 합계, 평균 추가
# print(s[2])
# s.append(s[2]+s[3]+s[4])
# print(s)
# s.append((s[2]+s[3]+s[4])/3)
# print(s)
# print("{},{},{},{},{},{},{:.2f}".format(s[0],s[1],s[2],s[3],s[4],s[2]+s[3]+s[4],(s[2]+s[3]+s[4])/3))


# list 추가 - append - 제일 뒤에 추가, insert - 원하는 위치 추가
# list 삭제 - del - 위치 삭제, remove - 값으로 검색해서 삭제
# a_list = [1,2,3]
# # 마지막에 10추가
# a_list.append(10)
# print(a_list)

# # index 2번에 100 추가
# a_list.insert(2,100)
# print(a_list)

# # index 1번 삭제
# del a_list[1]
# print(a_list)

# # 100이라는 값을 삭제
# a_list.remove(100)
# print(a_list)




## 문자열 슬라이싱
# str = "좋은 하루되세요. 많은 행복받으세요. 많은 감사! 많은 돈."
# print(len(str))

# 뒤에서 5자리 전 까지 출력
# print(str[-5:])
# print(str[-1])
# print(str[::-1])