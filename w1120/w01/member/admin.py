from django.contrib import admin
from member.models import Member

class MemberAdmin(admin.ModelAdmin):
	list_display = ['id','pw','name','nickname','cdate']

admin.site.register(Member,MemberAdmin)