# 10은 2의 배수입니다.
print("%d은 %d의 배수입니다." % (10,2))
#변수
a = 10
b = 2
print(a,b)

# 출력 자릿수 표시
# 10/3
print("%d" % b)
print("%5d" % b) # %5d - 공간 5자리 확보
print("%05d" % b) # %05d - 공간 5자리 확보에 0을 넣음
#001 010 100.00 출력
num = 1
num2 = 10
num3 = 100
# print("%03d" % num)
# print("%03d" % num2)
# print("%.2f" % num3)
# print("%03d %03d %.2f" % (num,num2,num3))
# print("%05d" % (-10))

print("%.2f" % (758.12345678))
print("%013.2f" % (25.05)) #소수점도 한자리를 차지함
num4 = 150.15
print("%d %.f %s" % (num4,num4,num4))
print("숫자 : ",10) # 타입이 다른것을 쓸때는 , 를 씀
#print("숫자 : "+10) #에러- 타입이 다른 것에 + 할 수 없음
print("*" * 10)
print("%5.1f" % (123456789.123))

# 10*2=20
# print("%d * %d = %d" % (a,b,a*b))

# 사용표시
# ** %d-정수, %f-실수, %s-문자열, %c-문자1개, **  %.2f
# name = "홍길동"
# kor = 100
# eng = 100
# math = 99
# # 홍길동 총 합 : 299, 평균 : 99.33333
# print("%s 총 합 : %d, 평균 : %.2f" % (name,kor+eng+math,(kor+eng+math)/3))






#### print 사용 형태 ####
# print 1) , 2) % 3) format 4) f
# print(a,"은",b,"의 배수입니다.")
# print("%d은 %d의 배수입니다." % (a,b))
# print("{}은 {}의 배수입니다.".format(a,b))
# print(f"{a}은 {b}의 배수입니다.")
# #print(a+"은"+b+"의 배수입니다.") -> 안됨