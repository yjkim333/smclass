from django.shortcuts import render,redirect
from member.models import Member

# 로그인 페이지 열기, 로그인 확인
def login(request):
	if request.method == 'GET':
		return render(request, 'login.html')
	else:
		id = request.POST.get('id')
		pw = request.POST.get('pw')

		qs = Member.objects.filter(id=id,pw=pw)

		if qs:
			print("로그인 성공")
			request.session['session_id'] = qs[0].id
			request.session['session_nickname'] = qs[0].nickname
			context = {"lmsg":"1"}
		else:
			print("로그인 실패")
			context = {"lmsg":"0"}
		return render(request, 'login.html', context)
	

# 로그아웃
def logout(request):
	request.session.clear()
	return redirect('index')

