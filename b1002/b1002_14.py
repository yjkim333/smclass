import random

# 1~100의 숫자 중에 랜덤으로 추출
# 입력한 숫자가 랜덤 숫자보다 크면 입력한 숫자가 큽니다
# 입력한 숫자가 랜덤 숫자 보다 작으면 입력한 숫자가 작습니다.
# 10번 도전하도록 하시오
# 정답입니다. 프로그램 종료. break

#### while ####
# i = 0 #초기값
# r_num = random.randint(1,100)
# count = 0
# while i<10: #조건식
#   num = int(input("숫자를 입력하세요."))
#   if num > r_num:
#     print("입력한 숫자가 큽니다.")
#     i +=1 #증감식
#   elif num < r_num:
#     print("입력한 숫자가 작습니다.")
#     i +=1
#   elif num == r_num:
#     print("정답! 정답 번호 : ",num,"\n-프로그램 종료-")
#     count = 1
#     break
    
# # 10번 도전해서 실패할 경우
# if count == 0:
#   print("10번 도전에 실패하셨습니다. 정답 번호는 : ",r_num)


# for
count = 0
r_num = random.randint(1,100)
for i in range(10):
  num = int(input("숫자를 입력하세요."))
  if num<r_num:
    print("입력한 숫자가 작습니다.")
    i+=1
  elif num>r_num:
    print("입력한 숫자가 큽니다.")
    i+=1
  else:
    print("정답! 정답 번호 : ",num,"\n-프로그램 종료-")
    count = 1
    break
# 10번 도전해서 실패할 경우
if count == 0:
  print("10번 도전에 실패하셨습니다. 정답 번호는 : ",r_num)