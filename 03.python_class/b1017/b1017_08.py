import datetime
import os
members = []
m_title = ['id','pw','name','nickName','address','money']

#### member.csv파일 불러오기
f = open('C:/workspace/smclass/b1017/member.csv',"r",encoding="utf-8")
while True:
	line = f.readline()
	if not line: break
	# c리스트 저장
	c = line.strip().split(",")
	c[5] = int(c[5])  # money
	# members리스트에 딕셔너리 저장
	members.append(dict(zip(m_title,c)))
f.close()
#-----------------------------
# cart.txt파일 읽기, member딕셔너리 저장
cartNo = 0
cart = []
c_keys = ["cno","id","name","pCode","pName","price","date"]
# isfile : 파일인지확인, isdir : 디렉토리인지 확인, exists : 파일이 존재하는지 확인
if os.path.exists("b1017/cart.txt"):
	f = open('b1017/cart.txt','r',encoding='utf-8')
	while True:
		line = f.readline()
		if not line: break
		c = line.strip().split(",")
		c[0] = int(c[0])
		c[5] = int(c[5])
		cart.append(dict(zip(c_keys,c)))
	f.close()
#-----------------------------------------

# 파일 저장해서 불러오기
product = [
	{"pno":1,"pCode":"t001","pName":"삼성TV","price":2000000,"color":"black"},
	{"pno":2,"pCode":"g001","pName":"LG냉장고","price":3000000,"color":"white"},
	{"pno":3,"pCode":"h001","pName":"하만카돈스피커","price":500000,"color":"gray"},
	{"pno":4,"pCode":"w001","pName":"세탁기","price":1000000,"color":"yellow"},
]

f = open("products.txt","w",encoding="utf-8")
# f.write(product)
f.close()




session_info = {}
p_title = ["번호","아이디","이름","코드","상품명","가격","구매일자"]


#####  프로그램 시작  #####
while True:
	print("[ 메인화면 ]")
	print("1. 로그인")
	print("2. 회원가입")
	print("0. 프로그램 종료")
	print("-"*30)
	choice = input("원하는 번호를 입력하세요.>> ")
	if choice == "1":
		# 프로그램 구현
		while True:
			print("[  로그인  ]")
			flag = 0
			input_id = input("아이디를 입력하세요.>> ")
			input_pw = input("패스워드를 입력하세요.>> ")
			for m in members:
				if input_id == m['id'] and input_pw == m['pw']:
					flag = 1
					session_info = m
					break
			if flag == 0:
				print("아이디 또는 비밀번호가 틀립니다. 다시 입력하세요.")
			else:
				break
		break

	elif choice == "2":
		print("[  회원가입  ]")
		while True:
			while True:
				flag = 0
				r_input_id = input("아이디를 입력하세요.>> ")
				for m in members:
					if r_input_id == m['id']:
						flag = 1
						break
				if flag == 1:
					print("이미 등록된 아이디 입니다. 다시 입력해 주세요.")
					continue
				else:
					print(f"{r_input_id} 는 사용 가능한 아이디 입니다.")
					break
			
			r_input_pw = input("비밀번호를 입력하세요.>> ")
			r_input_name = input("이름을 입력하세요.")
			r_input_nickname = input("닉네임을 입력하세요.")
			r_input_address = input("주소를 입력하세요.")
			r_input_money = int(input("충전금액을 입력하세요."))

			r_m = [r_input_id,r_input_pw,r_input_name,r_input_nickname,r_input_address,r_input_money]

			members.append(dict(zip(m_title,r_m)))
			print(f"반갑습니다, {r_input_nickname}님")
			print("회원가입이 완료되었습니다.")
			break
		
	elif choice == "0":
		print("프로그램을 종료합니다.")
		break
	

# 프로그램을 구현하시오.
while True:
	print()
	print("          [  SM-Shop  ]")
	print(f"                         {session_info['nickName']} 님, 반갑습니다.")
	print(f"                         보유금액 : {session_info['money']:,} 원")
	print()
	print("1. 삼성TV - 2,000,000")
	print("2. LG냉장고 - 3,000,000")
	print("3. 하만카돈스피커 - 500,000")
	print("4. 세탁기 - 1,000,000")
	print("7. 내용저장")
	print("8. 구매내역 ")
	print("9. 금액충전 ")
	choice = int(input("구매하려는 상품번호를 입력하세요.>> "))
	# 프로그램 구현