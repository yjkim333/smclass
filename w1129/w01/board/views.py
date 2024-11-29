from django.shortcuts import render
from board.models import Board
from comment.models import Comment
from member.models import Member


# 게시판 리스트
def blist(request):
	qs = Board.objects.all().order_by("-bgroup",'bstep')
	context = {'blist':qs}
	return render(request, 'blist.html', context)


# 게시글 보기
def bview(request,bno):
	qs = Board.objects.filter(bno=bno)
	c_qs = Comment.objects.filter(board=qs[0]).order_by('-cno')
	print("확인 : ",c_qs,c_qs.count)
	context = {'board':qs[0],"clist":c_qs}
	return render(request, 'bview.html', context)
