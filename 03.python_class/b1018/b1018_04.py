# 반지름을 입력받아, 원릐 둘레와 넓이를 출력하시오.

# 절차적인 형태의 프로그램 구현
# r = int(input("반지름 입력 >> "))
# print(f"원의 둘레 : {2*3.14*r}")
# print(f"원의 넓이 : {3.14*r**2}")

# 클래스 생성
class Circle:
	def __init__(self,r):
		self.__r = r   # __ -> 변수에 직접적으로 접근 제한

	# 원의 넓이
	def get_area(self):
		return 3.14*self.__r**2
	
	# 원의 둘레
	def get_circum(self):
		return 2*3.14*self.__r

# 클래스 선언
c1 = Circle(int(input("반지름 입력 >> ")))

c1.r = 7
print("둘레:",c1.get_circum())
print("넓이:",c1.get_area())

# print(c1.r)
# print(f"원의 둘레 : {2*3.14*c1.r}")
# print(f"원의 넓이 : {3.14*c1.r**2}")

c2 = Circle(int(input("반지름 입력 >> ")))
print("둘레:",c2.get_circum())
print("넓이:",c2.get_area())
