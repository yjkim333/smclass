from django.shortcuts import render
from students.models import Student

# Create your views here.
def write(request):
	return render(request,'stu_write.html')


# 학생 리스트 가져오기
def list(request):
	qs = Student.objects.all()
	context = {'list':qs}
	return render(request,'stu_list.html',context)

