import requests
from bs4 import BeautifulSoup

url = "https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&xfrom=main^gnb#pageNum%%9"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

# soup 변환
soup = BeautifulSoup(res.text,"lxml")
# print(soup.prettify)
# print(soup.find("div",{"id":"bestPrdList"}).find("h3").text)
# print(soup.find("div",{"id":"bestPrdList"}).h3.text)
# print(soup.find("li",{"id":"rnkTab1"}).text)

# print(soup.find("div",{"id":"bestPrdList"}).find("div",{"class":"pname"}).p.text)
print(soup.find("div",{"id":"bestPrdList"}).find("strong",{"class":"sale_price"}).text)
plists = soup.find("div",{"id":"bestPrdList"}).find("ul",{"class":"cfix"}).find_all("li")
for i,p in enumerate(plists):
	print(f"{i+1}위 - {p.find("div",{"class":"pname"}).p.text}",end='\t')
	print(f" 가격 : {p.find("strong",{"class":"sale_price"}).text} 원")