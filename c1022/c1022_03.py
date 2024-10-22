import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료

soup = BeautifulSoup(res.text,"lxml")

data = soup.select_one("div.aside_popular")
print("---",data.select_one("h3>span").text,"---")
pops = data.select("tbody>tr")
# print(len(pops))
sum = 0

for i,pop in enumerate(pops):
	print(pop.select_one("th").text)
	print(pop.select_one("td").text,"원")
	print(pop.select_one("td").find_next_sibling("td").em.text,end="  ")
	print(pop.select_one("td").find_next_sibling("td").select_one("span.tah").text.strip())
	print()
	sps = pop.select_one("td").find_next_sibling("td").select("span")
	for sp in sps:
		print(sp.text.strip(),end='\t')
	print()
	print()
	s = int(pop.select_one("td").text.replace(",",""))
	sum += s
	# print(pop.select_one(":nth-child(3)>em").text)
	# print(pop.select_one(":nth-child(3)>span").text)
print("합계 :",sum)