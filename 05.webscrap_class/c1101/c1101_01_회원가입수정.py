import oracledb
import datetime


## db 연결 함수 선언 ##
def connects():
	user = 'ora_user'
	password = '1111'
	dsn = 'localhost:1521/xe'
	try: conn = oracledb.connect(user=user,password=password,dsn=dsn)
	except Exception as e: print("예외발생 :",e)
	return conn


## 회원수 확인
def member_count():
	## 오라클 db - mem table count 가져와
	conn = connects()
	cursor = conn.cursor()
	# employees 부서번호 10번인 사원수를 가져오시오
	# sql = "select count(*) no, a.department_id dept, department_name deptname from employees a,departments b where a.department_id = b.department_id and a.department_id = 50 group by a.department_id,department_name"
	sql = "select count(*) from mem"
	cursor.execute(sql)
	row = cursor.fetchone()
	conn.close()
	return row
	


### 회원수 확인 값을 리턴하시오.
all_member = member_count()
# all_member = 100

nowYear = datetime.datetime.now().year

print()
print("   [  커뮤니티  ]   ")
# print("현재 회원 수 :",all_member[0],", 부서번호 :",all_member[1],", 부서명 :",all_member[2])
print("현재 회원 수 :",all_member[0])

print()
print("1. 로그인")
print("2. 회원가입")
print("3. 회원정보수정")
print()
choice = input("원하는 번호 입력 >> ")

if choice == 1:
	pass

elif choice == '2':
	print("  [  회원가입  ]  ")
	id = input("아이디를 입력하세요. >>")
	pw = input("비밀번호를 입력하세요. >>")
	name = input("이름을 입력하세요. >>")
	birth = input("생년월일을 입력하세요. (예. 20020312) >>")
	age = nowYear-int(birth[:4])  # 나이 자동 계산 입력
	gender = input("성별을 입력하세요.(Male/Female) >>")
	hobby = input("취미를 입력하세요. >>")

	my_list = [id,pw,name,age,birth,gender,hobby]

	# # db접속
	conn = connects()
	cursor = conn.cursor()
	sql = "insert into mem (id,pw,name,age,birth,gender,hobby) values(:1, :2, :3, :4, :5, :6, :7)"
	# sql = "insert into mem (id,pw,name,age,birth,gender,hobby) values(:id, :pw, :name, :birth, :age, :gender, :hobby)"
	cursor.execute(sql,my_list)
	# cursor.execute(sql,id=id,pw=pw,name=name,age=age,birth=birth,gender=gender,hobby=hobby)
	conn.commit()
	conn.close()
	print("저장되었습니다.")

elif choice == '3':
	print("  [  회원정보수정  ]  ")
	# # db접속
	conn = connects()
	cursor = conn.cursor()
	id = 'aaa'
	sql = "select * from mem where id = :id"
	cursor.execute(sql,id=id)
	row = cursor.fetchone()
	print("아이디 :",row[0],"  현재 취미 :",row[6])
	hobby = input("변경할 취미를 입력하세요. >>")

	sql = "update mem set hobby = :hobby where id = :id"
	cursor.execute(sql,hobby=hobby,id=id)
	conn.commit()
	conn.close()
	print("수정되었습니다.")	


# # db접속
# conn = connects()
# cursor = conn.cursor()
# sql = "select * from member where id=:id and pw=:pw"
# cursor.execute(sql,id=user_id,pw=user_pw)
# row = cursor.fetchone()
# cursor.close()
