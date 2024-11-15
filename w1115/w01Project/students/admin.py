from django.contrib import admin
from students.models import Student

# Register your models here.

# admin 페이지에 컬럼 보여지는 부분
# list_display에 있는 컬럼 보여줘라
class StudentAdmin(admin.ModelAdmin):
	list_display = ['s_name','s_major','s_age']


# admin 사이트에 추가
admin.site.register(Student,StudentAdmin)