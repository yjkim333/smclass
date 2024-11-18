from django.contrib import admin
from students.models import Student

# admin 페이지의 Student테이블에 보여줄 카테고리
class StudentAdmin(admin.ModelAdmin):
	list_display = ['name','major','grade','age','gender']


# Register your models here.
# admin에 등록
admin.site.register(Student,StudentAdmin)
