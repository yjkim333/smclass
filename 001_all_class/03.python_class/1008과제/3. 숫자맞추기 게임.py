import random
# 1~100에서 랜덤 숫자1 생성
while True:
  i = 0
  i_list = []
  r_num = random.randint(1,100)
  print("<10번의 기회 안에 1에서 100사이의 랜덤 숫자를 맞춰보세요.>")
  print()
  while i<10:
    i_num = int(input(f"{i+1}번째 도전>>"))
    if i_num < r_num:
      print("더 큰 숫자를 입력해 보세요")
      print()
      i_list.append(i_num)
    elif i_num > r_num:
      print("더 작은 숫자를 입력해 보세요")
      print()
      i_list.append(i_num)
    elif i_num == r_num:
      print(f"정답입니다! {i+1}번째 도전에 성공하셨습니다!")
      print(f"정답 : {r_num} , 입력 히스토리 : {i_list}")
      print()
      break
    i += 1
  if i == 10:
    print("10번의 기회를 모두 썼습니다. 정답 : ",r_num)
    print()
  choice = int(input("1. 다시하기 \n2. 그만하기"))
  print()
  if choice == 1:
    print("새로운 게임을 시작합니다.")
  elif choice == 2:
    print("게임을 종료합니다.")
    break
      