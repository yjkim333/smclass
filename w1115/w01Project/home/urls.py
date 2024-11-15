from django.urls import path,include

# . -> 현재 폴더에서..
from . import views


app_name = ''  # app 이름 -> url 말고 이름으로 접근할 때 사용
urlpatterns = [
	# Views.py 연결
		path('',views.index,name='index')
]
