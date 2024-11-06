# a = "안녕하세요. 반갑습니다. 파이썬 수업입니다."
# search = "파이썬"
# print(a.find(search))
# print(a[a.find(search):a.find(search)+3])


import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/main/ranking/popularDay.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

# print(soup.find("div",{"class":"rankingnews_box"}))
# print(len(soup.findAll("div",{"class":"rankingnews_box"})))


# print(soup.find("div",{"class":"rankingnews_box_wrap _popularRanking"}))
# # find() - 1개 검색
# rankingnews_wrap = soup.find("div",{"class":"rankingnews_box_wrap _popularRanking"})
# # find_all() - 여러개 검색
# rankingnews_boxs = rankingnews_wrap.find_all("div",{"class":"rankingnews_box"})
# print(len(rankingnews_boxs))

# print(rankingnews_boxs.find("strong",{"class":"rankingnews_name"}))

print(soup.title)						# 제일 먼저 찾아지는 것을 출력
print(soup.find("title"))		# 특정 위치의 태그와 속성을 가지고를 출력
print(soup.find("div",{"class":"rankingnews_box_wrap"}))
soup.find("div",{"class":"rankingnews_box_wrap"}).find_all("div",{"class":"rankingnews_box"})
newsLists = soup.find("div",{"class":"rankingnews_box_wrap"}).find_all("div",{"class":"rankingnews_box"})
print("여러개 개수 확인 :",len(newsLists))

for newsList in newsLists:
	print(newsList.find("strong",{"class":"rankingnews_name"}).text)