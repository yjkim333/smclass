from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup
import random

url = "http://www.naver.com"

# 크롬브라우저 열기
browser = webdriver.Chrome()
# 네이버 페이지 이동
browser.get(url)
# 로그인버튼 선택
elem = browser.find_element(By.CLASS_NAME,"MyView-module__link_login___HpHMW")
# 로그인버튼 클릭
elem.click()
time.sleep(random.randint(1,3))

# 자바스크립트 호출방법
id = "dydwns4671"
pw = "!@3"
input_js = 'document.getElementById("id").value = "{id}"; document.getElementById("pw").value = "{pw}";'.format(id = "dydwns4671",pw = "!@3")
browser.execute_script(input_js)
time.sleep(random.randint(2,5))

# 로그인버튼 클릭
elem = browser.find_element(By.CLASS_NAME,"btn_login")
elem.click()


elem = browser.find_element(By.ID,"new.dontsave")
elem.click()




time.sleep(100)

# -----------------------------------------------------------------
# # ID 값을 입력
# elem = browser.find_element(By.ID,"id")
# elem.send_keys("dydwns4671")
# time.sleep(random.randint(2,4))
# # PW 값을 입력
# elem = browser.find_element(By.ID,"pw")
# elem.send_keys("!@3")
# time.sleep(random.randint(2,4))

# # 로그인버튼 클릭
# elem = browser.find_element(By.CLASS_NAME,"btn_login")
# elem.click()




