# 합수선언
def calc(num,num2,op):
	if op == '+':
		return num+num2
	elif op == '-':
		return num-num2
	elif op == '*':
		return num*num2
	elif op == '/':
		return num/num2

num = int(input("숫자1 >> "))
num2 = int(input("숫자2 >> "))
op = input(" +, -, *, / 중 하나를 선택하세요")

print("결과값 :",calc(num,num2,op))
