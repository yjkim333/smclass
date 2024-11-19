from django.db import models


class Student(models.Model):
	## primary key 를 설정하지 않으면 자동으로 pk=id 가 생성
	name = models.CharField(max_length=100)
	major = models.CharField(max_length=100)
	grade = models.IntegerField(default=1)
	age = models.IntegerField(default=1)
	gender = models.CharField(max_length=10)
	hobby = models.CharField(max_length=50)

	def __str__(self):  # __str__ -> 문자열만 리턴
		return f"{self.name},{self.major},{self.grade}"