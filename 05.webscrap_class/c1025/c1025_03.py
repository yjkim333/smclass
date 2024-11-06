# a= [1,2,3]
# b=[4,5,6,7]
# print(a+b)

a = ['1만','3,450','1.7만','500','1,000']
# float 타입으로 변경해서 리스트 저장


def chg(val):
	if '만' in val:
		r_val = float(val[:-1])*10000
	else:
		r_val = float(val.replace(",",""))
		return r_val
	
a_list = list(map(chg,a))
print(a_list)

# 최대값
print(max(a_list))
# 최소값
print(min(a_list))
# 정렬
print(a_list.sort())
print(a_list.sort(reverse=True))





# b = "1.7만"

# c = b.split("만")
# print(c)
# if "만" in b:
# 	c = b.split("만")
# 	c[0] = float(c[0])*10000
# 	print(c[0])
# else:

# # print(c[0])


