import os
import requests
from bs4 import BeautifulSoup
import time

url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    'Accept-Language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료
soup = BeautifulSoup(res.text,"lxml")

# print(soup.prettify())

# 기준점
#contentarea > div.box_type_l > table
data = soup.select_one("#contentarea > div.box_type_l > table")
stocks = data.select("tr")
# print(len(stocks))  # 50개

### list 생성 ###
# print(stocks[0].select("th"))
# sts = stocks[0].select("th")
# st_list = []
# for st in sts:
# 	print(st.text)
# 	st_list.append(st.text)
# print(st_list)

### 1. 상단 타이틀
# 리스트내포
# sts = stocks[0].select("th")
st_list = [st.text for st in stocks[0].select("th")]
# print(st_list)
# print(len(sts))  # 상단 타이틀 항목 : 12개


### 2. 
# print(stocks[1].select("td"))		# 항목 : 1개
# print(len(stocks[2].select("td")))
# print(stocks[2].select("td"))		# 항목 : 12개
# 첫번째 줄
# sto_list = [sto.text.strip().replace("\t","").replace("\n","") for sto in stocks[2].select("td")]
# print(sto_list)

# csv로 30개 주식 정보 저장
import csv

with open("C:/workspace/smclass/c1023/stock.csv","w",encoding="utf-8-sig",newline="") as f:
	writer = csv.writer(f)
	writer.writerow(st_list)
	
	print(len(stocks))
	stocks_list = []
	for i in range(1,50):
		sto_list = []
		if len(stocks[i].select("td")) > 1:
			sto_list = [sto.text.strip().replace("\t","").replace("\n","") for sto in stocks[i].select("td")]
			stocks_list.append(sto_list)
			writer.writerow(sto_list)
	
print(stocks_list)
print("완료!")

