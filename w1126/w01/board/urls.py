from django.urls import path,include
from . import views

app_name = 'board'
urlpatterns = [
	# 게시판리스트
    path('blist/', views.blist, name='blist'),
	# 글쓰기
    path('bwrite/', views.bwrite, name='bwrite'),
	# 글상세보기
    path('bview/<int:bno>/', views.bview, name='bview'),
	# 글 삭제
    path('bdelete/<int:bno>/', views.bdelete, name='bdelete'),
	# 글 수정
    path('bupdate/<int:bno>/', views.bupdate, name='bupdate'),
	# 답글 쓰기
    path('breply/<int:bno>/', views.breply, name='breply'),
]
