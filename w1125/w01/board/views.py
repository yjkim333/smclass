from django.shortcuts import render,redirect
from board.models import Board
from member.models import Member
from django.db.models import F
from datetime import datetime


# 게시판 리스트
def blist(request):
	qs = Board.objects.all().order_by('-bgroup','bstep')
	context = {'blist':qs}

	return render(request, 'blist.html', context)



# 게시글 쓰기 페이지 열기, 글쓰기 저장
def bwrite(request):
	if request.method == 'GET':
		return render(request, 'bwrite.html')
	else:
		# session_id 의 id 값을 가져옴
		id = request.session.get('session_id')
		member = Member.objects.get(id=id)
		btitle = request.POST.get('btitle')
		bcontent = request.POST.get('bcontent')
		bfile = request.FILES.get('bfile','')
		print("파일이름 :",request.FILES)
		print("파일이름2 :",bfile)

		# bno - 자동입력
		# id - Member에서 가져옴
		# btitle,bcontent,
		# bgroup,bstep,bindent,bhit,bdate - 자동 입력

		# DB 저장 - bgroup -> bno AutoField 자동 번호생성
		qs = Board.objects.create(member=member,btitle=btitle,bcontent=bcontent,bfile=bfile)
		qs.bgroup = qs.bno
		qs.save()

		context = {"wmsg":"1"}

		return render(request, 'bwrite.html', context)
	


# 글 상세보기 페이지 - 조회수 증가&중복증가방지, 이전글&다음글
def bview(request,bno):

	### 조회수 증가

	## 1) get() 형태 => qs.save()
	# qs = Board.objects.get(bno=bno)
	# qs.bhit += 1
	# qs.save()
	# context = {'board':qs}

	### 쿠키사용기간 - 1일 동안 유지
	# 11월25일 23시59분0초 로 세팅
	tomorrow = datetime.replace(datetime.now(),hour=23,minute=59,second=0)
	# 쿠키설정포맷 - strftime - 시간포맷형태
	expires = datetime.strftime(tomorrow,"%a,%d-%b-%Y %H:%M:%S GMT")


	## 2) filter() 형태 => update() 명령어 사용
	qs = Board.objects.filter(bno=bno)

	context = {'board':qs[0]}

### 이전글 다음글
	# 이전 글
	prev_qs = Board.objects.filter().order_by('-bgroup','bstep').first()
	# 다음 글
	next_qs = Board.objects.filter().order_by('bgroup','-bstep').first()

# -----------------------

	response = render(request, 'bview.html', context)

	print("cookie_name :",request.COOKIES.get('cookie_name'))
	### 새로고침 조회수 증가 방지
	# 조회수 증가하면, cookie_name에 증가한 게시글의 번호를 추가하여 반복 증가 방지
	# cookie_name 이 존재하면 게시글 조회한 적 있음
	if request.COOKIES.get('cookie_name') is not None:
		# 쿠키를 읽어와서 안에 bno가 1|3|4 저장이면-> 2번 게시글을 조회할 땐 조회수 카운트 / 3번 조회시 조회수 증가 안됨.
		cookies = request.COOKIES.get('cookie_name')
		cookies_list = cookies.split("|")
		# 쿠키에 번호가 없으면 번호 추가
		if str(bno) not in cookies_list:
			print("cookie_name 있지만, 번호가 없으면")
			# |1|3|4 -2번글 조회시-> |1|3|4|2
			response.set_cookie('cookie_name', cookies+f'|{bno}', expires=expires)
			qs.update(bhit = F('bhit')+1)
			
	else:  # cookie_name 이 존재하지 않으면 지금까진 게시글 조회한 적이 없음
		# set_cookie('cookie_name', bno, 쿠키사용기간)
		print("cookie_name 없으면")
		response.set_cookie('cookie_name', bno, expires=expires)
		# F함수 - field 값 참조  -  from django.db.models import F
		qs.update(bhit = F('bhit')+1)

	return response



# 게시글 삭제
def bdelete(request,bno):
	qs = Board.objects.get(bno=bno)
	qs.delete()
	context = {'dmsg':bno}
	return render(request, 'blist.html', context)



# 게시글 수정페이지, 수정저장
def bupdate(request,bno):
	if request.method == 'GET':
		qs = Board.objects.get(bno=bno)
		context = {'board':qs}
		return render(request, 'bupdate.html', context)
	else:
		bno = request.POST.get('bno')
		btitle = request.POST.get('btitle')
		bcontent = request.POST.get('bcontent')

		qs = Board.objects.get(bno=bno)
		qs.btitle = btitle
		qs.bcontent = bcontent
		qs.save()
		return redirect('board:bview', bno)
	


# 답글달기
def breply(request,bno):
	if request.method == 'GET':
		qs = Board.objects.get(bno=bno)
		context = {'board':qs}
		return render(request, 'breply.html', context)
	else:
		id = request.POST.get('id')
		member = Member.objects.get(id=id)
		bgroup = int(request.POST.get('bgroup'))			# 답글들 그룹핑
		bstep = int(request.POST.get('bstep'))				# 답글들의 순서
		bindent = int(request.POST.get('bindent'))		# 답글 들여쓰기
		btitle = request.POST.get('btitle')
		bcontent = request.POST.get('bcontent')

		# 같은 bgroup에서 bstep이 더 큰 것만 검색해서 bstep 1씩 증가
		qs = Board.objects.filter(bgroup=bgroup,bstep__gt=bstep)		# bstep__gt=~ - ~보다 큰것
		qs.update(bstep = F('bstep')+1)

		qs = Board(member=member,btitle=btitle,bcontent=bcontent,bgroup=bgroup,bstep=bstep+1,bindent=bindent+1)
		qs.save()

		context = {'rmsg':'1'}
		return render(request, 'breply.html', context)
