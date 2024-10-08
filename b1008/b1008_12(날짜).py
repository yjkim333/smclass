import datetime

today = datetime.datetime.now()
# 날짜,시간,밀리초
print(today)

# 날짜 포맷
now_date = today.strftime("%y-%m-%d")
print(now_date)
now_datetime = today.strftime("%y-%m-%d %H:%M:%S")
print(now_datetime)

print(type(now_date))  # -> 타입은 str, 포맷사용하면 타입이 str로 됨