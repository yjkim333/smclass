from django.shortcuts import render,redirect
from students.models import Student

# 학생 입력 페이지 호출 및 저장
# render - 페이지 호출
# redirect - 데이터 저장
def write(request):
	if request.method == 'GET':
		# render - html 파일 호출
		print("get 방식으로 들어옴")
		return render(request, 'write.html')
	else:
		print("post 방식으로 들어옴")
		name = request.POST['name']
		major = request.POST['major']
		grade = request.POST['grade']
		age = request.POST['age']
		gender = request.POST['gender']
		print('입력데이터 :',name,major,grade,age,gender)

		## DB 저장
		Student.objects.create(name=name,major=major,grade=grade,age=age,gender=gender)
		print('1명 학생 저장')

		return redirect('students:list')
		# return redirect('/students/list/')
	


# 학생리스트 페이지 호출
def list(request):
	qs = Student.objects.all()
	context = {"slist":qs}
	# context - html로 데이터 전달 변수
	return render(request,'list.html',context)
	


# 학생상세정보페이지
def view(request,name):
	print('이름 :',name)
	qs = Student.objects.filter(name=name)	# filter -> 1개의데이터-list타입으로 / 없을 경우 {} - 빈 queryset이 넘어옴
	# qs = Student.objects.get(name=name)   # -> 없을 경우 에러  -> try except 사용해야함
	# qs = get_object_or_404(Student,name = name) # -> 없을 경우 구문 리턴
	print(qs)
	context = {'stu':qs[0]} # qs -> filter로 queryset 리스트 타입으로 넘어오기 때문
	return render(request,'view.html',context)




# 학생수정 페이지
# 1. url - 매개변수로 데이터값을 전달 받음.
def modify(request,name):
	if request.method == 'GET':
		print('modify 이름 :',name)
		# 1개 데이터 가져오기
		qs = Student.objects.filter(name=name)
		context = {'stu':qs[0]}
		return render(request,'update.html',context)
	else:
		print("POST 호출")
		qs = Student.objects.get(name=name)
		name = request.POST['name']
		major = request.POST['major']
		grade = request.POST['grade']
		age = request.POST['age']
		gender = request.POST['gender']
		print("수정 modify 정보 :",name,major,grade,age,gender)
		## DB 저장
		qs.major = major
		qs.grade = grade
		qs.age = age
		qs.gender = gender
		qs.save()
		return redirect('students:list')

# 2. 파라미터
def modify2(request):
	name = request.GET.get('name')
	print('modify2 이름 :',name)
	# 1개 데이터 가져오기
	qs = Student.objects.filter(name=name)
	context = {'stu':qs[0]}
	return render(request,'update.html',context)

# 3. appname - 매개변수로 데이터값을 전달 받음.
def modify3(request,name):
	print('modify3 이름 :',name)
	# 1개 데이터 가져오기
	qs = Student.objects.filter(name=name)
	context = {'stu':qs[0]}
	return render(request,'update.html',context)



# 학생삭제
def delete(request,name):
	print("삭제정보 :",name)
	Student.objects.get(name=name).delete()
	return redirect('students:list')














# # 학생 입력 페이지 호출
# def write(request):
# 	# render - html 파일 호출
# 	return render(request, 'write.html')


# # 학생 입력데이터 저장
# def doWrite(request):
# 	if request.method == 'POST':
# 		name = request.POST['name']
# 		major = request.POST['major']
# 		grade = request.POST['grade']
# 		age = request.POST['age']
# 		gender = request.POST['gender']
# 		print('입력데이터 :',name,major,grade,age,gender)
# 	else:
# 		print("해당되는 데이터가 없습니다.")

# 	return redirect('/')

