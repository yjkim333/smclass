from django.contrib import admin
from django.urls import path,include

urlpatterns = [
	# root페이지/admin -> admin 페이지
    path('admin/', admin.site.urls),
    # students의 urls 추가
	# http://127.0.0.1:8000/students
    path('students/',include('students.urls')),
    path('',include('home.urls')),
]
