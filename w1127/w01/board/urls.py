from django.urls import path,include
from . import views

app_name = 'board'
urlpatterns = [
	# 게시판리스트
    path('blist/', views.blist, name='blist'),
	# 게시글쓰기
    path('bwrite/', views.bwrite, name='bwrite'),
	# 게시글쓰기
    path('bview/<int:bno>/', views.bview, name='bview'),
	# 게시글수정
    path('bupdate/<int:bno>/', views.bupdate, name='bupdate'),
]
