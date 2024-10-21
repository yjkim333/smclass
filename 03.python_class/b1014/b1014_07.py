# stu_title = ['국어','영어','수학']
# students = {'국어':100,'영어':100,'수학':99,'합계':299}

# print("[  점수 수정  ]")
# print("1. 국어점수")
# print("2. 영어점수")
# print("3. 수학점수")
# choice = int(input("수정하려는 과목을 선택하세요.>> "))
# if choice == 1:
# 	print("현재 국어점수 :",students['국어'])
# 	students['국어'] = int(input("변경할 점수 입력>> "))
# 	students['합계'] = students['국어'] + students['영어'] + students['수학']
# elif choice == 2:
# 	print("현재 영어점수 :",students['영어'])
# 	students['영어'] = int(input("변경할 점수 입력>> "))
# 	students['합계'] = students['국어'] + students['영어'] + students['수학']
# elif choice == 3:
# 	print("현재 수학점수 :",students['수학'])
# 	students['수학'] = int(input("변경할 점수 입력>> "))
# 	students['합계'] = students['국어'] + students['영어'] + students['수학']
# print("변경 : ",students)




stu_title = ['국어','영어','수학']
# print(stu_title[0]) # 국어  choice = 1  -> 0+1
# print(stu_title[1]) # 영어  choice = 2	-> 1+1
# print(stu_title[2]) # 수학  choice = 3	-> 2+1
students = {'국어':100,'영어':100,'수학':99,'합계':299}

def s_modify(choice):
	print("현재 {}점수 : {}".format(stu_title[choice-1],students[stu_title[choice-1]]))
	students[stu_title[choice-1]] = int(input("변경할 점수 입력>> "))

print("[  점수 수정  ]")
print("1. 국어점수")
print("2. 영어점수")
print("3. 수학점수")
choice = int(input("수정하려는 과목을 선택하세요.>> "))
if choice == 1:
	s_modify(choice)
	# print("현재 {}점수 : {}".format(stu_title[choice-1],students[stu_title[choice-1]]))
	# students[stu_title[choice-1]] = int(input("변경할 점수 입력>> "))
elif choice == 2:
	s_modify(choice)
	# print("현재 {}점수 : {}".format(stu_title[choice-1],students[stu_title[choice-1]]))
	# students[stu_title[choice-1]] = int(input("변경할 점수 입력>> "))
elif choice == 3:
	s_modify(choice)
	# print("현재 {}점수 : {}".format(stu_title[choice-1],students[stu_title[choice-1]]))
	# students[stu_title[choice-1]] = int(input("변경할 점수 입력>> "))

students['합계'] = students['국어'] + students['영어'] + students['수학']
print("변경 : ",students)
