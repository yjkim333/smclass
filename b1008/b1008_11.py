# html_class - join02_info_input.html notice_read.html  (a_html - notice_list.html에서 헤더와 이미지 그대로 사용)
# 1004_학생성적프로그램 리스트->딕셔너리
# 1002_14 숫자 맞추기 게임 구현 - + 리스트에 자신이 입력한 숫자를 저장해서 출력(정답은 뭐 니가 입력했던 건 뭐뭐뭐)


ss = "파이썬 수업중 타입 문자열 타입,정수형 타입,실수형 타입,논리형 타입이 있습니다"
i_str = input("글자를 입력하세요.")

a_str = '파이썬'
a = a_str.join("-")
print(a)

# 공백제거
sss = ss.replace(" ","")
print(sss)

# 검색 글자 개수 - count - 없으면 0
# idx = ss.count(i_str)
# print("개수 : ",idx)


# idx = ss.find(i_str)+1
# print(ss.find(i_str,idx))
# '타입'의 위치 값을 모두 출력하시오
# idx = 0
# a_list = []
# for i in range(ss.count(i_str)):
# 	num = ss.find(i_str,idx)  #0번부터 시작 ->8,15
# 	a_list.append(num)
# 	# print(num)
# 	idx = num + 1
# print(f"검색 갯수 : {len(a_list)}, 위치값 : {a_list}")

# 위치값
# find - 없을 때 -1 리턴
# idx = ss.find(i_str)
# print("위치값 : ",idx)

# index - 없을 때 에러
# idx = ss.index(i_str)
# print("위치값 : ",idx)

# if i_str in ss:
# 	print("있다.")
# else:
# 	print("없다.")



# # 1~20 중에 3의 배수만 리스트에 추가하시오
# a_list = []
# # for문
# for i in range(1,21):
# 	if i%3 == 0:
# 		a_list.append(i)
# print(a_list)

# # 리스트내포
# # [값 for문 조건식]
# b_lsit = [i for i in range(1,21) if i%3 == 0]
# print(b_lsit)



# aArr = [1,2,3,4,5]
# a_list = [1,4,9,16,25]
# # 컴프리헨션(리스트내포) 사용
# a_list = [i*i for i in aArr]
# print(a_list)