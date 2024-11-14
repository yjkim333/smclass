"""
URL configuration for tempPjt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	### url admin으로 들어오면 -> admin의 urls.py 로 연결해라
    path('admin/', admin.site.urls),
	### url students 들어오면 -> students 에서 urls.py 로 연결해라
	path('students/',include('students.urls')),
    path('event/',include('event.urls')),
	# 주소가 아무것도 들어오지 않으면 home의 urls로 연결
    path('',include('home.urls')),
]
