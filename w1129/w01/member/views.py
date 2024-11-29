from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt  # csrf 토큰 예외처리 사용
from django.core import serializers # json타입
from member.models import Member

# 로그인페이지
def login(request):
	return render(request, 'login.html')

# 로그인체크
def loginChk(request):
	id = request.POST.get('id','')
	pw = request.POST.get('pw','')
	print("확인",id,pw)
	# DB확인
	qs = Member.objects.filter(id=id,pw=pw)  # filter - queryset - list
	if qs:
		request.session['session_id'] = qs[0].id
		request.session['session_nickname'] = qs[0].nickname
		list_qs = list(qs.values())
		context = {'result':'success','member':list_qs}
	else:
		context = {'result':'fail'}
	return JsonResponse(context)	# jsonresponse - dic,list타입의 데이터를 보낼 수 있음. 객체자체는 못보냄


# logout
def logout(request):
	request.session.clear()
	return redirect('index')
