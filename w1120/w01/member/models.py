from django.db import models

class Member(models.Model):
	id = models.CharField(max_length=50, primary_key=True)
	pw = models.CharField(max_length=100, blank=False)  #blank=False -> 데이터가 꼭 있어야 한다
	name = models.CharField(max_length=100)
	nickname = models.CharField(max_length=100)
	cdate = models.DateTimeField(auto_now=True)		# auto_now=True -> 자동으로 현재시간 입력

	def __str__(self):
		return f"{self.id},{self.name}"