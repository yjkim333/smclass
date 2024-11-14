from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from bs4 import BeautifulSoup
import time
import random

# url = "https://www.yanolja.com/"

# # 브라우저 열기
# browser = webdriver.Chrome()
# # 창 최대화
# browser.maximize_window()
# # url 입력
# browser.get(url)

# # 검색창 클릭
# browser.find_element(By.XPATH,'//*[@id="__next"]/div/div/header/section/a[2]').click()
# # 날짜 선택		# 입실날짜 선택		# 퇴실날짜 선택 	# 확인 버튼 클릭
# browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div/div[1]/form/div/div[2]/div[1]/button').click()
# time.sleep(0.5)
# browser.find_element(By.XPATH,'/html/body/div[4]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[3]/td[2]').click()
# browser.find_element(By.XPATH,'/html/body/div[4]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[3]/td[4]').click()
# browser.find_element(By.XPATH,'/html/body/div[4]/div/div/section/section[4]/button').click()
# # 검색창 클릭 	# 검색어 입력 	# enter 키 입력
# elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div/div[1]/form/div/div[1]/div/input')
# elem.click()
# elem.send_keys("강릉 호텔")
# elem.send_keys(Keys.ENTER)

# # 자동시 로딩 대기
# # 화면의 호텔 검색 내용이 뜰 때까지 대기, 최대 30초까지 대기
# WebDriverWait(browser,30).until(lambda x:x.find_element(By.XPATH,'//*[@id="__next"]/div/main/section/div[2]'))

# # 화면을 스크롤 해서 내리기 반복
# # execute_script() -> 자바스크립트 실행 함수
# prev_height = browser.execute_script("return document.body.scrollHeight")
# while True:
# 	browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# 	time.sleep(1)
# 	# 페이지가 로딩되면서 길어진 길이를 다시 가져옴
# 	curr_height = browser.execute_script("return document.body.scrollHeight")
# 	# 페이지를 스크롤해서 길이가 더 길어졌는지 확인
# 	if prev_height == curr_height:
# 		break
# 	# 스크롤 길이가 더 길어지면 이전길이에 현재 길이를 입력시킴
# 	prev_height = curr_height

# print("스크롤 내리기 완료")

# soup = BeautifulSoup(browser.page_source,"lxml")
# # 데이터 html파일로 저장
# with open("c1024/yanolja.html","w",encoding="utf-8") as f:
# 	f.write(soup.prettify())

# 데이터 파일 불러오기 -> beautifulsoup parsing
with open("c1024/yanolja.html","r",encoding="utf-8") as f:
	soup = BeautifulSoup(f,'lxml')

# 평점 4.8이상, 금액 17만원 이하 검색해서 출력
# 1. 호텔명: , 평점: , 금액: , --------  2. 호텔명:.....

data = soup.select_one("div.PlaceListBody_listContainer__2qFG1")
# print(data)
h_lists = data.select("div.PlaceListItemText_container__fUIgA")
print(len(h_lists))
s_lists = []
e_lists = []
for i,list in enumerate(h_lists):
	s = []
	e = []
	try:
		name = list.select_one("div.PlaceListTitle_container__qe7XH").text.strip()
		rating = float(list.select_one("span.PlaceListScore_rating__3Glxf").text.strip())
		price = int(list.select_one("span.PlacePriceInfoV2_discountPrice__1PuwK").text.strip().replace(",",""))
		if rating >= 4.8 and price <= 170000:
			print(i+1)
			print("호텔명 :",name)
			print("평점 :",rating)
			print("금액 :",price)
			print("*"*50)
			s = [i+1,name,rating,price]
			s_lists.append(s)
		else:
			print(i+1,"조건에 맞지 않음")
			print("*"*50)

	except Exception as e:
		print(i+1)
		print("예외 :",e)
		print("*"*50)
		e = [i+1,e]
		e_lists.append(e)
print(s_lists)
while True:
	print("="*50)
	print(" [ 검색 결과 ] ")
	print("1. 조건에 맞는 검색 개수")
	print("2. 조건에 맞지 않는 검색 개수")
	print("3. 예외 처리 개수")
	print("4. 조건 중 최고 금액")
	print("5. 조건 중 최고 평점")
	print("0. 종료")
	choice = input("원하는 번호 입력 >> ")
	if choice == '1':
		print("조건에 맞는 검색 개수 :",len(s_lists))
	elif choice == '2':
		print("조건에 맞지 않는 검색 개수 :",len(h_lists)-len(s_lists)-len(e_lists))
	elif choice == '3':
		print("예외 처리 개수 :",len(e_lists))
	elif choice == '4':
		s_lists.sort(key=lambda x:x[3],reverse=True)
		print(s_lists[0])
	elif choice == '5':
		s_lists.sort(key=lambda x:x[2],reverse=True)
		print(s_lists[0])
	elif choice == '0':
		break







# input("enter 키를 누르면 종료됩니다>>")