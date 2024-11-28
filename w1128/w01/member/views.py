from django.shortcuts import render
from member.models import Member
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt  # csrf 토큰 예외처리 사용
from django.core import serializers # json타입



# 로그인 페이지
def login(request):
	return render(request, 'login.html')


# 로그아웃
def logout(request):
	request.session.clear()
	# del request.session['session_id']
	context = {'outmsg':'1'}
	return render(request, 'index.html', context)



# json 타입 변경 -> list,dict 타입으로 변경 / qs - set타입 => list타입으로 변경
# 로그인체크
# @csrf_exempt   # csrf예외처리
def loginChk(request):
	id  = request.POST.get('id','')
	pw  = request.POST.get('pw','')
	qs = Member.objects.filter(id=id,pw=pw)  # 데이터 없으면 None
	# qs = Member.objects.get(id=id,pw=pw)  	# db에  없으면 에러  -> try,exception
	if qs:
		print("성공")
		request.session['session_id'] = id
		request.session['session_nickname'] = qs[0].nickname
		# filter 
		qs_list = list(qs.values())
		context = {"result":"success","member":qs_list}
		# get 
		# json_qs = serializers.serialize('json',[qs]) # json 타입변경
		# context = {"result":"success","member":json_qs}
	else:
		print("실패")
		context = {"result":"fail"}

	return JsonResponse(context)



# 회원가입
def step03(request):
	return render(request, 'step03.html')


# id 중복체크
def idChk(request):
	id = request.POST.get('id')
	qs = Member.objects.filter(id=id)
	if qs:
		context = {"result":"fail"}
	else:
		context = {"result":"success"}
		
	return JsonResponse(context)

