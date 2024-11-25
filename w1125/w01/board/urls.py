from django.urls import path,include
from . import views

app_name = 'board'
urlpatterns = [
	# 게시판 리스트
    path('blist/', views.blist, name='blist'),
	# 글쓰기 페이지
    path('bwrite/', views.bwrite, name='bwrite'),
	# 글 상세 페이지
    path('bview/<str:bno>/', views.bview, name='bview'),
	# 글 상세 - 삭제
    path('bdelete/<str:bno>/', views.bdelete, name='bdelete'),
	# 글 상세 - 수정
    path('bupdate/<str:bno>/', views.bupdate, name='bupdate'),
	# 글 상세 - 답글쓰기
    path('breply/<str:bno>/', views.breply, name='breply'),
]
