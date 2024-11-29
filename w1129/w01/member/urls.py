from django.urls import path, include
from . import views

app_name = 'member'
urlpatterns = [
    path('login/', views.login, name='login'),
    # 로그인체크
    path('loginChk/', views.loginChk, name='loginChk'),
    # 로그인체크
    path('logout/', views.logout, name='logout'),
]

