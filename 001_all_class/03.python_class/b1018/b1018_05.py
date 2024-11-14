class Circle:
	def __init__(self,r):
		self.__r = r  # 내부클래스에서만 변수에 접근해서 수정이 가능함

	# 원의 넓이
	def get_area(self):
		return 3.14*self.__r**2
	
	# 원의 둘레
	def get_circum(self):
		return 2*3.14*self.__r

	# gettrt,setter
	def get_r(self):
		return self.__r
	
	def set_r(self,r):
		self.__r = r

	# 참조변수를 출력할 때 리턴되는 함수 : __str__()
	def __str__(self):
		c_str = "반지름의 길이 : {}, 원의 넓이 : {}, 원의 둘레 : {:.2f}".format(self.__r,self.get_area(),self.get_circum())
		return c_str

c1 = Circle(10)
print(c1)





# # 클래스 선언
# # _ 나 __ 나 내부적으로 캡슐화하겠다고 선언
# c1 = Circle(10)															  	 # 1. 선언 안에서 값을 입력
# print("c1 길이",c1.get_r())										   # 2. getter로 값을 출력
# c1.set_r(200)																     # 3. setter로 값을 입력
# print("c1 길이 변경",c1.get_r())						 		 # 4. getter로 값을 출력
# c1.__r = 100																			# 5. 변수 직접 입력
# print("c1 길이 직접 변경",c1.__r)									 # 6. 변수 직접 출력
# print("get으로 읽어온 r",c1.get_r())					   # 7. getter로 값을 출력