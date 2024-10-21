members = []
m_keys = ["id","pw","name","nickName","address","money"]

# 파일 불러오기
f = open('C:/workspace/smclass/b1017/member.csv','r',encoding='utf-8')
while True:
	line = f.readline()
	if not line: break
	m = line.strip().split(",")
	m[5] = int(m[5])
	members.append(dict(zip(m_keys,m)))
# print(members)
f.close()

while True:
	print("1.회원등록")
	print("2.회원검색")
	choice = int(input("원하는 번호를 입력해주세요 >> "))
	# 회원 등록
	if choice == 1:
		id = input("아이디를 입력하세요.>> ")
		flag = 0
		for m in members:
			if id in m['id']:
				print("이미 동일 아이디가 있습니다.")
				flag = 1
				break
		if flag == 1:
			continue
		else: print(f"{id}(은)는 사용가능한 아이디입니다.")
		pw = input("패스워드 입력 >>")
		name = input("이름 입력 >> ")
		nickName = input("닉네임 입력 >> ")
		money = int(input("충전 금액 입력 >> "))
		m_list = [id,pw,name,nickName,money]
		members.append(dict(zip(m_keys,m_list)))
		print(f"{name} 님 회원가입이 완료되었습니다.")
		print(m_list)
		print()
		print(members)

	# id 검색 - 입력한 문자(a)가 들어있는 아이디 모두 출력
	elif choice == 2:
		search = input("검색할 ID 입력 >> ")
		flag = 0
		mm = []
		print(f"[ {search} 검색 결과 ]")
		for i,m in enumerate(members):
			if m['id'].find(search) != -1:
				flag = 1
				mm.append(m)
				# print(f"{i+1}번 {m['id']}")
				
		if flag == 0:
			print("검색결과 없음")
		elif flag == 1:
			print(f"{mm}")
			print(f"총 인원 : {len(mm)}")

		# print(sArr)