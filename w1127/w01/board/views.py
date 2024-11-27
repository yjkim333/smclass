from django.shortcuts import render
from member.models import Member
from board.models import Board
from datetime import datetime
from django.db.models import F

# 게시판 리스트
def blist(request):
	qs = Board.objects.all().order_by('-bgroup','bstep')
	context = {'blist':qs}
	return render(request, 'blist.html', context)


# 게시글 쓰기페이지, 저장
def bwrite(request):
	if request.method == 'GET':
		return render(request, 'bwrite.html')
	else:
		id = request.session.get('session_id')
		member = Member.objects.get(id=id)
		btitle = request.POST.get('btitle')
		bcontent = request.POST.get('bcontent')
		bfile = request.FILES.get('bfile','')

		# DB저장
		qs = Board.objects.create(member=member,btitle=btitle,bcontent=bcontent,bfile=bfile)
		qs.bgroup = qs.bno
		qs.save()
		context = {"wmsg":"1"}
		return render(request, 'blist.html', context)
	

# 게시글 상세보기
def bview(request,bno):
	qs = Board.objects.get(bno=bno)
	context = {"board":qs}
	day1 = datetime.replace(datetime.now,)
	# 조회수 1증가
	qs.bhit +=  1
	qs.save()

	return render(request, 'bview.html', context)


# 게시글 수정
def bupdate(request,bno):
	if request.method == 'GET':
		qs = Board.objects.filter(bno=bno)
		context = {"board":qs[0]}
		return render(request, 'bupdate.html', context)
	else:
		bno = request.POST.get('bno')
		btitle = request.POST.get('btitle')
		bcontent = request.POST.get('bcontent')
		bfile = request.FILES.get('bfile','')

		# DB저장
		qs = Board.objects.get(bno=bno)
		qs.btitle = btitle
		qs.bcontent = bcontent
		if bfile:
			qs.bfile=bfile
		qs.save()
		context = {"umsg":bno}
		return render(request, 'bupdate.html', context)