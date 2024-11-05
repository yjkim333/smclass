### 학생성적프로그램 ##
# students 테이블을 사용해서.
# 1. 학생성적입력
# students_seq,김유신 99 98 96 total avg rank sdate
# 2. 학생성적출력
# 3. 학생성적검색

import oracledb
import stu_func


while True:
	choice = stu_func.main_print() 		# 메인화면 출력부분

	if choice == '1':									# 학생성적입력 부분
		stu_func.stu_insert()

	elif choice == '2':								# 학생성적출력 부분	
		stu_func.stu_output()

	elif choice == '3':								# 학생성적검색 부분	
		stu_func.stu_search()
		
	elif choice == '4':
		stu_func.stu_align()						# 학생성적정렬 부분	
		
	elif choice == '5':
		stu_func.stu_rank()							# 학생등수처리 부분

	elif choice == '0':
		print("-- 프로그램 종료 --")
		break