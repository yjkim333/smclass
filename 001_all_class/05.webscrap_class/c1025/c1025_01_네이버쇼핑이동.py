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

# naver.com 에서 검색창 네이버 쇼핑 입력-엔터
# 네이버쇼핑 클릭
# 네이버 쇼핑 검색창에서 무선마우스 입력-엔터
url = "https://naver.com"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

# 네이버 검색창 네이버 쇼핑 검색
elem = browser.find_element(By.XPATH,'//*[@id="query"]')
elem.click()
elem.send_keys("무선마우스")
time.sleep(2)
pyautogui.moveTo(800,200)
pyautogui.doubleClick()
pyautogui.keyDown("ctrl")
pyautogui.keyDown("x")
pyautogui.keyUp("ctrl")
pyautogui.keyUp("x")
time.sleep(2)
elem.send_keys("네이버 쇼핑")
elem.send_keys(Keys.ENTER)

# 네이버 검색내용 네이버 쇼핑 클릭
time.sleep(1)
pyautogui.click(442,712)
time.sleep(1)
# browser.switch_to.window(browser.window_handles[1])
pyautogui.click(492,207)
pyautogui.keyDown("ctrl")
pyautogui.keyDown("v")
pyautogui.keyUp("ctrl")
pyautogui.keyUp("v")
time.sleep(1)
pyautogui.click(800,207)





#--------------------------------------------------------
# # 1.
# # 네이버 쇼핑 검색창 입력 enter키 입력
# url = "https://www.naver.com/"
# browser = webdriver.Chrome()
# browser.maximize_window()
# browser.get(url)
# elem = browser.find_element(By.ID,"query")
# # 네이버 쇼핑 클릭
# elem = browser.find_element(By.XPATH,'//*[@id="main_pack"]/section[1]/div/div/div[1]/div/div[2]/a')
# elem.click()
# time.sleep(2)
# # 네이버 쇼핑에서 무선 마우스 검색창 입력 enter키 입력
# # 새로운 탭으로 이동
# browser.switch_to.window(browser.window_handles[1])
# elem = browser.find_element(By.XPATH,'//*[@id="gnb-gnb"]/div[2]/div/div[2]/div/div[2]/form/div[1]')
# elem.send_keys("무선 마우스")
# elem.send_keys(Keys.ENTER)
# input("enter키 입력완료")
#--------------------------------------------------------










input("엔터")






