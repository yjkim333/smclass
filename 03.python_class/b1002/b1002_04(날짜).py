# import datetime
# today = datetime.datetime.now()

from datetime import datetime
today = datetime.now()

# if 12시 이상이면 오후 ,아니면 오전 출력
if today.hour < 12:
  print("오전 입니다.")
else:
  print("오후 입니다.")

# print("{}년 {}월 {}일".format(today.year,today.month,today.day))
# print(today.year,"년",end='')
# print(today.month,"월",end='')
# print(today.day,"일",end='')
# print(today.hour,"시",end='')
# print(today.minute,"분",end='')
# print(today.second,"초",end='')
