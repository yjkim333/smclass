from django.shortcuts import render,redirect
from students.models import Student

# 학생등록페이지, 학생등록저장
def write(request):
	if request.method == 'GET':
		return render(request,'write.html')
	
	else:
		name = request.POST['name']
		major = request.POST['major']
		grade = request.POST.get('grade')
		age = request.POST['age']
		gender = request.POST['gender']
		hobbys = request.POST.getlist('hobby')

		# Student 테이블 저장
		Student.objects.create(name=name,major=major,grade=grade,age=age,gender=gender,hobby=hobbys)

		return redirect('/students/list/')



# 전체학생리스트
def list(request):
	qs = Student.objects.all()
	context = {"slist":qs}
	return render(request,'list.html',context)


# 학생상세페이지
def view(request,name):
	qs = Student.objects.get(name=name)
	context = {"stu":qs}
	return render(request,'view.html',context)


# 학생정보수정
def update(request):
	if request.method == 'GET':
		name = request.GET['name']
		qs = Student.objects.get(name=name)
		context = {"stu":qs}
		return render(request,'update.html',context)