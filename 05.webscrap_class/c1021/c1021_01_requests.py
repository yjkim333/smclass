# 웹스크래핑
# 1. request 라이브러리설치
# 1) pip install requests - 터미널에 입력설치   - 윕정보 요청하는 라이브러리
# 2) pip install beautifulsoup4 - thml,xml파일에서 원하는 데이터를 손쉽게 parsing 할 수 있는 python 라이브러리
# 3) pip install lxml - css문법으로 특정요소를 쉽게 가져올 수 있는 python 라이브러리
# 2. extensions 에서 open in browser 설치

# 웹 크롤링 - 웹크롤러가 일정 규칙에 따라 복수개의 웹페이지를 브라우징 하는 것
# 웹 스크랩핑 - 웹사이트 상에서 원하는 정보를 추출하여 수집하는 기술


### 웹스크래핑 세팅 ###
import requests
# res = requests.get("http://www.google.com/")  # html 소스를 가져옴.
res = requests.get("http://www.naver.com/")  # html 소스를 가져옴.
# res = requests.get("http://www.melon.com/index.htm")  # html 소스를 가져옴.
res.raise_for_status()  # 에러시 종료
# if res.status_code == 200:
# 	print(res.text)
# else:
# 	print("접근할 수 없음.")
print("응답코드 :",res.status_code)   # html 응답코드 
print(res.text) # html 소스코드 출력

# requests로 정보를 가져올 시
# 제이쿼리,자바스크립트,외부페이지,react,vue...등의 비동기식으로 작동되는 소스의 정보는 못 가져옴 -> selenium으로 해야됨.


### 웹소스코드 파일 저장
# f = open("a.html","w",encoding="utf-8")
# f.write(res.text)
# f.close()

# f.close() 안해도 됨.
with open("C:/workspace/smclass/c1021/naver.html","w",encoding="utf-8") as f:
	f.write(res.text)


###
print("총 문자 길이 :",len(res.text))