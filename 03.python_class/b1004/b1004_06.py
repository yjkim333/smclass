a_list = ["홍길동","유관순","이순신"]
# 이름 뒤에 님 붙여
a_list = [a+"님" for a in a_list]
print(a_list)




# a_list = [1,2,3,4,5]
# a_list = [1*1,2*2,3*3,4*4,5*5]
# print(a_list)

# 리스트의 값을 변경해서 리스트에 저장 1)
# for i,a in enumerate(a_list):
# 	a_list[i] = a**2

# 리스트의 값을 변경해서 리스트에 저장 2) 리스트 내포(한줄for문)
# a_list = [a**2 for a in a_list] # 리스트
# print(a_list)

# 리스트 값 변경 - index 번호에 값을 수정
# print(a_list)
# a_list[1] = 100
# print(a_list)

# 리스트 슬라이싱 0부터 4이전(3)까지 출력
print(a_list[0:4])

# 리스트 범위보다 넘어서 출력하려면, 에러가 나지 않고 출력은 됨
# 범위까지만 출력.
print(a_list[0:10])

# 없는 곳에 입력하면 에러
# a_list[10] = 122

# 없는 곳 출력하면 에러
# 


#  enumerate()함수
# a_list = ['홍길동','유관순','이순신','강감찬','김구','김유신','홍길자']
# # for문 출력
# for a in a_list:
# 	print(a)

# # enumerate()함수 - index 번호를 출력
# for i,a in enumerate(a_list):
# 	print(i+1,":",a)

# print(a_list)