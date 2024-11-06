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
import pyautogui			# terminal -> pip install pyautogui 설치 => 마우스 컨트롤

url = "https://www.yanolja.com/search/%EA%B0%95%EB%A6%89%ED%98%B8%ED%85%94?pageKey=1729747971796"

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

pyautogui.moveTo(960,540)
time.sleep(1)
pyautogui.moveTo(50,100)
time.sleep(1)
pyautogui.moveTo(50,700)
time.sleep(1)
pyautogui.moveTo(1500,300)
time.sleep(1)
pyautogui.moveTo(1500,800)
time.sleep(1)
pyautogui.moveTo(900,600)
time.sleep(1)
pre_height = browser.execute_script("return document.body.scrollHeight")
while True:
	pyautogui.scroll(-pre_height)
	time.sleep(2)

	curr_height = browser.execute_script("return document.body.scrollHeight")
	if pre_height == curr_height: break
	pre_height = curr_height

print("스크롤 내리기 완료")

# 마우스를 옮겨 클릭
pyautogui.moveTo(900,900)
pyautogui.click()



input("엔터키 -> 종료")
