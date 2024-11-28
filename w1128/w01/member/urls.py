from django.urls import path, include
from . import views

app_name = 'member'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('loginChk/', views.loginChk, name='loginChk'),
	# 회원가입
    path('step03/', views.step03, name='step03'),
	# 중복확인
    path('idChk/', views.idChk, name='idChk'),
]
