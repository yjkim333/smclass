from django.urls import path, include
from . import views

app_name = 'comment'
urlpatterns = [
	# 리스트
    path('clist/', views.clist, name='clist'),
	# 댓글 저장
    path('cwrite/', views.cwrite, name='cwrite'),

]
