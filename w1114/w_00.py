# ip - 네트워크 상의 컴퓨터 주소
# dns(domain name system) - 도메인 주소를 ip주소로 변환
# => www.naver.com -> 211.1.1.2 

# 웹서비스 프레임워크
# django / flask

# http 
# client <---response---|http/smtp/ftp/pop...|---request---> serve
# http - 1.request 2.(server)요청작업수행 3.response 4.연결해제-연결을 유지하기 위해서 쿠키 또는 섹션사용 
# client --post/get/put/delete--> server --create-생성/read-조회/update-수정/delete-삭제--> DB
# CRUD - create-생성(insert)/read-조회(select)/update-수정/delete-삭제
# get - url에 데이터 노출 / 데이터 길이 제한 / 보안에 취약
# post - 요청메세지에 데이터 담음 / 상대적으로 보안에 강함 / django에서 주로 사용

# url
# 기본형태 - https://search.naver.com/search.naver?query=weather
# -> https://-프로토콜 + search.naver.com-도메인 + search.naver-경로 + query(변수)=weather(데이터)-쿼리
# REST URL - https://search.naver.com/search/today/weather
# -> search/today/weather - url 맵핑(데이터)스트링


# 서버구성
# client --> server -> 웹서버 & 애플리케이션 서버  --> DB
# 웹서버 - 주로 정적인 데이터 요청처리 / 동적인 데이터 요청시 애플리케이션 서버에 전달 -> 트래픽 제한 관리 등 프로그램 외적인 부분 관리
# 애플리케이션 서버 - 주로 동적인 데이터 요청 처리 / DB 연동

# http 프로토콜
# 1xx 2xx 3xx 



# pip install --upgrade pip -> pip upgrade

# django -  설치
# pip install Django

# django upgrade
# pip install Django --upgrade

# django 삭제
# django 위치 확인
# python -c "import django; print(django.__path__)"
# 위치 찾아서 django 관련 파일 삭제하면 django 삭제됨.

# cd - change directory
# cd w1114 - w1114 폴더로
# cd.. - 상위 폴더
# c\ - 최상위 폴더


### django 프로젝트 실행 ##

## [프로젝트 생성] ##
# tempPjt (가명)라는 프로젝트 실행
# django-admin startproject tempPjt
# => 기본적인 프레임워크 생성

# 예시
# django-admin startproject shopmall
# django-admin startproject community
# django-admin startproject naverProject
# django-admin startproject kt

# 프로젝트 이름변경
# -> 프로젝트 폴더에서 실행
# move tempPjt tempProject



## [애플리케이션 생성] ##
# -- manage.py 사용 -- 
# python manage.py startapp students


# -- 애플리케이션
# MVC 패턴
# MVT 패턴


# |USER| urls.py -> views.py <--> DB
#                            <--> Templete



###############
# settings.py
# 1
### -- app 추가할 때 설정하는 부분 -- ###
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
# 	# 앱 추가
# 	'students.apps.StudentsConfig',
		##StudentsConfig - students.apps.py 의 class
# ]

# 2
# # 한국어로 설정
# LANGUAGE_CODE = 'ko-kr'
# TIME_ZONE = 'Asia/Seoul'


##########################

# 처음엔 tempPjt의 url로 들어오고,

# tempPjt - urls.py
# 1.
# from django.contrib import admin
### 뒤에 include
# from django.urls import path, include

# urlpatterns = [
# 		### url admin으로 들어오면 -> admin의 urls.py 로 연결해라
#     path('admin/', admin.site.urls),
#			### url students 들어오면 -> students 에서 urls.py 로 연결해라 
###	 	path('students/',include('students.urls'))
# ]


# students - urls.py

# from django.urls import path, include
# from . import views  => view 연결

# app_name = 'students'  => 앱 이름 지정

# urlpatterns = [
# 	### url 주소/ views.py 함수명, url 이름
# 	### url 주소 => http://127.0.0.1:8000/students/reg
# 	path('reg/',views.regStudent,name='reg'),
# ]


