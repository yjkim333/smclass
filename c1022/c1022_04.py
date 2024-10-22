import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료

soup = BeautifulSoup(res.text,"lxml")

data = soup.select_one("div.box_type_l")
titles = data.select_one("tr.type1").select("th")
for title in titles:
	print(title.text,end="\t")
print()

conts = data.select_one("table").select("tr>td")

# print(len(conts))
for cont in conts:
	print(cont.text.strip(),end="\t")

# print(conts)
# for cont in range()