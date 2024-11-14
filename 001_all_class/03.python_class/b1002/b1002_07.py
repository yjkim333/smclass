students = [
  [1,'홍길동',100,90,99],
  [2,'유관순',100,100,99],
  [3,'이순신',100,100,99],
  [4,'강감찬',100,90,99],
  [5,'김구',90,90,99]
]
# 이름을 입력받아 같은 이름이 있으면 데이터 삭제, 없으면 없습니다 출력
name = input("이름을 입력하세요.")
count = 0
for idx,s in enumerate(students):
  if s[1] == name:
    del students[idx]
    print(name,"을(를)삭제합니다.")
    print(f"{name}을(를)삭제합니다.")
    count = 1
    break
if count == 0:
  print("없습니다")
else:
  print("학생 성적 : ",students)



# for s in students:
#   if s[1] == name:
#     students.remove(s)
#     break
# if s[1] == name:
#   print(students)
# else:
#   print("없습니다.")




# all_list = [[1,'홍길동',100],[1,'유관순',200],[3,'이순신',100]]

# a = [3,'이순신',100]

# # 데이터 값으로 삭제
# # all_list.remove(a)
# # print(all_list)

# # 이름이 유관순 인것을 삭제
# for s in all_list:
#   if s[1] == '유관순':
#     all_list.remove(s)
#     print(all_list)


# a = [1,'홍길동',100]
# b = [1,'홍길동',200]
# c = [1,'홍길동',100]

# if a==b:
#   print("같음")
# else:
#   print("다름")

# if a==c:
#   print("같음")
# else:
#   print("다름")

# aArr = [2,3,4,5,6,7,8,9,10]

# # 50,100 추가
# aArr.append(50)
# aArr.append(100)
# print(aArr)

# # 2번 자리에 30 추가
# aArr.insert(2,30)
# print(aArr)

# # 숫자 6을 삭제
# aArr.remove(6)
# print(aArr)

# # index 0,3 데이터를 삭제
# del aArr[0], aArr[3]
# print(aArr)