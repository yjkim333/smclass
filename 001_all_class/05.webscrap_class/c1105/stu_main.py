### 학생성적프로그램 ##
# students 테이블을 사용해서.

import oracledb
import stu_func


while True:
	choice = stu_func.main_print() 		# 메인화면 출력부분

	if choice == '1':									# 학생성적입력 부분
		stu_func.stu_insert()

	elif choice == '2':								# 학생성적출력 부분	
		stu_func.stu_output()

	elif choice == '3':								# 학생성적검색 부분	
		stu_func.stu_select()
		
	elif choice == '4':								# 학생성적정렬 부분	
		stu_func.stu_sort()
		
	elif choice == '5':								# 학생등수처리 부분
		stu_func.stu_rank()

	elif choice == '0':
		print("-- 프로그램 종료 --")
		break