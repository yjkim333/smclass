import os


f = open('C:/workspace/smclass/b1017/cart.txt','r',encoding='utf-8')
while True:
	line = f.readline()
	if not line : break
	print(line.strip())

# isfile() - 파일인지 아닌지
# exists() - 파일이 존재하는지

if os.path.isfile("b1017/students.txt"):
	print("파일 있음")
else:
	print("파일 없음")
