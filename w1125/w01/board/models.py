from django.db import models
from member.models import Member


class Board(models.Model):
	bno = models.AutoField(primary_key=True)
	# id = models.CharField(max_length=100)
	member = models.ForeignKey(Member,on_delete=models.DO_NOTHING, null=True)
	# on_delete 
	# models.DO_NOTHING - 아무 행동 하지 않음
	# models.CASCADE - 부모 삭제 시 외래키 포함 행 함께 삭제
	# models.SET_NULL - 부모 삭제 시 외래키 값을 null로 변경 , null=True 일때

	btitle = models.CharField(max_length=1000)
	# TextField = oracle - clob
	bcontent = models.TextField()
	
	# 계층형 게시판용
	bgroup = models.IntegerField(null=True)
	bstep = models.IntegerField(default=0)
	bindent = models.IntegerField(default=0)
	bhit = models.IntegerField(default=0)
	bdate = models.DateTimeField(auto_now=True)

	# img 파일 업로드
	bfile = models.ImageField(null=True, upload_to='board')
	# bimg = models.FileField(null=True)


	def __str__(self):
		return f"{self.bno},{self.btitle},{self.bgroup},{self.bdate}"
