import datetime
# 현재년도
nowYear = datetime.datetime.now().year
print()
print(datetime.datetime.now().year)

# in_year = input("생일 입력 >> 20020312")
in_year = "20020312"

print(in_year)
print(in_year[:4])
print(nowYear-int(in_year[:4]))


print("현재나이 : ",nowYear-int(in_year[:4]))
