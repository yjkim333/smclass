# class 생성
class Car:
	def __init__(self,color,tire,gear,speed):
		self.color = color
		self.tire = tire
		self.gear = gear
		self.__speed = speed

	def upSpeed(self,value):
		if value > 0: self.__speed += value
		else:
			raise "값을 잘못넣었습니다."
	
	def downSpeed(self,value):
		self.__speed -= value


c1 = Car("white",4,"auto",0)
c1.color = "blue"
print(c1.color)
c1.speed = 300
print(c1.__speed)



# class 사용하려면 class 선언!! 해야함!
# c1 = Car()  # class 선언
# print(c1.color)
# print(c1.tire)

# 속도  = 0 -> 100 바꾸는 방법

# c2 = Car()
# c2.color = 'red'
# print(c2.color)
# print(c1.color)


# 리스트,딕셔너리 - 변수에 직접 값을 할당하는 방식 (보안상 좋지 않은 방법)

# 1) speed 변수에 직접 값을 할당
# c1.speed = 100
# print(c1.speed)

# 2) 함수를 활용해서 값을 할당 (권장방법)
# c1.upSpeed(100)
# print(c1.speed)


