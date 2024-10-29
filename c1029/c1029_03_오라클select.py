## 학생 성적 출력을 하시오 ##
import oracledb

conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')

cursor = conn.cursor()


# num = input("숫자를 입력하세요. >> ")

# execute 함수에 변수를 추가
# sql = "select * from students where no >=:no"
# cursor.execute(sql,no=num)

### no = 10,20,30 을 검색해서 출력

# execute 함수 : 리스트 값 전달
# execute 뒤에는 dict,list,tuple 만 가능
num = input("숫자를 입력하세요. >>(10,20,30) ")
n_list = num.split(",")
sql = "select * from students where no in(:1,:2,:3)"
cursor.execute(sql,n_list)

# execute 함수 : 리스트 값 전달
num1 = input("숫자를 입력하세요. >> ")
num2 = input("숫자를 입력하세요. >> ")
num3 = input("숫자를 입력하세요. >> ")
n_list = [num1,num2,num3]
sql = "select * from students where no in(:1,:2,:3)"
cursor.execute(sql,n_list)





num1 = input("숫자를 입력하세요. >> ")
num2 = input("숫자를 입력하세요. >> ")
num3 = input("숫자를 입력하세요. >> ")
sql = "select * from students where no in(:no1,:no2,:no3)"
cursor.execute(sql,no1=num1,no2=num2,no3=num3)

# for i in range(3):
# 	sql = f"select * from students where no in ({input("숫자를 입력하세요. >> ")})"
# 	cursor.execute(sql)


# 문자열함수 f 사용
# sql = f"select * from students where no >= {no}"
# cursor.execute(sql)


rows = cursor.fetchall()

title = ['번호','이름','국어','영어','수학','합계','평균','등수','등록일']
for i,t in enumerate(title):
	if i == 1:
			print(f"{t:10}",end='\t')
			continue
	print(t,end='\t')
print()
print("ㅡ"*50)

for row in rows:
	for i,r in enumerate(row):
		if i == 1:
			print(f"{r:10}",end='\t')
			continue
		if i == 6:
			print(f"{r:.2f}",end='\t')
			continue
		if i == 8:
			print(r.strftime("%Y/%m/%d"))
			continue
		print(r,end='\t')
print()

conn.close()