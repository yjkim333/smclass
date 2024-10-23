# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
# import requests
# from bs4 import BeautifulSoup
# import random
# # 1. 네이버항공권 페이지 열기
# url = "https://flight.naver.com/"
# browser = webdriver.Chrome()
# browser.maximize_window() # 창 최대화
# browser.get(url)

# # # 8. 데이터를 검색하는 동안 대기 상태
# # # 화면 대기 함수
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # # 화면 대기 
# # # WebDriverWait(browser,30) -> 최대 30초 대기 
# # # 화면에 찾으려고 하는 <html> 요소가 있는지 확인
# # elem = WebDriverWait(browser,30).until(EC.presence_of_all_elements_located(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div[2]'))
# elem = WebDriverWait(browser, 120).until(lambda x: x.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div[2]'))

# # 화면 스크롤 내리기
# # 현재 스크롤 높이(길이) 검색
# prev_height = browser.execute_script("return document.body.scrollHeight")
# print("최초 높이 :",prev_height)

# while True:
# 	# 스크롤 내리기
# 	browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# 	time.sleep(2)  # 다른 정보가 추가 될때까지 대기
# 	# 내린 후 높이 확인
# 	curr_height = browser.execute_script("return document.body.scrollHeight")

# 	if prev_height == curr_height:
# 		# 중지
# 		break
	
# 	prev_height = curr_height
# 	print("현재높이 :",curr_height)


















# flight.html 에서 금액이 50000원 미만 항공권을 출력하시오
# 김포-제주 50000원 이하 항공권 개수 : 16개
# 제주-김포 50000원 이하 항공권 개수 : 30개

import requests
from bs4 import BeautifulSoup

with open("flight.html","r",encoding='utf-8') as f:
	soup = BeautifulSoup(f,'lxml')

g_data = soup.select("div.domestic_results__gp5WB>div")
print("항공사 :",g_data[1].select_one("span.airline_text__WWkbY").text.strip())
print("가격 :",g_data[1].select_one("i.domestic_num__ShOub").text.strip())
print("*"*30)
