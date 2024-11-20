from django.shortcuts import render
from member.models import Member


def m2(request):
	if request.method == 'GET':
		Id = request.COOKIES.get('Id','')
		Mo = request.COOKIES.get('Mo','')
		Op = request.COOKIES.get('Op','')
		context = {'Id':Id,'Mo':Mo,'Op':Op}
		return render(request,'m2.html',context)
	
	else:
		response = render(request,'index.html')

		memberId = request.POST.get('memberId')
		money = request.POST.get('money')
		option = request.POST.get('option')
		saveProduct = request.POST.get('saveMember')

		if saveProduct is not None:
			response.set_cookie('Id',memberId,max_age=60*60)
			response.set_cookie('Mo',money,max_age=60*60)
			response.set_cookie('Op',option,max_age=60*60)

		else:
			response.delete_cookie('Id')
			response.delete_cookie('Mo')
			response.delete_cookie('Op')
		
		return response



def product(request):
	if request.method == 'GET':
		saveP = request.COOKIES.get('saveP','')
		saveN = request.COOKIES.get('saveN','')
		context = {'saveP':saveP,'saveN':saveN}
		return render(request,'product.html',context)
	
	else:
		response = render(request,'index.html')

		pId = request.POST.get('pId')
		pName = request.POST.get('pName')
		saveProduct = request.POST.get('saveProduct')
		print(pId,pName,saveProduct)

		if saveProduct is not None:
			response.set_cookie('saveP',pId,max_age=60*60)
			response.set_cookie('saveN',pName,max_age=60*60)
		else:
			response.delete_cookie('saveP')
			response.delete_cookie('saveN')

		return response





def login2(request):

	if request.method == 'GET':
		cookId = request.COOKIES.get('cookId','')
		print("cookId :",cookId)
		context = {'cookId':cookId}
		return render(request,'login2.html',context)
	

	else:
		response = render(request,'index.html')

		# 로그인 버튼 클릭 시 넘어오는 3 개 정보
		id = request.POST.get('id')
		pw = request.POST.get('pw')
		saveId = request.POST.get('saveId')

		if saveId is not None:
			response.set_cookie('cookId',id,max_age=60*60)

		else: response.delete_cookie('cookId')
		


		return response












# 로그인 페이지
def login(request):

	if request.method == "GET":
		## 쿠키정보 검색 - request.COOKIES.get('쿠키이름')
		## 쿠키 저장 - response.set_cookie('key','value')
		## 쿠키 삭제 - response.delete_cookie('key')


		# 모든 request에는 쿠키가 있음
		print("쿠키 정보 :",request.COOKIES)
		# 쿠키정보 검색
		print("cookinfo 정보",request.COOKIES.get('cookinfo'))
		
		saveId = request.COOKIES.get('saveId','')
		print("saveId :",saveId)
		context = {'saveID':saveId}
		
		response = render(request,'login.html',context)
		# 쿠키 설정(저장)
		if not request.COOKIES.get('cookinfo'):
			response.set_cookie('cookinfo','1111',max_age=60*60)
		# max_age = 60초*60 => 1시간 / max_age가 없으면 브라우저 종료시 삭제
		# 60*60*24*30 = 1달

		return response
	
	else:
		print("쿠키정보 :",request.COOKIES)
		id = request.POST.get('id')
		pw = request.POST.get('pw')
		saveID = request.POST.get('saveId')		# saveId 가 없으면(None) -> '' 으로 리턴
		# saveID = request.POST.get('saveId',"")		# saveId 가 없으면(None) -> '' 으로 리턴
		# saveID = request.POST['saveId']		# saveId 가 없으면 에러
		print("전달받은 정보 :",id,pw,saveID)
		response = render(request,'login.html')
		
		## 아이디 기억하기 
		if saveID is not None: # 아이디 기억하기 체크가 있으면 쿠키 저장
			response.set_cookie('saveId',id,max_age=60*60)
		else: # 아이디 기억하기 체크가 없으면 삭제
			response.delete_cookie('saveId')

		return response




# 회원리스트 페이지
def mlist(request):
	qs = Member.objects.all()
	context = {'mlist':qs}
	return render(request,'mlist.html',context)