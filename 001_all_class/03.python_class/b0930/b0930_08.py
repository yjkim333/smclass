## list 추가 방법 : append - 제일 뒤에 추가, insert - 원하는 위치에 추가
a_list = [1,2,3]
print(a_list)
a_list.append(4)
print(a_list)
a_list.append(10)
print(a_list)
a_list.insert(0,50) #(위치,추가하는 값)
print(a_list)
a_list.insert(3,20) #(위치,추가하는 값)
print(a_list)

## list 삭제 방법 : del - index 위치의 데이터 삭제, remove - 데이터 값으로 삭제
del a_list[0] # 0번째 데이터 삭제
print(a_list)

del a_list[2] # 2번째 데이터 삭제
print(a_list)

a_list.remove(4)
print(a_list) # 4라는 데이터 삭제

a_list.remove(1)
print(a_list) # 1이라는 데이터 삭제


stu = [1,'홍길동',100,100,100,99]
# 합계, 평균 추가해서 출력
stu.append(stu[2]+stu[3]+stu[4]+stu[5])
stu.append((stu[2]+stu[3]+stu[4]+stu[5])/4)
print(stu)