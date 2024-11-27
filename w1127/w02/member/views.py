from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from member.models import Member
from django.core import serializers  # json 타입

# 로그인
def login(request):
	return render(request, 'login.html')


# ajax 통신
# csrf_token
# @csrf_exempt	# csrf_token 예외처리 할 수 있음
def loginChk(request):
	# {'name':'KIM','age':20} - 데이터
	id = request.POST.get('id','')
	pw = request.POST.get('pw','')
	print("html에서 넘어온 data :",id,pw)

	# 객체 보내는 방법
	# get 검색 -> serializers로 json 타입으로 변경
	# qs = Member.objects.get(id=id,pw=pw)
	# json_qs = serializers.serialize('json',qs)
	# if qs:
	# 	context = {"member":json_qs,"result":'success'}
	# else:
	# 	context = {"result":"fail"}
	# return JsonResponse(context)

	# filter 검색
	# # qs를 리스트타입으로 변경 - 리스트타입 아니면 타입에러
	# qs = Member.objects.filter(id=id,pw=pw)
	# mlist = list(qs.values())
	qs = list(Member.objects.filter(id=id,pw=pw).values())
	if qs:
		context = {"member":qs,"result":'success'}
	else:
		context = {"result":"fail"}
	return JsonResponse(context)


	# # 변수 보내는 방법
	# qs = Member.objects.filter(id=id,pw=pw)
	# if qs:
	# 	context = {'id':qs[0].id,'nickname':qs[0].nickname,"result":'success'}
	# else:
	# 	context = {"result":"fail"}

	# return JsonResponse(context)