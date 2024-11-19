from django.shortcuts import render,redirect
from students.models import Student
from django.urls import reverse

# 학생등록페이지 열기, 학생등록저장
def write(request):
	if request.method == 'POST':	# 저장 시-> form의 POST 방식
		name = request.POST.get('name')		# request.POST.get('name') -> 데이터가 없을 시 None 리턴, 에러x
		major = request.POST.get('major')
		grade = request.POST['grade']		# request.POST['grade'] -> 데이터가 없을 시 에러
		age = request.POST['age']
		gender = request.POST['gender']
		# hobby = request.POST['hobby'] 	# -> 마지막 1개만 들어옴
		hobbys = request.POST.getlist('hobby')		# -> 리스트 타입으로 checkbox데이터 모두 들어옴
		# hobbys 스트링으로 타입 변경 - join  list -> str타입으로
		# hobby = ','.join(hobbys)
		# hobby 리스트로 타입 변경 - split str -> list타입으로
		# hobby_list = hobby.split(',')

		print(name)
		# print("hobby: ",hobby)
		# print("hobbys복수: ",hobbys)

		# 테이블에 저장 2 가지
		# 1. qs.save()
		qs = Student(name=name,major=major,grade=grade,age=age,gender=gender,hobby=hobbys)
		qs.save()

		# 2. create() -> save() 필요 없음
		# Student.objects.create(name=name,major=major,grade=grade,age=age,gender=gender,hobby=hobbys)

		return redirect('/students/list/')
		# return redirect('index')

	# 학생 페이지 열기
	else:	# request.GET
		# html 파일은 templates 폴더에서 검색
		return render(request,'write.html')
	


### html에서 views.py 로 데이터 넘기는 방법
# 1. form
# 2. 파라미터
# 3. url appname

### views.py에서 html로 데이터 넘기는 방법
# 1. context
# 2. ajax
# 3. 리액트, 뷰



# 학생 리스트 페이지
def list(request):
	# 테이블에서 학생전체정보 가져오기
	# qs = Student.objects.all()
	# 정렬해서 가져오기
	# grade 순차정렬
	# qs = Student.objects.order_by('grade')
	# grade 역순정렬 + name  정렬
	qs = Student.objects.order_by('-grade','name')
	context = {'slist':qs}

	return render(request,'list.html',context)



# 학생 검색
def search(request):
	search = request.GET.get('search')
	print("검색어 :",search)

	# 데이터 검색
	# qs = Student.objects.filter(name=search)
	qs = Student.objects.filter(name__contains=search)

	context = {'slist':qs}

	return render(request,'list.html',context)


# 학생 상세 페이지
def view(request,name):
	qs = Student.objects.get(name=name)
	context = {"stu":qs}

	return render(request,'view.html',context)


# 학생 수정 페이지, 학생 수정 저장
def update(request):
	if request.method == 'GET':
		name = request.GET['name']
		print(name)
		qs = Student.objects.get(name=name)
		context = {'stu':qs}
		return render(request,'update.html',context)
	else:
		name = request.POST.get('name')
		major = request.POST.get('major')
		grade = request.POST.get('grade')
		age = request.POST.get('age')
		gender = request.POST.get('gender')
		hobby = request.POST.getlist('hobby')

		# Student테이블 검색
		qs = Student.objects.get(name=name)
		qs.major = major
		qs.grade = grade
		qs.age = age
		qs.gender = gender
		qs.hobby = hobby
		qs.save()

		return redirect('students:view',name)
		# return redirect(reverse('students:view',args=(name,)))


# 학생 정보 삭제
def delete(request,name):
	print("삭제할 데이터 이름 :",name)
	Student.objects.get(name=name).delete()
	return redirect('/students/list/')
