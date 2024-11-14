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
from django.urls import path, include
from . import views

app_name = 'students'

urlpatterns = [
	### url 주소/ views.py 함수명, url 이름
	### url 주소 => http://127.0.0.1:8000/students/reg
	### 이름으로 연결 => students:reg <- app_name:name
	path('reg/',views.regStudent,name='reg'),
]
