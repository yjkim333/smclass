# Selenium - 동적 웹 페이지 가져오기 가능 - 느림
# requests - 웹페이지(html) 읽어오기 - 빠름
# seleninum , requests => Beautifulsoup으로 원하는 데이터 추출(웹스크래핑)
# *설치*
# 1. pip install selenium 설치
# 2. 크롬브라우저 드라이버 설치

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup

# webdriver.Chrome(드라이버주소/chromedriver.exe)
# root에 파일이 저장되어 있으면 주소 입력하지 않아도 됨.
browser = webdriver.Chrome()
# 이동하려는 주소입력
browser.get("https://naver.com")

# html 위치 찾기 - requests의 select 
elem = browser.find_element(By.CLASS_NAME,"MyView-module__link_login___HpHMW")
# 클릭
elem.click()				# 클릭
browser.back()			# 뒤로가기
browser.forward()		# 앞으로 가기
browser.refresh()		# 새로고침
elem = browser.find_element(By.NAME,"pw")

elem = browser.find_element(By.ID,"query")

# 글자입력
elem.send_keys("네이버 영화")
# enter 키 입력
elem.send_keys(Keys.ENTER)

# 탭 이동
browser.switch_to.window(browser.window_handles[1])

time.sleep(100)  # 지연 100초