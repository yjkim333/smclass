# import time
# import random
# # a = [0]*100
# # for i in range(100):
# # 	a[i] = i
# # print(a)


# # b = [i for i in range(100)]
# # # print(b)
# # for i in b:
# # 	print(i)
# # 	time.sleep(1)

# # print(random.uniform(1,3))

# b = [i for i in range(100)]
# # print(b)
# for i in b:
# 	print(i)
# 	time.sleep(random.uniform(1,3))


## 다음 사이트 검색으로 주식 정보 입력해서 페이지 이동을 하시오
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get("https://daum.net")

elem = browser.find_element(By.ID,"q")
# elem.click()
elem.send_keys("주식정보")
elem.send_keys(Keys.ENTER)

browser.get("https://naver.com")
elem = browser.find_element(By.CLASS_NAME,"search_input")
elem.send_keys("삼성전자 주식")
elem.send_keys(Keys.ENTER)

time.sleep(100)





