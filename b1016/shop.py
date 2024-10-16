import datetime
member = []
m_keys = ["id","pw","name","nickName","address","money"]
c_keys = ['cno','id','name','pCode','pName','price','date']





product = [
	{"pno":1,"pCode":"t001","pName":"삼성TV","price":2000000,"color":"black"},
	{"pno":2,"pCode":"g001","pName":"LG냉장고","price":3000000,"color":"white"},
	{"pno":3,"pCode":"h001","pName":"하만카돈스피커","price":500000,"color":"gray"},
	{"pno":4,"pCode":"w001","pName":"세탁기","price":1000000,"color":"yellow"},
]

cartNo = 0
cart = []
session_info = {}
p_title = ['번호','아이디','이름','상품코드','상품명','가격','구매일자']

# member.txt 파일읽기 -> member 딕셔너리 저장
f = open('member.txt','r',encoding='utf-8')
while True:
	line = f.readline()
	if not line :break
	m = line.strip().split(",")
	m[5] = int(m[5])
	member.append(dict(zip(m_keys,m)))
f.close()
# print(member)
#------
# cart.txt 파일읽기 -> cart 딕셔너리 저장
f = open('cart.txt','r',encoding='utf-8')
while True:
	line = f.readline()
	if not line : break
	c = line.strip().split(",")
	c[0] = int(c[0])
	c[5] = int(c[5])
	cart.append(dict(zip(c_keys,c)))
f.close()

##### 함수선언 #####
# 상품구매함수 선언
def buy(choice,cartNo):
	print(f"{product[choice-1]['pName']}를 구매하셨습니다.")
	print("구매내역에 등록되었습니다.")
	print()
	# 로그인정보 - session_info
	now = datetime.datetime.now()
	today = now.strftime("%Y-%m-%d %H:%M:%S")
	c = {"cno":cartNo+1,"id":session_info['id'],"name":session_info['name'],"pCode":product[choice-1]['pCode'],"pName":product[choice-1]['pName'],"price":product[choice-1]['price'],"date":today}
	session_info['money'] -= product[choice-1]['price']
	cart.append(c)
	cartNo += 1
	return cartNo
#-----
# 구매내역출력함수 선언
def buy_output():
	print("[  구매 내역  ]")
	print(f"{p_title[0]}\t{p_title[1]}\t{p_title[2]}\t{p_title[3]}\t{p_title[4]:15s}\t{p_title[5]}\t{p_title[6]}")
	print("ㅡ"*45)
	sum = 0
	for i in cart:
		sum += i['price']
		print(f"{i['cno']}\t{i['id']}\t{i['name']}\t{i['pCode']}\t{i['pName']:15s}\t{i['price']}\t{i['date']}")
	print()
	print(f"총 구매 건수 : {len(cart)} 건")
	print(f"총 구매 금액 : {sum:,} 원")
#-----
# 금액충전함수 선언
def buy_money():
	print("[  금액 충전  ]")
	print(f"현재 보유금액 : {session_info['money']:,} 원")
	session_info['money'] += int(input("충전할 금액 입력 >> "))
	print(f"보유금액이 {session_info['money']:,} 원으로 변경되었습니다.")
#-----
# 내용저장함수 호출
def buy_save():
	# member.txt 파일 생성해서 csv형태로 문자열로 저장하시오
	f = open('member.txt','w',encoding='utf-8')
	for m in member:
		f.write(f"{m['id']},{m['pw']},{m['name']},{m['nickName']},{m['address']},{m['money']}\n")
	f.close()

	# member.txt 파일 생성해서 csv형태로 문자열로 저장하시오
	f = open('cart.txt','a',encoding='utf-8')
	for i in cart:
		f.write(f"{i['cno']},{i['id']},{i['name']},{i['pCode']},{i['pName']},{i['price']},{i['date']}\n")
	f.close
	print("내용저장이 완료되었습니다.")

#-----

##### Start #####
while True:
	print("[ 로그인 화면 ]")
	input_id = input("아이디를 입력하세요.>> ")
	input_pw = input("패스워드를 입력하세요.>> ")
	flag = 0
	for m in member:
		if input_id == m['id'] and input_pw == m['pw']:
			session_info = m
			flag = 1
			break
	if flag == 0:
		print("아이디 또는 패스워드가 일치하지 않습니다.")
	elif flag == 1:
		print("SM Shop에 오신것을 환영합니다.")
		break

while True:
	print()
	print("          [  SM-Shop  ]")
	print(f"                         {session_info['nickName']}님 환영합니다.")
	print(f"                         보유금액 : {session_info['money']:,} 원")
	print()
	print("1. 삼성TV - 2,000,000원")
	print("2. LG냉장고 - 3,000,000원")
	print("3. 하만카돈스피커 - 500,000원")
	print("4. 세탁기 - 1,000,000원")
	print("7. 내용 저장")
	print("8. 구매 내역")
	print("9. 금액 충전")
	choice = int(input("구매하려는 상품번호 입력 >> "))

	if choice == 1:
		cartNo = buy(choice,cartNo)					# 상품구매함수 호출
	elif choice == 2:
		cartNo = buy(choice,cartNo)					# 상품구매함수 호출
	elif choice == 3:
		cartNo = buy(choice,cartNo)					# 상품구매함수 호출
	elif choice == 4:
		cartNo = buy(choice,cartNo)					# 상품구매함수 호출
	elif choice == 7:
		buy_save()													# 내용저장함수 호출
	elif choice == 8:
		buy_output()												# 구매내역출력함수 호출
	elif choice == 9:
		buy_money()													# 금액충전함수 선언
