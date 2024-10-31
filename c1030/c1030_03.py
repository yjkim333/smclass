import oracledb
import random
# email 발송 관련 import
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


def connets():
	user = 'ora_user'
	password = '1111'
	dsn = 'localhost:1521/xe'
	try:
		conn = oracledb.connect(user=user,password=password,dsn=dsn)
	except Exception as e: print("예외발생 :",e) 
	return conn


while True:
	print()
	print("[ 커뮤니티 ]")
	print("1. 로그인")
	print("2. 비밀번호 찾기")
	print("3. 회원가입")
	print("0. 프로그램 종료")
	print("ㅡ"*15)
	choice = input("원하는 번호 입력 >> ")

	if choice == '1':
		print("[ 로그인 ]")
		user_id = input("아이디를 입력하세요. >> ")
		user_pw = input("비밀번호를 입력하세요. >> ")

		# 오라클 db에 접속해서 member 테이블에서 검색해서 가져옴.

		# db접속
		conn = connets()
		cursor = conn.cursor()
		sql = "select * from member where id=:id and pw=:pw"
		cursor.execute(sql,id=user_id,pw=user_pw)

		# rows = cursor.fetchall()
		row = cursor.fetchone()
		print(row)
		if row != None:
			print("[로그인 성공]")
			print(f"{row[2]} 님, 환영합니다.")
		else:
			print("아이디 또는 패스워드가 잘못되었습니다. 정확히 입력해 주세요.")

		cursor.close()


		# ### 프로그램 구현 ###

	elif choice == '2':
		print("[ 비밀번호 찾기 ]")
		search = input("아이디를 입력하세요. >> ")
		# 아이디가 있는지 확인
		conn = connets()
		cursor = conn.cursor()
		sql = "select * from member where id=:id"
		cursor.execute(sql,id=search)
		row = cursor.fetchone()
		print(row)
		if row != None:
			print("아이디가 존재합니다. 임시 비밀번호를 발급합니다.")
			
			### 
			# 1. 임시 비밀번호 생성
			r_pw = random.randrange(0,100000000)  # 86560154
			# 2. 이메일로 발송
			
			smtpName = "smtp.naver.com"
			smtpPort = 587

			sendEmail = "dydwns4671@naver.com"
			pw = "4DN9XWEN6ZBL"
			recvEmail = row[3]

			title = "임시 비밀번호 발송"
			content = f"임시비밀번호는 {r_pw} 입니다."

			msg = MIMEText(content)
			msg['Subject'] = title
			msg['From'] = sendEmail
			msg['To'] = recvEmail

			# 서버이름,서버포트
			s = smtplib.SMTP(smtpName,smtpPort)
			s.starttls()
			s.login(sendEmail,pw)
			s.sendmail(sendEmail,recvEmail,msg.as_string())
			s.quit

			# 메일발송완료
			print("등록된 메일로 임시비밀번호를 발송했습니다.")

			# 3. 아이디의 비밀번호를 임시비밀번호로 수정합니다.
			sql = "update member set pw=:pw where id=:id"
			cursor.execute(sql,id=search,pw=r_pw)
			conn.commit()
			print("수정")
			# 3. 임시번호로 로그인 했을 경우 로그인 성공이 나타나도록 하시오.
		else:
			print("등록된 아이디가 없습니다.")
		
		cursor.close()


	elif choice == '3':
		pass

	elif choice == '0':
		print("---프로그램 종료---")
		break