from django.urls import path,include
from . import views

app_name = 'board'
urlpatterns = [
	
	# 게시판 리스트 페이지
    path('blist/', views.blist, name='blist'),
	
	# 게시글 쓰기 페이지
    path('bwrite/', views.bwrite, name='bwrite'),
	
	# 게시글 상세보기 페이지
    path('bview/<int:bno>/', views.bview, name='bview'),
	
	# 게시글 상세보기 페이지
    path('bmodify/<int:bno>/', views.bmodify, name='bmodify'),

	# 게시글 삭제
		path('bdelete/<int:bno>/', views.bdelete, name='bdelete'),

	# 게시글 답변달기
		path('breply/<int:bno>/', views.breply, name='breply'),


]
