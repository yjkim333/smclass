from django.db import models

# Create your models here.

## 오라클에서 table 생성 가능, insert,update,select,delete

## 오라클에 접속하지 않고, table 생성가능
## => ORM 방식 (object-relational mapping) - 객체 관계형 맵핑

# Student라는 테이블을 만드는것
class Student(models.Model):
	s_name = models.CharField(max_length=100)
	s_major = models.CharField(max_length=100)
	s_age = models.IntegerField(default=0)
	s_grade = models.IntegerField(default=0)
	s_gender = models.CharField(max_length=30)

	def __str__(self):
		return self.s_name


# ORACLE 에서 테이블 생성
# create table students2 (
# s_name varchar2(100),
# s_major varchar2(100),
# s_age number default 0,
# s_grade number default 0,
# s_gender varchar2(30)
# );