###########################
# students-views.py

# from django.shortcuts import render

# # Create your views here.
# def regStudent(request):
# 	return render(request,'register.html')


#####
# students - templates 폴더 생성
# register.html 파일 생성




# html 자동완성키 설정
# 1. extentions- auto close Tag
# 2. ctrl + ,
# 3. setting
# 4. editor:font ligatures
# 5.  
# 	"auto-close-tag.activationOnLanguage": ["*"],
#		"emmet.includeLanguages": { "django-html": "html" },
#  추가


############################

## [ 데이터베이스 생성 - DB 테이블 설치,변경,삭제,추가 ]
# python manage.py migrate
# -> 기본적인 형태의 db테이블 설치

## DB에 table 변경된 것(설치,변경,삭제,추가)이 있는지 확인
# python manage.py makemigrations

## 관리자 등록
# python manage.py createsuperuser

## [ 서버 구동 ]
# python -u manage.py runserver 0.0.0.0:8000
# -> 브라우저 url - http://127.0.0.1:8000/
# -> 관리자 페이지 - http://127.0.0.1:8000/admin


## models.py -> db에 테이블을 만들수 있는 공간

# students-models.py 에서

## 오라클에서 table 생성 가능, insert,update,select,delete

## 오라클에 접속하지 않고, table 생성가능
## => ORM 방식 (object-relational mapping) - 객체 관계형 맵핑

# Student라는 테이블을 만드는것
# class Student(models.Model):
# 	s_name = models.CharField(max_length=100)
# 	s_major = models.CharField(max_length=100)
# 	s_age = models.IntegerField(default=0)
# 	s_grade = models.IntegerField(default=0)
# 	s_gender = models.CharField(max_length=30)

# 	def __str__(self):
# 		return self.s_name


# ORACLE 에서 테이블 생성
# create table students2 (
# s_name varchar2(100),
# s_major varchar2(100),
# s_age number default 0,
# s_grade number default 0,
# s_gender varchar2(30)
# );

# 한 뒤 
# python manage.py makemigrations 으로 확인한번하고
# python manage.py migrate 로 적용

# -------------------
# students-admin.py => 어드민페이지에 Student 클래스가 보임
# from django.contrib import admin
# from students.models import Student

# # Register your models here.
# admin.site.register(Student)

# -------------------
# 테이블에 데이터 입력
# python manage.py shell => cmd-sqlplus 명령어(콘솔창)와 같음
# 
### 콘솔창에서 import!
# from students.models import Student
# ## insert
# qs = Student(s_name='hong1',s_major = '컴퓨터공학',s_age=20,s_grade=1,s_gender='M')
# ## commit
# qs.save()

# print(qs)

# select 복수
# qs = Student.objects.all()
# 
# qs[0],qs[1]

# select 1명
# qs = Student.objects.get(s_name='hong1')
# qs.s_name


### update - 수정
# qs = Student.objects.get(s_name='hong1')
# qs.s_age=25
# qs.save()


### delete - 삭제
# qs = Student.objects.get(s_name='hong1')
# qs.delete()
# qs.save()


# ORACLE
# insert into students2 values('홍길동','com',20,1,'M');
# commit;


############

# http://127.0.0.1:8000/ - root페이지(index페이지)
# http://127.0.0.1:8000/students/write

# <li><a href="/students/write">학생등록 이동</a></li>
# "/students/write" -> root 페이지 뒤에 붙여라

# <li><a href="./students/write">학생등록 이동</a></li>
# "./students/write" -> 현재 페이지 폴더 뒤에 이어서 붙여라

# <li><a href="../students/write">학생등록 이동</a></li>
# "../students/write" -> /하나 앞으로 와서 (이전폴더) 붙여라 http://127.0.0.1:8000/students/뒤에 붙여라

# <li><a href="../../students/write">학생등록 이동</a></li>
# "../students/write" -> /두번 앞으로 와서 (이전폴더의 이전폴더) 붙여라