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

url = "https://new.land.naver.com/complexes?ms=37.4594312,126.8931808,17&a=APT:PRE:ABYG:JGC&e=RETAIL"

# browser = webdriver.Chrome()
# browser.maximize_window()
# browser.get(url)

# time.sleep(0.5)
# pyautogui.moveTo(1270,560)
# time.sleep(2)
# pyautogui.moveTo(1270,500)
# time.sleep(2)
# pyautogui.click()
# pyautogui.moveTo(100,750)
# time.sleep(1)

# prev_height = browser.execute_script("return articleListArea.scrollHeight")
# print("화면 높이 :",prev_height)

# while True:
# 	# browser.execute_script("window.scroll(0,articleListArea.scrollHeight)")
# 	pyautogui.scroll(-prev_height)
# 	time.sleep(2)
# 	curr_height = browser.execute_script("return articleListArea.scrollHeight")
# 	if prev_height == curr_height:
# 		break
# 	prev_height = curr_height
# 	print("높이 :",prev_height)

# soup = BeautifulSoup(browser.page_source,'lxml')
# data = soup.select_one("#complexOverviewList > div.list_contents > div.item_area > div")
# with open("c1024/naver.html","w",encoding="utf-8") as f:
# 	f.write(soup.prettify())


# print()
# all_height = browser.execute_script("return document.body.scrollHeight")
# print("화면 전체 높이 :",all_height)


# 매매, 전세 중 매매 가격이 낮은 5개 전세 가격이 낮은 5개 출력하시오.
with open("c1024/naver.html","r",encoding="utf-8") as f:
	soup = BeautifulSoup(f)
data = soup.select_one("#articleListArea")


def num_chg(p):
	b = p.split('억')
	f_num = int(b[0])*1000000000
	if b[1].strip() != '':
		s_num = int(b[1].strip().replace(",",""))*10000
	else:
		s_num = 0
	price = f_num+s_num
	return price

def spec_chg(spec):
	spec_a = spec.split(",")
	spec_b = spec_a[0].split("/")
	spec_c = int(spec_b[1][:-2])
	return spec_c


lists = data.select("div.item")
m_list = []
j_list = []
print(len(lists))
for i,list in enumerate(lists):
	type = list.select_one("span.type").text.strip()
	if type == "월세":
		continue
	name = list.select_one("div.item_title").text.strip()
	p = list.select_one("span.price").text
	
	# spec 분리 함수 생성 호출
	s = list.select_one("span.spec").text.strip()		# 116B/84m², 중/35층, 남향
	spec = spec_chg(s)
	price = num_chg(p)
	# p = list.select_one("span.price").text.strip().replace("억","00000000").replace(" ","+")
	# p = p.split("+")
	# # print(p)
	# if len(p)>1:
	# 	fn = int(p[0])
	# 	sn = int(p[1].strip().replace(",",""))
	# 	price = fn+sn
	# else:
	# 	for i in p:
	# 		price = int(i)
	if type == "매매":
		print(i+1)
		print("아파트명 :",name)
		print("유형 :",type)
		print("가격 :",price)
		print("평형 :",spec)
		print("ㅡ"*50)
		m = [name,type,price,spec]
		m_list.append(m)
	elif type == "전세":
		print(i+1)
		print("아파트명 :",name)
		print("유형 :",type)
		print("가격 :",price)
		print("평형 :",spec)
		print("ㅡ"*50)
		j = [name,type,price,spec]
		j_list.append(j)



while True:
	print()
	print("1. 매매가 낮은 5개")
	print("2. 전세가 낮은 5개")
	print("3. 84타입 매매가 낮은 5개")
	choice = input("원하는 번호 >> ")
	if choice == '1':
		print()
		m_list.sort(key=lambda x:x[2])
		print(m_list[:5])
	elif choice == '2':
		print()
		j_list.sort(key=lambda x:x[2])
		print(j_list[:5])
	elif choice == '3':
		print()
		m_type_84 = [x for x in m_list if x[3] == 84]
		m_type_84.sort(key=lambda x:x[2])
		print(m_type_84[:5])
	elif choice == '0':
		break
		
		

# input("엔터")
