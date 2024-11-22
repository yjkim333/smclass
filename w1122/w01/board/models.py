from django.db import models


class Board(models.Model):
	# 번호
	bno = models.AutoField(primary_key=True)

	id = models.CharField(max_length=100)
	# member = models.ForeignKey(Member, on_delete=models.DO_NOTHING, null=True)

	# 게시글 제목
	btitle = models.CharField(max_length=1000)
	# 게시글 내용
	bcontent = models.TextField()

	# 답글 기능 있을 때 답글리스트 그룹핑
	bgroup = models.IntegerField(null=True)

	# 답글 기능 있을 때 답글리스트 순서
	bstep = models.IntegerField(default=0)

	# 답글 기능 있을 때 답글 제목 들여쓰기
	bindent = models.IntegerField(default=0)

	bhit = models.IntegerField(default=0)
	bdate = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.bno},{self.id},{self.btitle},{self.bdate}"