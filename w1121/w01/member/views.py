from django.shortcuts import render,redirect
from member.models import Member

# 로그인페이지, 로그인버튼클릭시
def login(request):
	if request.method == 'GET':
		return render(request,'login.html')
	else:
		id = request.POST.get('id')
		pw = request.POST.get('pw')

		qs = Member.objects.filter(id=id,pw=pw)
		if qs:
			msg = '로그인 성공'
			print(msg)

			## session연결
			request.session['session_id'] = id
			request.session['session_nickname'] = qs[0].nickname

			return redirect('index')
		else:
			msg = '아이디 또는 패스워드가 일치하지 않습니다.'
			print('로그인 실패')
			return render(request, 'login.html', {'login_msg':msg})


# 로그아웃
def logout(request):
	request.session.clear()
	# def request.session['session_id']  # -> 해당 세션 삭제
	return redirect("/")


# 전체회원리스트
def mlist(request):
	id = request.session['session_id']
	if id == 'admin':
		qs = Member.objects.all()
	
	else:
		qs = Member.objects.filter(id=id)
	context = {'mlist':qs}
	return render(request,'mlist.html',context)


# 회원상세페이지
def mview(request,id):
	print("아이디",id)
	qs = Member.objects.filter(id=id)
	context = {'mem':qs[0]}
	return render(request,'mview.html',context)


# 회원정보수정
def mupdate(request,id):
	print("회원정보 :",id)
	if request.method=='GET':
		qs = Member.objects.filter(id=id)
		context = {'mem':qs[0]}
		return render(request,'mupdate.html',context)
	else:
		print("id :",id)
		# 관리자가 아니면, 로그인한 세션아이디 가져옴
		id = request.session['session_id']
		## 관리자 로그인이면, 아이디를 가져와서 저장
		if request.session['session_id'] == 'admin':
			id = request.POST.get('id')
		pw = request.POST.get('pw')
		name = request.POST.get('name')
		nickname = request.POST.get('nickname')
		tel = request.POST.get('tel')
		gender = request.POST.get('gender')
		hobbys = request.POST.getlist('hobby')
		hobby = ','.join(hobbys)

		qs = Member.objects.get(id=id)
		qs.pw = pw
		qs.name = name
		qs.nickname = nickname
		qs.tel = tel
		qs.gender = gender
		qs.hobby = hobby
		qs.save()

		return redirect('member:mlist')


# 회원정보등록
def mwrite(request):
	if request.method=='GET':
		return render(request,'mwrite.html')
	else:
		id = request.POST.get('id')
		pw = request.POST.get('pw')
		name = request.POST.get('name')
		nickname = request.POST.get('nickname')
		tel = request.POST.get('tel')
		gender = request.POST.get('gender')
		hobbys = request.POST.getlist('hobby')
		hobby = ','.join(hobbys)

		Member.objects.create(id=id,pw=pw,name=name,nickname=nickname,tel=tel,gender=gender,hobby=hobby)

		return redirect('member:mlist')
	


# 회원정보삭제
def mdelete(request,id):
	print("회원정보 :",id)
	Member.objects.get(id=id).delete()
	return redirect('member:mlist')
