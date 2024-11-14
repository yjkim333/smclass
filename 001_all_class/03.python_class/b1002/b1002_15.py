import random

i = 0
r_num = random.randint(1,100)
count=0
while i<10:
  num = int(input("숫자 입력 :"))
  if num > r_num:
    print("커요")
    print(i+1,"번째 도전입니다.")
    i += 1
  elif num < r_num:
    print("작아요")
    print(i+1,"번째 도전입니다.")
    i += 1
  else:
    print(i+1,"번째 도전에 정답! ",r_num)
    count = 1
    break
if count == 0:
  print("10번 기회가 끝났습니다. 정답은 ",r_num)
