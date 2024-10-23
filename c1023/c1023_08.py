from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup
import random

# url = "http://naver.com"

# browser = webdriver.Chrome()
# browser.get(url)

# elem = browser.find_element(By.ID,"query")
# elem.send_keys("네이버 항공권")
# elem.send_keys(Keys.ENTER)

# # 네이버항공권 링크 클릭
# elem = browser.find_element(By.CLASS_NAME,"link_name").click()

# ----------------------------------------------------------------



# 1. '네이버항공권' 페이지 열기
url = "https://flight.naver.com/"
browser = webdriver.Chrome()
browser.maximize_window() # 창을 최대화 시킴
browser.get(url)

# 2. 출발지 클릭 # 출발지 입력 # 김포공항 선택
# //*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[1]
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[1]').click()
elem = browser.find_element(By.CLASS_NAME,"autocomplete_input__qbYlb").send_keys("김포")
time.sleep(0.5)
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/section/ul/li[2]/a/b').click()

# 3. 도착지 클릭 # 도착지 입력 # 제주 선택
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[2]').click()
elem = browser.find_element(By.CLASS_NAME,"autocomplete_input__qbYlb").send_keys("제주")
time.sleep(0.5)
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/section/ul/li/a/b').click()

# 4. 가는 날 클릭 # 가는 날 날짜 선택
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[2]/button[1]').click()
time.sleep(0.5)
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[4]/button').click()

# 5. 오는 날 클릭 # 오는 날 날짜 선택
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[2]/button[2]').click()
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[7]/button').click()

# 6. 인원 선택 # 성인 추가 + 버튼 클릭
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[3]/button').click()
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[4]/div/div/div[1]/div[1]/button[2]').click()

# 7. 항공권 검색 버튼 클릭
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/button[1]').click()
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/button[1]').click()

# 8. 데이터를 검색하는 동안 대기 상태
# # 검색 중 time.sleep
# time.sleep(10)

# # 8. 데이터를 검색하는 동안 대기 상태
# # 화면 대기 함수
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# # 화면 대기 
# # WebDriverWait(browser,30) -> 최대 30초 대기 
# # 화면에 찾으려고 하는 <html> 요소가 있는지 확인
# elem = WebDriverWait(browser,30).until(EC.presence_of_all_elements_located(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div[2]'))
elem = WebDriverWait(browser, 120).until(lambda x: x.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div[2]'))

# 화면 스크롤 내리기
# 현재 스크롤 높이 검색
prev_height = browser.execute_script("return document.body.scrollHeight")
print("최초 높이 :",prev_height)

	# 스크롤 내리기
while True:
	browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
	time.sleep(2)  # 다른 정보가 추가 될때까지 대기
	# 내린 후 높이 확인
	curr_height = browser.execute_script("return document.body.scrollHeight")

	if prev_height == curr_height:
		# 중지
		break
	
	prev_height = curr_height
	print("현재높이 :",curr_height)


# 데이터 가져와서 처리
# BeautifulSoup 데이터 처리
# 웹 스크래핑
soup = BeautifulSoup(browser.page_source,"lxml")

with open('flight.html','w',encoding='utf-8') as f:
	f.write(soup.prettify())

input("enter 키를 입력하면 프로그램이 종료됩니다.")
browser.quit()


time.sleep(100)

