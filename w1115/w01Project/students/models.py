from django.db import models

## DB 생성

## ORM 구조 (Object Relational Mapping)
# - 객체(object)와 DB의 테이블을 자동으로 연결(mapping) 시켜 RDB 테이블을 객체 지향적으로 사용하게 해주는 기술
# - 다만 ORM 만으로는 SQL의 모든 부분을 다루기 어려움.

# Create your models here.

class Student(models.Model):
	s_name = models.CharField(max_length=100)
	s_major = models.CharField(max_length=100)
	s_grade = models.IntegerField(default=0)
	s_age = models.IntegerField(default=0)
	s_gender = models.CharField(max_length=30)

	# class -> oracle table 자동구성
	# def 는 class 안쪽에!
	def __str__(self): # -> str타입만 보여지게 함.
		return self.s_name



# [model ORM 명령어]

## [입력 - insert]
# qs = Student(s_name = '홍길동',s_major = '컴퓨터공학',s_grade=1,s_age=20,s_gender='M')
# qs.save()

# Student.objects.create(s_name = '홍길동',s_major = '컴퓨터공학',s_grade=1,s_age=20,s_gender='M')
# -> qs.save() 안해도 됨


## [검색 - select]
# - 전체 검색 -
# qs = Student.objects.all()
# qs[0]
# qs[1]
# - 부분 검색 -
# qs = Student.objects.get(s_name='홍길동')
# Student 객체타입 -> qs.s_name
# qs = Student.objects.filter(s_name='홍길동')
# Queryset 타입 - 1개가 넘어와도 리스트형태 -> qs[0].s_name
# qs
# - 비교 검색 -
# __lt - ~ 보다 적음
# __lte - ~ 보다 같거나 작다
# __gt - ~ 보다 크다
# __gte - ~ 보다 같거나 크다
# __isnull - null인자료검색
# __contains - 특정문자열포함
# __startswith - 특정문자열로 시작
# __endswith - 특정문자열로 끝남
# qs = Student.objects.filter(s_age__lt=21)
# qs = Student.objects.filter(s_name__contains='순')


## [수정 - update]
# - 해당 데이터 검색 후 컬럼에 수정 값을 입력하면 수정됨.
# qs = Student.objects.get(s_name='홍길동')
# qs.s_age = 30
# qs.save()


## [삭제 - delete]
# 1
# Student.objects.get(s_name='홍길동').delete()
# 2
# qs = Student.objects.get(s_name='홍길동')
# qs.delete()