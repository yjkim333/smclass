students = [
  {'no':1,'name':"홍길동",'kor':100,'eng':100,'math':99,'total':299,'avg':99.67,'rank':0},
  {'no':2,'name':"유관순",'kor':80,'eng':80,'math':85,'total':245,'avg':81.67,'rank':0},
  {'no':3,'name':"이순신",'kor':90,'eng':90,'math':91,'total':271,'avg':90.33,'rank':0},
  {'no':4,'name':"강감찬",'kor':60,'eng':65,'math':67,'total':192,'avg':64.00,'rank':0},
  {'no':5,'name':"김구",'kor':100,'eng':100,'math':84,'total':284,'avg':94.67,'rank':0}
]

# students 의 타입은 list 타입
print(students)
print("ㅡ"*28)
# sort() - > 리스트내의 함수
# lambda x:x[1]
# students.sort(key=lambda x:x['name'],reverse=True)
students.sort(key=lambda x:x['total'],reverse=True)
# 딕셔너리에서는 lambda x:x[key]
print(students)


# ##리스트 정렬##
# aArr = [4,5,6,1,2]
# print(aArr)
# aArr.sort() # 순차정렬
# print(aArr)
# aArr.sort(reverse=True) # 역순정렬
# print(aArr)
# aArr.reverse() # 리스트를 거꾸로(반대로) 출력 - 정렬은 아님
# print(aArr)

# students = [
#   [1,"홍길동",100,100,99,299,99.67,0],
#   [2,"유관순",80,80,85,245,81.67,0],
#   [3,"이순신",90,90,91,271,90.33,0],
#   [4,"강감찬",60,65,67,192,64.00,0],
#   [5,"김구",100,100,84,284,94.67,0]
# ]

# print(students)

# 리스트 정렬

# 함수 사용 정렬
# def stu_sort(x):
	# return x[1]
# students.sort(key=stu_sort) # 함수를 사용해서 정렬 => 약식으로 쓰면 아래처럼 lambda  

# #sort() -> list에서만 지원되는 정렬함수 = 리스트에서만 쓸 수 있음 , 자체로 list 내용 변경
# students.sort(key=lambda x:x[5]) # x[5](합계)으로 순차정렬
# students.sort(key=lambda x:-x[5]) # x[5](합계)으로 역순정렬 - 숫자는 앞에 - 만 붙임
# students.sort(key=lambda x:x[1]) # x[1](이름)으로 순차정렬
# students.sort(key=lambda x:x[1],reverse=True) # 역순정렬
# x = sorted(students,key=lambda x:x[1]) # sorted()함수 사용해서 정렬 -> 자체로 변경 못함 = 변수로 받아야됨
# print(x)
# print(students)

