from django.urls import path, include
from . import views

app_name = 'board'
urlpatterns = [
	# 리스트
    path('blist/', views.blist, name='blist'),
	# 글 상세보기
    path('bview/<int:bno>/', views.bview, name='bview'),

]
