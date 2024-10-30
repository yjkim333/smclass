import random

# ### 임시비밀번호 생성 ###
# a_list = [0,1,2,3,4,5,6,7,8,9]
# # 랜덤 8자리 숫자
# a = random.randrange(0,100000000)  # 0~9999
# ran_num = f"{a:08}"
# print(ran_num)


import oracledb


def connets():
	user = 'ora_user'
	password = '1111'
	dsn = 'localhost:1521/xe'
	try:
		conn = oracledb.connect(user=user,password=password,dsn=dsn)
	except Exception as e: print("예외발생 :",e) 
	return conn


#### 데이터 수정 ####
# db접속
conn = connets()
cursor = conn.cursor()
# 입력
user_id = input("아이디를 입력하세요. >> ")    # eee
user_pw = input("비밀번호를 입력하세요. >> ")  # 2222

sql = "update member set pw=:pw where id=:id"
cursor.execute(sql,id=user_id,pw=user_pw)
conn.commit()

print("파일이 수정되었습니다.")

cursor.close()
