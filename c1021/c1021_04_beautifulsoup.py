import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/main/ranking/popularDay.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

with open("C:/workspace/smclass/c1021/1.html","w",encoding="utf-8") as f:
	f.write(res.text)


# html, css 정보를 가진 소스로 변경
# res.text -> str => html,css
soup = BeautifulSoup(res.text,"lxml")  # str -> html태그,css태그가 사용될 수 있는 형태로 변경

# BeautifulSoup 사용
# 태그 출력, 태그 안의 글자 출력
print(soup.title)    					# title 태그 출력
print(soup.title.get_text())	# title 태그 문자열을 출력
print(soup.title.text)				# title 태그 문자열을 출력

print("없는 태그 :",soup.titletitletitle)  					# 없는 태그 입력 시 None
# print("없는 태그 :",soup.titletitle.get_text())		# -> 없는 태그 입력 시 에러
# print("없는 태그 :",soup.titletitle.text)					# -> 에러

print(soup.a)							# 첫번째 a태그 가져옴
print(soup.a.next)				# next -> 다음 태그를 가져옴
print(soup.a.next.text)		# next의 문자열을 출력

# 태그 속성 출력
print(soup.a.attrs)				# 태그의 속성값 가져옴 -> 딕셔너리 형태
print(soup.a["href"])			# a태그의 href 속성 값을 가져옴.

# 특정 정보를 출력
# print(soup.find("div",attrs={"id":"header"}))
print(soup.find("div",{"id":"header"}))										# div 태그 중에 id = "header"
print(soup.find("h2",{"class":"rankingnews_tit"}))				# h2 태그 중에 class = rankingnews_tit
print(soup.find("h2",{"class":"rankingnews_tit"}).text)		# h2 태그 중에 class = rankingnews_tit 의 텍스트
print("ㅡ"*50)

print(soup.find_all("div"))					# 모든 div 태그 검색
print(len(soup.find_all("div")))		# 모든 div 태그 갯수 검색
print(len(soup.findAll("div")))			# 모든 div 태그 갯수 검색
print(type(soup.findAll("div")))		# <class 'bs4.element.ResultSet'> -> 객체의 리스트


# soup.prettify() 정보 저장
# with open("C:/workspace/smclass/c1021/2.html","w",encoding="utf-8") as f:
# 	# soup.prettify() -> 소스가 정리되어 저장됨.
# 	f.write(soup.prettify())

print()
print("완료")

# print(res.text)