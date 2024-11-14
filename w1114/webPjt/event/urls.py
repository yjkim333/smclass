
from django.urls import path,include
# . -> 현재폴더
# 현재폴더에서 views 찾아줘
from . import views

app_name = 'event'

urlpatterns = [
	path('event1/',views.event1, name='event1')
]
