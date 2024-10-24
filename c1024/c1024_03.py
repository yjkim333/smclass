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

# #------------------------------------------
# # selenium 화면을 숨김처리
# options = Options()
# options.add_argument("--headless")
# options.add_argument("--window-size=1920,1080")  # 디스플레이설정-화면해상도
# options.add_argument("User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36")
# #------------------------------------------

# url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
# browser = webdriver.Chrome(options=options)
# browser.maximize_window()
# browser.get(url)

# soup = BeautifulSoup(browser.page_source,'lxml')
# data = soup.select_one("div#detected_value").text
# print(data)

# # 숨긴처리된 화면을 캡쳐
# browser.get_screenshot_as_file("gmarket.png")

# input("엔터키 입력 - 종료 >>")


# for i in range(3):
# 	url = f"https://www.gmarket.co.kr/n/search?keyword=%EB%85%B8%ED%8A%B8%EB%B6%81&k=61&p={i+1}"
# 	browser = webdriver.Chrome()
# 	browser.get(url)
# 	time.sleep(3)
# 	soup = BeautifulSoup(browser.page_source,'lxml')
# 	with open(f"c1024/gmark{i+1}.html","w",encoding='utf-8') as f:
# 		f.write(soup.prettify())


# 만족도 95이상, 금액 1500000 이하, 평가수 100이상

with open("c1024/gmark1.html","r",encoding='utf-8') as f:
	soup = BeautifulSoup(f,'lxml')

data = soup.select_one("div#region__content-body")
# print(data)
lists = data.select("div.box__item-container")
for i,list in enumerate(lists):
	try:
		if price <= 1500000 and rating >=95 and num >= 100:
			name = list.select_one("span.text__item").text.strip()
			price = int(list.select_one("strong.text.text__value").text.strip().replace(",",""))
			rating = int(list.select_one("div.box__seller-awards").text.strip()[4:6])
			num = int(list.select_one("li.list-item.list-item__feedback-count>span.text").text.strip().replace(" ","").replace("\n","")[1:3])
			print("상품명 :",name)
			print("가격 :",price)
			print("만족도 :",rating)
			print("평가수 :",num)
			print("ㅡ"*50)
	except Exception as e:
		print(e)
		print("*"*50)