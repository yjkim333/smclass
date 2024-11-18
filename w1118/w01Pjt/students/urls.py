from django.urls import path,include
from . import views

app_name = 'students'  # <- name 으로 url 연결 시 사용
urlpatterns = [
    # urls 추가
    path('write/',views.write,name='write'),  # 학생입력페이지
    
    # 학생리스트
    path('list/',views.list,name='list'),  # 학생리스트페이지
	
    # 학생상세
    path('<str:name>/view/',views.view,name='view'),  # 학생상세정보페이지
    
    # 수정 - 1,2,3
    path('<str:name>/modify/',views.modify,name='modify'),  # 학생수정페이지1 - url
    path('modify2/',views.modify2,name='modify2'),  # 학생수정페이지2 - 파라미터
    path('<str:name>/modify3/',views.modify3,name='modify3'),  # 학생수정페이지3 - appName
    
    path('<str:name>/delete/',views.delete,name='delete'),  # 학생삭제페이지
		

    # path('doWrite/',views.doWrite,name='doWrite'),  # urls 추가
]
