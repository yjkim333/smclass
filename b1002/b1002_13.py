import random # 랜덤 사용시 써야함

aArr = []
# randint
# 0~9까지의 랜덤 숫자 추출해서 aArr에 10번을 추가하시오
# 같은 숫자는 제외하고 입력을 하세요.
# for i in range(10):
#   r_num = random.randint(0,9)
#   if r_num not in aArr:
#    aArr.append(r_num)
# print(aArr)

# 10개 채워서 넣기
i = 0
while i<10: # 10개일 때 종료
  r_num = random.randint(0,9)
  if r_num not in aArr:
   aArr.append(r_num)
   i += 1

print(aArr)