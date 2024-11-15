# django framework flow
# client -request-> URLConf(project의 urls.py) -> View(views.py) -> Model -> DB
# 																						 -> Templates(html) 

# urls, views, templates, ... 분리하는 이유 => 보안에 유리



#### template language
# Template태그 - {%문법%} -ex- {%for문%}{%endfor%} / {%if문%}{%endif%}
# {%csrf_token%} - CSRF 공격방지를 위한 태그 / 장고 내부적으로 CSRF 토큰값의 유효성 검증 -> 데이터 저장할때 안넣으면 저장이 안됨
# Template변수 - {{변수}}
# Template필터 - {{변수|옵션}}