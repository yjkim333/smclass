import os
import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com/chart/index.htm"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료

soup = BeautifulSoup(res.text,"lxml")


data = soup.select_one("table")

lists = data.select("tr")  # len(lists) - 101개

# list[0] : 상단 타이틀
title = []
tits = lists[0].select("th")
for tit in tits:
	title.append(tit.text.strip())
	# print(tit.text.strip())

# 1~100위 리스트 출력
for i in range(1,101):
	# 폴더가 존재하지 않을 때
	if not os.path.exists("C:/workspace/smclass/c1022/melon"):
		os.makedirs("C:/workspace/smclass/c1022/melon")
	
	with open(f"C:/workspace/smclass/c1022/melon/{i}.jpg","wb") as f:
		lis = lists[i].select("td")   # len(lis) - 12개
		print("순위 :",lis[1].select_one("span").text)
		print("이미지 :",lis[3].select_one("img")['src'])
		img = requests.get(lis[3].select_one("img")['src'])
		f.write(img.content)
		songs = lis[5].select("div.ellipsis")
		print("곡 정보 :",songs[0].select_one("a").text,end=" ")
		singers = songs[1].select("a")
		if len(singers) != 4:
			print(singers[0].text)
		else:
			print(singers[0].text," ",singers[1].text)
		print("."*60)
		# for song in songs:
		# 	print("곡정보 :",song.select_one("a").text)