# if - else
# if elif else

# 100-98 - A+
# 97-94 - A
# 93-90 - A-
# 89-88 - B+
# 87-84 - B
# 83-80 - B-
# 70점 대 - C
# 60점 대 -D
# 60점 미만 - F

num = int(input("숫자입력"))

score = ""
# 중첩if문
if 90<= num:
  score = "A"
  if 98<= num:
    score += "+"
  elif 90 <= num <=93:
    score += "-"
elif 80<=num:
  pass

# 높은 숫자를 위에 써야 and 조건 하나 줄일 수 있다
# if 98 <= num:
#   print("A+")
# elif 94 <= num:
#   print("A")
# elif 90 <= num:
#   print("A-")
# elif 88 <= num:
#   print("B+")
# elif 84 <= num:
#   print("B")
# elif 80 <= num:
#   print("B-")
# elif 78 <= num:
#   print("C+")
# elif 74 <= num:
#   print("C")
# elif 70 <= num:
#   print("C-")
# elif 68 <= num:
#   print("D+")
# elif 64 <= num:
#   print("D")
# elif 60 <= num:
#   print("D-")
# else:
#   print("F")

# if 98 <= num <=100:
#   print("A+")
# elif 94 <= num <=97:
#   print("A")
# elif 90 <= num <=93:
#   print("A-")
# elif 88 <= num <=89:
#   print("B+")
# elif 84 <= num <=87:
#   print("B")
# elif 80 <= num <=83:
#   print("B-")
# elif 78 <= num <=79:
#   print("C+")
# elif 74 <= num <=77:
#   print("C")
# elif 70 <= num <=73:
#   print("C-")
# elif 68 <= num <=69:
#   print("D+")
# elif 64 <= num <=67:
#   print("D")
# elif 60 <= num <=63:
#   print("D-")
# else:
#   print("F")









# 3,4,5월 - 봄 6,7,8월 - 여름 9,10,11 - 가을 12,1,2 -겨울
# num = int(input("숫자입력"))
# if 3<= num <=5:
#   print("봄")
# elif 6<= num <=8:
#   print("여름")
# elif 9<= num <=11:
#   print("가을")
# elif num == 12 or num == 1 or num ==2: # 1<= num <=2 or num==12
#   print("겨울")
# else:
#   print("잘못된 입력")


# 입력한 숫자가 10 이하이거나 100 이상일때 정답입니다. 아니면 오답
# num = int(input("숫자입력"))
# if num <= 10 or num >= 100:
#   print("정답")
# else:
#   print("오답")


# 입력한 숫자가 1 이상 10 이하 때만 정답입니다. 출력 오답입니다 출력
# 1 <= x >= 10    -> 파이썬에선 이렇게 써도 됨
# num = int(input("숫자입력"))
# if num >= 1 and num <= 10:
#   print("정답")
# else:
#   print("오답")

# if 1 <= num <= 10:
#   print("정답")
# else:
#   print("오답")


# # 입력한 숫자가 짝수,홀수인지 출력
# num = int(input("숫자입력"))
# if num%2 == 0:
#   print("짝수입니다.")
# else:
#   print("홀수입니다.")