from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from bs4 import BeautifulSoup
import time
import random
import csv

# for i in range(4):
# 	url = f"https://search.daum.net/search?w=tot&q=202{i}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
# 	headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
# 	res = requests.get(url,headers=headers)
# 	res.raise_for_status() # 에러시 종료


# 	soup = BeautifulSoup(res.text,"lxml")

# 	# 브라우저 열기
# 	browser = webdriver.Chrome()
# 	# url 입력
# 	browser.get(url)
# 	soup = BeautifulSoup(browser.page_source,"lxml")

# 	# 데이터 html파일로 저장
# 	with open(f"d1106/daum_movie{i+1}.html","w",encoding="utf-8") as f:
# 		f.write(soup.prettify())





###--------------------------------------------------------------
# 데이터 파일 불러오기 -> beautifulsoup parsing
with open('d1106/movie.csv',"a",encoding="utf-8-sig",newline="") as f:
	writer = csv.writer(f)
	m_title = ['이미지링크','영화제목','누적관객수','개봉일']
	writer.writerow(m_title)
for i in range(4):
	with open(f"d1106/daum_movie{i+1}.html","r",encoding="utf-8") as f:
		soup = BeautifulSoup(f,'lxml')

	data = soup.select_one('#mor_history_id_0')
	# print(data)

	m_lists = data.select('ul.c-list-basic>li')
	# print(ms)
	print(len(m_lists))
	movies = []
	for i,list in enumerate(m_lists):
		m = []
		link = list.select_one('img')['src'].strip()
		title = list.select_one('strong.tit-g').text.strip()
		counts = list.select_one('p.conts-desc>a').text.strip().replace(",","").replace("명","").replace("만","").split(" ")
		count = int(counts[1])*10000
		date = list.select_one('span.conts-subdesc').text.strip()
		print("이미지링크 :",link)
		print("영화제목 :",title)
		print("누적관객 :",count)
		print("개봉일 :",date)
		print()
		m = [link,title,count,date]
		with open('d1106/movie.csv',"a",encoding="utf-8-sig",newline="") as f:
			writer = csv.writer(f)
			writer.writerow(m)
		movies.append(m)
		if i>=9:
			break

		print(movies)


		

	print("파일 저장")