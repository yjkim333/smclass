from django.urls import path
from . import views

app_name = 'students'
urlpatterns = [
	# 학생등록페이지
    path('write/', views.write, name='write'),
	# 전체학생리스트페이지
		path('list/', views.list, name='list'),
	# 학생상세페이지
		path('<str:name>/view/', views.view, name='view'),
	# 학생정보수정페이지
		path('<str:name>/update/', views.update, name='update'),

]
