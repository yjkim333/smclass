# students 리스트 타입
students = [
  {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
  {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
  {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
  {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
  {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
]
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수'] #전역변수
choice = 0 # 전역변수
chk = 0    # 체크변수
count = 1  # 성적처리
stuNo = len(students)  # 리스트에 학생이 있으면, 그 인원으로 변경
no=0;name="";kor=0;eng=0;math=0;total=0;avg=0;rank=0 #성적처리변수

# 학생성적프로그램
while True:
	print("[ 학생성적프로그램 ]")
	print("="*50)
	print("1. 학생성적입력")
	print("2. 학생성적출력")
	print("3. 학생성적수정")
	print("4. 학생성적검색")
	print("5. 학생성적삭제")
	print("6. 등수처리")
	print("7. 학생성적정렬")
	print("0. 프로그램 종료")
	print("="*50)
	choice = input("원하는 번호를 입력하세요.(0.종료)>> ")
	if choice == '1':
		print("[ 학생 성적 입력 ]")
		print()
		while True:
			#학생 성적 직접 입력
			no = stuNo + 1  # 리스트 학생 수
			name = input(f"{no}번째 학생 이름 입력(메뉴로이동 -> 0)>>")
			if name == "0":
				print("성적입력을 취소합니다.")
				print()
				break
			kor = int(input("국어 성적 입력"))
			eng = int(input("영어 성적 입력"))
			math = int(input("수학 성적 입력"))
			total = kor + eng + math
			avg = total/3
			ss = {'no':no,'name':name,'kor':kor,'eng':eng,'math':math,'total':total,'avg':avg,'rank':rank}
			students.append(ss)
			stuNo += 1 #학생수(번호) 1증가
			print(f"{name} 학생의 성적 저장되었습니다.")
			print()

	
	elif choice == '2':
		print(" [ 학생 성적 출력 ] ")
		for t in s_title:
			print(t,end='\t')
		print()
		print("ㅡ"*32)

		for s in students:
			print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}".format(s['no'],s['name'],s['kor'],s['eng'],s['math'],s['total'],s['avg'],s['rank']),end='\t')
			print()

	elif choice == '3':
		print(" [ 학생 성적 수정 ] ")
		

	elif choice == '4':
		print(" [ 학생 성적 검색 ] ")
		search = input("학생 이름 검색 (메뉴로 이동->0)>>")
		for s in students:
			if s['name'] == search:
				chk = 1
				print(f"{s['name']} 학생을 찾았습니다.")
				print(f"{s['name']} 학생의 성적")
				for t in s_title:
					print(t,end='\t')
				print()
				print("ㅡ"*32)
				print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}".format(s['no'],s['name'],s['kor'],s['eng'],s['math'],s['total'],s['avg'],s['rank']),end='\t')
				print()		
		if chk != 1:
			print(f"{search} 학생의 검색 결과가 없습니다.")
				


	elif choice == '5':
		print(" [ 학생 성적 삭제 ] ")


	elif choice == '6':
		print(" [ 등수 처리 ] ")

	elif choice == '7':
		while True:
			print("[ 학생 성적 정렬 ]")
			print("1. 이름 순차정렬")
			print("2. 이름 역순정렬")
			print("3. 합계 순차정렬")
			print("4. 합계 역순정렬")
			print("5. 번호 순차정렬")
			print("0. 메뉴로 이동")
			print("ㅡ"*30)
			choice = input("원하는 번호를 입력하세요.>>")
			if choice == '1':
				students.sort(key=lambda x:x['name'])
			elif choice == '2':
				students.sort(key=lambda x:x['name'],reverse=True)
			elif choice == '0':
				print("이전페이지로 이동")
				break
		print("정렬이 완료되었습니다.")
						
							
		
		
		
		




# 
# 학생 성적 입력 부분을 구현하시오.
# dict 타입으로 입력할 것
# 번호, 이름, 국어, 영어, 수학, 총점, 평균, 등수
# 입력이 완료되면 출력이 바로 되도록 하시오.

# print("[ 학생 성적 입력]")
# print("ㅡ"*25)
# stu = {}
# while True:
# 	stu['no'] = 1
# 	stu['name'] = input("학생 이름 입력 : ")
# 	stu['kor'] = int(input("국어점수 입력 : "))
# 	stu['eng'] = int(input("영어점수 입력 : "))
# 	stu['math'] = int(input("수학점수 입력 : "))
# 	stu['total'] = stu['kor'] + stu['eng'] + stu['math']
# 	stu['avg'] = stu['total']/3
# 	stu['rank'] = 0
# 	stu['no'] += 1
# 	break
# print("번호\t번호\t번호\t번호\t번호\t번호\t번호\t번호\t")
