students = [
  [1,'홍길동',100,90,99],
  [2,'유관순',100,100,99],
  [3,'이순신',100,100,99]
]

ss = [4,'강감찬',100,90,99]
students.append(ss)

# 값이 2개 이상 저장하려면 , 주소값
# 이순신인 데이터를 삭제.
# remove 삭제
# for s in students:
#   if s[1] == '이순신':
#     students.remove(s)
# print(students)

# del 삭제
for idx,s in enumerate(students):
  print(idx,":",s)
  if s[1] == '이순신':
    del students[idx]

# # print(students)     # 한번에 모두 출력

# for s in students:  # 1개씩 가져와서 출력
#   print(s)

# # 이름이 유관순 인것을 출력
# for s in students:  # 1개씩 가져와서 출력
#   if s[1] == "유관순":
#     print(s)
