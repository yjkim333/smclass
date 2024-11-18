from django.urls import path,include
from . import views

app_name = 'board'  # <- name 으로 url 연결 시 사용
urlpatterns = [
    path('list/',views.list,name='list'),  
]
