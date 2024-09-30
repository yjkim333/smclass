# stu_data = ['홍길동',100,100,100,99]
# for s in stu_data:
#   print(s)

# 학생이름 : 홍길동
# 국어점수 : 100
# 영어점수 : 100
# 수학점수 : 100
# 과학점수 : 99
# 합계 : 
# 평균 : 
# name = stu_data[0]
# kor = stu_data[1]
# eng = stu_data[2]
# math = stu_data[3]
# sci = stu_data[4]
# total = kor+eng+math+sci
# avg = total/4

# print("학생이름 : {}".format(name))
# print("국어점수 : {}".format(kor))
# print("영어점수 : {}".format(eng))
# print("수학점수 : {}".format(math))
# print("과학점수 : {}".format(sci))
# print("합계 : {}".format(total))
# print("평균 : {:.1f}".format(avg))

#이순신의 평균을 출력하시오
stu_title = ['번호','이름','국어','영어','수학','과학','합계','평균']
stu_datas = [[1,'유관순',100,100,100,99],[2,'이순신',100,100,100,99],[3,'김구',100,100,100,99]]
  #학생데이터에서 합계 평균을 추가해서 1줄로 출력하시오.
print("                    [학생성적 프로그램]")
# print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(stu_title[0],stu_title[1],stu_title[2],stu_title[3],stu_title[4],stu_title[5],stu_title[6],stu_title[7],))
# print("-"*60)
for s_t in stu_title:
  # print("{}".format(s_t),end='\n') 
  # print("{}".format(s_t)) 위에거랑 같은거 
  print("{}".format(s_t),end='\t') # end=' ' : 공백을 주고 옆으로 출력함
print() #줄단락 바뀜
print("-"*60)


for d in stu_datas:
  # print(d)
  print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{:.1f}".format(d[0],d[1],d[2],d[3],d[4],d[5],d[2]+d[3]+d[4]+d[5],(d[2]+d[3]+d[4]+d[5])/4))
  ##번호,이름,국어,영어,수학,과학,합계,평균



#print("이순신의 평균 : {}".format((stu_datas[1][1]+stu_datas[1][2]+stu_datas[1][3]+stu_datas[1][4])/4))


#원의 넓이 : 반지름 * 반지름 * 3.14
#두개의 길이를 입력받아 삼각형의 넒이, 직사각형 넓이를 구하시오
# length = input("2개의 길이를 입력하세요.")
# print(length.split(" "))
# l_list = length.split(" ")
# print("삼각형의 넓이 : {}".format(float(l_list[0])*float(l_list[1])*0.5))
# print("사각형의 넓이 : {}".format(float(l_list[0])*float(l_list[1])))



# l = int(input("길이1을 입력하세요."))
# l2 = int(input("길이2를 입력하세요."))
# print((l * l2)*0.5)
# print(l * l2)


#반지름을 입력받아 원의 넓이를 구하시오
# r = input("반지름을 입력하세요.")
# print((int(r)**2)*3.14)

# r = int(input("반지름을 입력하세요."))
# area = r ** 2 * 3.14
# print("원의 넓이 : ",area)
# print("원의 넓이 : {.1f}".format(area))

## 복합대입연산자 +=, -=, *=, /=, //=, $=, **=
# a = 10
# print(a + 5)
# a +=5; print(a)
# a -=5; print(a)
# a *=5; print(a)
# a /=5; print(a)
# a //=5; print(a)
# a **=5; print(a)
# a %=5; print(a)


# 증가연산자 감소연산자 ++ -- 없음


## 숫자를 문자열로 변환 ##
# 문자열 + 숫자 -> 불가
# a = 100
# b = 10
# print(str(a)+str(b))


## 문자형 숫자 변환 ##
# a = "100"
# b = "10.5" 
# c = "안녕"
# print(float(a))    #정수형 -> 정수타입, 실수타입 변경가능
# #print(int(b))     #실수형 -> 실수타입으로만 변경가능 
# #print(float(c))   #글자는 숫자형으로 변경 불가


# # 1줄 선언 2가지 방법
# s1,s2,s3 = 1,2,3
# a = 10; b = 5

## 사칙연산 우선순위
#print(2 + 2 - 2 * 2 / 2 * 2)


## 사칙연산, 추가적 연산 // % **
# a = 5; b = 3 #1줄에 여러 변수 넣을 때 ; 넣어주면 됨
# # /, %, //, **
# print("{}".format(a/b))
# print("{}".format(a%b))
# print("{}".format(a//b))
# print("{}".format(a**b))
# # print("{},{},{},{}".format(a/b,a%b,a//b,a**b))
