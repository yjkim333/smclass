from django.urls import path,include
from . import views

app_name = 'students'		# app_name 설정
urlpatterns = [
		#		(url 링크, views함수호출, name링크)
		path('write/', views.write, name='write'),

		# 리스트
		path('list/', views.list, name='list'),
		
		# 검색
		path('search/', views.search, name='search'),

		# 학생상세
		# <str:name>/view/ -> list.html에서 보낸 s.name 을 받아야함.
		path('view/<str:name>/', views.view, name='view'),

		# 학생수정
		path('update/', views.update, name='update'), # 파라미터 형태
		# path('update/<str:name>/', views.update, name='update'),

		# 학생삭제
		path('delete/<str:name>/', views.delete, name='delete'),
]