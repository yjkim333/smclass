# sm shop

# member.txt 불러와서 딕셔너리장 저
member = []
m_keys = ['id','pw','name','nickName','address','money']
f = open('member.txt','r',encoding='utf-8')
while True:
	line = f.readline()
	if not line : break
	m = line.strip().split(",")
	m[5] = int(m[5])
	member.append(dict(zip(m_keys,m)))
#-----

# cart.txt 불러와서 딕셔너리장 저
cart = []
c_keys = ['cno','id','name','pCode','pName','price','date']
f = open('cart.txt','r',encoding='utf-8')
while True:
	line = f.readline()
	if not line : break
	c = line.strip().split(",")
	c[0] = int(c[0])
	c[5] = int(c[5])
	cart.append(dict(zip(c_keys,c)))
#-----

product = [
	{"pno":1,"pCode":"t001","pName":"삼성TV","price":2000000,"color":"black"},
	{"pno":2,"pCode":"g001","pName":"LG냉장고","price":3000000,"color":"white"},
	{"pno":3,"pCode":"h001","pName":"하만카돈스피커","price":500000,"color":"gray"},
	{"pno":4,"pCode":"w001","pName":"세탁기","price":1000000,"color":"yellow"},
]

session_info = []
while True:
	print("[로그인]")
	input_id = input("ID 입력 >> ")
	input_pw = input("PW 입력 >> ")
	flag = 0
	for m in member:
		if input_id == m['id'] and input_pw == m['pw']:
			session_info.append(m)
			flag = 1
			break
	if flag == 0:
		print("아이디 또는 패스워드가 틀립니다.")
	elif flag == 1:
		print(f"{m['name']} 님, 반갑습니다.")
		break

print("[  SM Shop  ]")
print("1. 삼성 TV - 가격 : 2,000,000원")
print("2. LG 냉장고 - 가격 : 3,000,000원")
print("3. 하만카돈 스피커 - 가격 : 400,000원")
print("4. 드럼세탁기 - 가격 : 1,100,000원")
print("7. 내용 저장")
print("8. 구매 내역")
print("9. 금액 충전")
choice = int(input("구매하실 상품의 번호 입력 >> "))

if choice == 1:
	print("삼성 TV를 구매하셨습니다.")
	print("구매내역에서 확인하실 수 있습니다.")
	for p in product:
		pp = [p['pcode'],p['pName'],p]


{"pno":1,"pCode":"t001","pName":"삼성TV","price":2000000,"color":"black"},
c_keys = ['cno','id','name','pCode','pName','price','date']