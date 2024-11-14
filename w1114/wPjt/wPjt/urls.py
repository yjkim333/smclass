
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('home.urls')),
    path('admin/', admin.site.urls),
    path('event/',include('event.urls')),
    path('students/',include('students.urls')),
	
]
