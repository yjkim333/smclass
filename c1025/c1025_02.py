from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import time
import random
import pyautogui	
import csv


# 무선마우스
# 상품명, 가격, 평점, 평가수, 찜수 정보를 1-5페이지까지 가져와서
# 평점 4.8이상, 평가수 1000개 이상 인 상품을 csv 파일로 저장하고 출력
# browser = webdriver.Chrome()
# for i in range(1,6):
# 	url = f"https://search.shopping.naver.com/search/all?adQuery=%EB%AC%B4%EC%84%A0%EB%A7%88%EC%9A%B0%EC%8A%A4&origQuery=%EB%AC%B4%EC%84%A0%EB%A7%88%EC%9A%B0%EC%8A%A4&pagingIndex={i}&pagingSize=40&productSet=total&query=%EB%AC%B4%EC%84%A0%EB%A7%88%EC%9A%B0%EC%8A%A4&sort=rel&timestamp=&viewType=list"
# 	browser.get(url)
# 	time.sleep(2)
# 	soup = BeautifulSoup(browser.page_source,'lxml')
	
# 	prev_height = browser.execute_script('return document.body.scrollHeight')
# 	while True:
# 		browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# 		time.sleep(1)
# 		curr_height = browser.execute_script('return document.body.scrollHeight')
# 		if prev_height == curr_height:
# 			break
# 		prev_height = curr_height

# 	with open(f"c1025/navershop{i}.html","w",encoding='utf-8') as f:
# 		f.write(soup.prettify())

with open(f"c1025/navershop1.html","r",encoding='utf-8') as f:
	soup = BeautifulSoup(f,'lxml')

data = soup.select_one("div.basicList_list_basis__uNBZx>div")
lists1 = data.select("div.adProduct_item__1zC9h")
lists2 = data.select("div.product_item__MDtDF")
# pros = data.select("div.adProduct_item__1zC9h")+data.select("div.product_item__MDtDF")
# print(len(pros))
# cl = pros[0]['class']
# # print(cl[0])

# for i,pro in enumerate(pros):
# 	if pro['class'] == 'adProduct_item__1zC9h':
# 		print(i+1)
# 		name = pro.select_one("div.adProduct_title__amInq").strip()
# 		print(name)
# 		# print('adProduct_item__1zC9h')
# 	else:
# 		print(i+1)
# 		name = pro.select_one("div.product_title__Mmw2K>a").text.strip()
# 		print(name)
# 		print('product_item__MDtDF')


for list in lists1:
	name = list.select_one("div.adProduct_title__amInq").text.strip()
	price = int(list.select_one("span.price_num__S2p_v>em").text.strip().replace(",",""))
	rating = float(list.select_one("span.adProduct_rating__PaMzh").text.strip())
	rating_count = int(list.select_one("em.adProduct_count__EDNPm").text.strip().replace(",",""))
	heart = int(list.select_one("span.adProduct_num__t7R1x").text.strip())
	print("상품명 :",name)
	print("가격 :",price)
	print("평점 :",rating)
	print("평가수 :",rating_count)
	print("찜수 :",heart)
	print("ㅡ"*80)

# for i,list in enumerate(lists2):
# 	try:
# 		name = list.select_one("div.product_title__Mmw2K").text.strip().replace(" ","").replace("\n","")
# 		price = int(list.select_one("span.price_num__S2p_v>em").text.strip().replace(",",""))
# 		rating = float(list.select_one("span.product_grade__IzyU3").text.strip().replace("\n","").replace(",","")[2:])
# 		rating_count = (list.select_one("em.product_num__fafe5").text.strip().replace(",",""))
# 		heart = (list.select_one("span.product_num__fafe5").text.strip())
# 		print("상품명 :",name)
# 		print("가격 :",price)
# 		print("평점 :",rating)
# 		print("평가수 :",rating_count)
# 		print("찜수 :",heart)
# 		print("ㅡ"*80)
# 	except Exception as e:
# 		pass



