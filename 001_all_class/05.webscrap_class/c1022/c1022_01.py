import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/main/ranking/popularDay.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료


# print(res.text)  # 타입 : str

soup = BeautifulSoup(res.text,"lxml")

# html, css가 파싱이 되어 이쁘게 출력
# print(soup.prettify())

### 태그를 활용한 검색방법
# find, find_all, <=> select_one, select

# print(soup.find("h2",{"class":"rankingnews_tit"}))

# print(soup.select_one("h2.rankingnews_tit").text)
# print(soup.select_one("div#header"))



# print(soup.select_one("div.rankingnews_box"))
# data = soup.select_one("div.rankingnews_box_wrap")
# print(data)
# title = soup.select_one("div.rankingnews_box")
# print(f"언론사 : {title.select_one("strong.rankingnews_name").text}")
# newsLists = title.select_one("ul.rankingnews_list").select("li")
# # print(titles)
# for i,list in enumerate(newsLists):
# 	print(f"{i+1} : {list.select_one("a").text}")

titles = soup.select("div.rankingnews_box")

for i,title in enumerate(titles):
	print(f"{i+1}:{title.select_one("strong.rankingnews_name").text}")
newsLists = titles.select_one("ul.rankingnews_list").select("li")
for idx,list in enumerate(newsLists):
	print(f"{idx+1} : {list.select_one("a").text}")

