fruit = []

while True:
  # .strip() : 앞쪽 여백, 뒤쪽여백 제거 (trim)   =>   '사과 ' -> '사과,  ' 사과' -> '사과'
  # .replace(" ","") : 문자대체함수 =>  '사과 ' -> '사과,  ' 사과' -> '사과',  '사 과' -> '사과'
  search = input("과일이름 입력.(종료:x)").replace(" ","")
  # search = input("과일이름 입력.(종료:x)").strip()
  if search == 'x':
    break

  # 입력된 과일 이름을 리스트에 추가하시오
  if search in fruit:
    print("중복입니다.")
  else:
    print(search, "을(를) 추가합니다.")
    fruit.append(search)
    print("입력한 과일 이름 : ",fruit)



# while True:
#   break
# # break, continue -> 반복문일때만 쓴다  -> 반복문을 종료할 때
# print("종료")

# 무한반복문 -> while True:
# a = 0
# while True: #무한 반복
#   print(a)
#   a += 1


# while a<10:
#   a += 1
#   print(a)

# print("프로그램 종료")