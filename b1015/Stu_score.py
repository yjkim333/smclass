# 모듈 - 함수의 집합

# import 모듈이름  ->  앞에 함수명. 을 써야함
# import S_func

# from 모듈이름 import 불러올함수명 (* -> 전체)
from S_func import *


#####----- 프로그램 시작 -----#####

# 학생성적프로그램
while True:
	choice = title_program()      	# 메뉴출력함수 호출

	if choice == "1":								# 1.학생성적입력함수 호출
		stuNo = stu_input(stuNo)    	

	elif choice == "2":							# 2.학생성적출력함수 호출
		stu_output(students)
		
	elif choice == "3":							# 3.학생성적수정함수 호출
		stu_update(students)

	elif choice == "4":							# 4.학생성적검색함수 호출
		stu_select(students)
			
	elif choice == "5":							# 5.학생성적삭제함수 호출
		stu_delete(students)

	elif choice == "6":							# 6.등수처리함수 호출
		stu_rank(students)
		
	elif choice == "7":							# 7.학생성적정렬함수 호출
		stu_sort(students)

	elif choice == "0":
		print("[ 프로그램 종료 ]")
		print("프로그램을 종료합니다.")
		break

