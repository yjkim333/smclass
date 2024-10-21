students = [
  [1,'홍길동',100,90,99],
  [2,'유관순',100,100,99],
  [3,'이순신',100,100,99],
  [4,'강감찬',100,90,99],
  [5,'김구',90,90,99]
]

# 합계, 평균을 추가해서 전체를 출력하시오
for s in students:
	total = s[2]+s[3]+s[4]
	avg = total/3
	s.append(total)
	s.append(avg)
# print(students)
print("학번\t이름\t국어\t영어\t수학\t총점\t평균")
print("ㅡ"*28)
for s in students:
  print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(s[0],s[1],s[2],s[3],s[4],s[5],s[6]))