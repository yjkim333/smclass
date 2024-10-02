students = [
  [1,'홍길동',100,90,99],
  [2,'유관순',100,100,99],
  [3,'이순신',100,100,99],
  [4,'강감찬',100,90,99],
  [5,'김구',90,90,99]
]

# 합계, 평균 추가
for s in students:
  s.append(s[2]+s[3]+s[4])
  s.append((s[2]+s[3]+s[4])/3)
print(students)

cnt = 0
search = input("학생이름 검색")
for s in students:
  # 찾는 학생이 있으면 찾는 학생 이름이 있습니다. 없습니다.
  # 찾으면 cnt = 1
  if s[1] == search:
    print(search," 학생이 있습니다.")
    cnt = 1
    break

if cnt == 0:
  print("찾고자 하는 학생이 없습니다.")
