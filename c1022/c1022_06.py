import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com/chart/index.htm"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료

soup = BeautifulSoup(res.text,"lxml")

# print(soup.prettify())

f = open("C:\workspace\smclass\c1022\melon.text","w",encoding='utf-8')

# 순위, 이미지링크주소, 제목, 가수명
title = ['순위','사진링크주소','제목','가수']
for t in title:
	print(t,end='\t')
print()
# 파일저장
t = ",".join(title)+'\n'
f.write(t)

# tit = soup.select_one("table > thead")
# titles = tit.select("th")
# for i,title in enumerate(titles):
# 	if i == 0:
# 		continue
# 	elif i == 2:
# 		continue
# 	else:
# 		print(title.text.strip(),end='\t')
# print()

data = soup.select_one("table > tbody")
songs = data.select("tr")
for idx,song in enumerate(songs):
	print(song.select_one("span").text,end='')
	print(song.select_one("span").next.next.text,end='\t')
	print(song.select_one("img")["src"],end='\t')
	print(song.select_one("div.rank01").text.strip(),end='\t')
	print(song.select_one("div.rank02").next.next.text.strip())

	# print(song.text.strip(),end='\t')



#frm > div > table > tbody
















# title = ['순위', '종목명', '검색비율', '현재가', '전일비', '등락률', '거래량', '시가', '고가', '저가', 'PER', 'ROE']

# a = ','.join(title)+"\n"
# print(a)

# with open("C:\workspace\smclass\c1022\ a.text","w",encoding="utf-8") as f:
# 	f.write(a)


# b = '안녕,반가워,고마워,사랑해'
# b_list = b.split(",")
# print(b_list)