# for
# 0부터 1씩 증가하면서 10번 실행
for i in range(10):
	print(i)
print("ㅡ"*10)

# 5부터 10이전(9)까지 5번 실행
for j in range(5,10):
	print(j)
print("ㅡ"*10)

# range(시작값,끝값+1,증가값)
for i in range(1,9+1,2): 
	print(f"[ {i}단 ]")
	for j in range(1,9+1):
		print(f"{i}x{j} = {i*j}")
	print("*"*10)
 

a_list = [1,2,3,4,5]
for k in a_list:
	print(k)
print("ㅡ"*10)



# ### 파이썬 리스트타입 - 문자열-str, 정수형-int, 실수형-float, 논리형-bool

# 리스트타입
b_list = [3,5,9,10,20,3,3,10,5,20]
for m in b_list:
	print(m)
print("ㅡ"*10)


# ### 딕셔너리타입 - {} : json 타입과 모양이 같음. -> 키:값 (key:value)
dic = {
	"번호":1,
	"이름":"홍길동",
	"국어점수":100,
	"영어점수":100,
	"수학점수":90
}
print(dic["번호"]) #키 값을 넣으면 해당되는 값이 프린트
print(dic["이름"])
print("ㅡ"*20)

for n in dic: # dic에서 key의 값을 n에 넣어줌
	# print(n) # key를 출력
	print(dic[n]) # key의 value가 출력됨


print("ㅡ"*20)
# 리스트 길이 - len()
print(len(b_list))
print("ㅡ"*10)

# 리스트 안에 해당되는 숫자가 몇개 인지 확인 - count()
print(b_list.count(3))
print(b_list.count(5))

# 리스트 추가 - append(), insert(), extend([2,3]):리스트 뒤에 2,3 추가)
# 리스트 삭제 - del, remove(), clear:모두 삭제