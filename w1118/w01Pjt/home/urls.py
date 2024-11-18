from django.urls import path,include
from . import views

app_name = ''  # <- name 으로 url 연결 시 사용
urlpatterns = [
    path('',views.index,name='index'),  # urls 추가
	# 메인페이지 이름 - index,main,default
]
