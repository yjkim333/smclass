print("{} 평균 : {:.2f}".format("홍길동",(100+100+99)/3))
name = "홍길동"

#f함수 소수점 자리 출력
a=1.12345
print(f"소수점 2자리 출력 : {a:.2f}")

# f함수 프린트 소수점 처리 : format을 적용 후 변수 전달
avg = 99.666667
avg = "{:.2f}".format(99.666667)
print(f"{name} 평균 : {avg}")


print("출력")
print("""\
한국인의 우울증 유병률은 2020년 경제협력개발기구(OECD) 통계에 따르면
36.8%로 세계 최고 수준이다.

한국 건강보험평가원의 자료에 따르면 2021년 한국의 우울증 환자는 93만 명,
불안 장애 환자는 86만 명을 넘는 것으로 집계됐다.
""")

# name = "홍길동"
# num = 100
# num2 = 100
# num3 = 99
# print("%s 합계 : %d" % (name,num+num2+num3))
# print("{} 합계 : {}".format(name,num+num2+num3))
# print("%s 평균 : %.2f" % (name,(num+num2+num3)/3))
# print("{} 평균 : {}".format(name,(num+num2+num3)/3))
# print("{} 평균 : {:.2f}".format(name,(num+num2+num3)/3))

# # 숫자 : 12.12345 , 456.78940, 2.252525
# #소수점 2자리까지 출력
# #숫자 : 12.12, 456.79, 2.25
# print("숫자 : {:.2f},{:.2f},{:.2f}".format(12.12345,456.78940,2.252525))
# print("숫자 : {2:.2f},{1:.2f},{0:.2f}".format(12.12345,456.78940,2.252525)) #순서 바꾸기
# # \n : 단락바꾸기
# print("안녕\n하세요")
# # \특수기호 : 특수기호 출력
# print("\"")
# # \t : tab 기능
# print("안녕\t하세요")
# # \b : backspace 기능
# print("안녕\t\b\b하세요")

# print("한국인의 우울증 유병률은 2020년 경제협력개발기구(OECD) 통계에 따르면 36.8%로 세계 최고 수준이다.\n한국 건강보험평가원의 자료에 따르면 2021년 한국의 우울증 환자는 93만 명, 불안 장애 환자는 86만 명을 넘는 것으로 집계됐다.")
# # """ : 입력한 대로 출력, \:단락 지우기
# print("""\
# 1. 한국인의 우울증 유병률은 2020년 경제협력개발기구(OECD) 통계에 따르면
# 36.8%로 세계 최고 수준이다.

# 한국 건강보험평가원의 자료에 따르면 2021년 한국의 우울증 환자는 93만 명,
# 불안 장애 환자는 86만 명을 넘는 것으로 집계됐다.\
#       """)