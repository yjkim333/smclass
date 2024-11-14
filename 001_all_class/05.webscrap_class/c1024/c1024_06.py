lists = ['10억','9억 5,000','11억 500','7억','12억 5,250']
a = '9억 5,000'
# 숫자로 변경하는 방법
def num_chg(p):
  b = p.split('억')
  f_num = int(b[0])*1000000000
  if b[1].strip() != '':
    s_num = int(b[1].strip().replace(",",""))*10000
  else:
    s_num = 0
  price = f_num+s_num
  return price

for l in lists:
  price = num_chg(l)
  print("금액 :",price)
  

r_list = list(map(num_chg,lists))
print(r_list)