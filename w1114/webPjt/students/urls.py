
from django.urls import path,include
# . -> 현재폴더
# 현재폴더에서 views 찾아줘
from . import views

app_name = 'students'

urlpatterns = [
	path('write/',views.write, name='write')
]
