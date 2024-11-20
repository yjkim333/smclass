from django.shortcuts import render,redirect
from member.models import Member

# 로그인 페이지
def login(request):
	if request.method == 'GET':
		response = render(request,'login.html')
	else:
		emsg = ''
		id = request.POST.get('id')
		pw = request.POST.get('pw')
		qs = Member.objects.filter(id=id,pw=pw)
		if qs:
			context = {'emsg':emsg,'member':qs[0]}
			request.session['session_id'] = id
			request.session['session_nickName'] = qs[0].nickName
			response = render(request, 'index.html', context)
		else:
			emsg = "일치하는 아이디 또는 비밀번호가 없습니다."
			context = {'emsg':emsg,'member':''}
			response = render(request, 'login.html', context)
	return response


# 로그아웃
def logout(request):
	# session 모두 삭제
	request.session.clear()
	# 해당 session 삭제
	# del request.session['session_id']
	return redirect('index')



# 쿠키 만들기 페이지
def cookWrite(request):
	response = render(request, 'cookWrite.html')
	if request.method == 'GET':
		print("GET 방식으로 들어옴")
	else:
		response = render(request, 'index.html')
		print("POST 방식으로 들어옴")
		ckey = request.POST.get('ckey')
		cvalue = request.POST.get('cvalue')
		response.set_cookie(ckey,cvalue)
	return response


# 쿠키 삭제
def cookDelete(request):
	if request.method == 'GET':
		response = render(request, 'cookDelete.html')
	else:
		response = render(request, 'index.html')
		c = request.POST.get('ckey')
		response.delete_cookie(c)
		print(c,"쿠키 삭제됨")	
	return response
		



# 회원리스트
def mlist(request):
	return render(request, 'mlist.html')