from django.urls import path,include

# . -> 현재 폴더에서..
from . import views


app_name = 'students'  # app 이름 -> url 말고 이름으로 접근할 때 사용
urlpatterns = [
	# Views.py 연결
	# 루트페이지/students/write
	# name -> app 함수호출 이름
		path('write/',views.write,name='write'),
		
		path('save/',views.save,name='save'),
		path('list/',views.list,name='list'),
]
