from django.urls import path,include
from . import views

app_name = 'member'
urlpatterns = [
	# 로그인
    path('login/', views.login, name= 'login'),
	# 로그아웃
    path('logout/', views.logout, name= 'logout'),
	# 회원리스트
    path('mlist/', views.mlist, name= 'mlist'),
	# 회원상세
    path('mview/<str:id>/', views.mview, name= 'mview'),
	# 회원수정
    path('mupdate/<str:id>/', views.mupdate, name= 'mupdate'),
	# 회원등록
    path('mwrite/', views.mwrite, name= 'mwrite'),
	# 회원삭제
    path('mdelete/<str:id>/', views.mdelete, name= 'mdelete'),
]
