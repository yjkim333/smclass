
from django.urls import path,include
from . import views

app_name = 'event'
urlpatterns = [
    path('event1/',views.event1,name='event1'),
	
]
