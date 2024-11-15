from django.shortcuts import render
from students.models import Student

# Create your views here.
def write(request):
	return render(request,'stu_write.html')


# 학생 리스트 가져오기
def list(request):
	qs = Student.objects.all()
	# {'list':qs} 에서 'list' 는 qs 담는 변수 -> stu_list.html 에서 불러오는 변수
	context = {'list':qs}
	return render(request,'stu_list.html',context)

