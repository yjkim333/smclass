from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup
import random

# 다음 아이디, 패스워드 로그인

url = "http://www.daum.net"

browser = webdriver.Chrome()
browser.get(url)

elem = browser.find_element(By.CLASS_NAME,"btn_login")
elem.click()
time.sleep(random.randint(2,4))

# 자바스크립트 호출
id = "dydwns4671@hanmail.net"
pw = "!@3"
input_js = f'document.getElementById("loginId--1").value = "{id}"; document.getElementById("password--2").value = "{pw}";'
browser.execute_script(input_js)
time.sleep(random.randint(2,4))

elem = browser.find_element(By.CLASS_NAME,"btn_g.highlight.submit")
elem.click()



time.sleep(100)