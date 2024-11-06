from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pyautogui
import time
import requests
from bs4 import BeautifulSoup
import random
import csv
# email 발송 관련 import
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


url = "https://news.naver.com/main/ranking/popularDay.naver"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

data = soup.select_one("div.rankingnews_box")

# 파일저장
with open("c1025/news.txt","w",encoding="utf-8") as f:

	# 언론사
	press = data.select_one("#wrap > div.rankingnews._popularWelBase._persist > div.rankingnews_box_wrap._popularRanking > div > div:nth-child(1) > a > strong").text
	print("언론사 :",press)

	f.write(press+'\n')

	# 뉴스리스트
	newsLists = data.select("div.rankingnews_box")

	titlelists = data.select("ul.rankingnews_list > li")
	news = []
	for titlelist in titlelists:
		n = []
		# 번호
		idx = titlelist.select_one("em.list_ranking_num").text
		print(idx,".")
		# 기사제목
		title = titlelist.select_one("div.list_content > a").text
		print(title)
		print("ㅡ"*100)
		n = [idx,title]
		f.write(",".join(n)+'\n')
		news.append(n)
		
smtpName = "smtp.naver.com"
smtpPort = 587

sendEmail = "dydwns4671@naver.com"
pw = "5C1DVPPTFD3G"
recvEmail = "dydwns4671@naver.com"

title = "네이버 뉴스"
content = "네이버 뉴스 - 언론사 랭크 기사내용 첨부"

msg = MIMEMultipart()
msg['Subject'] = title
msg['From'] = sendEmail
msg['To'] = recvEmail
msg.attach(MIMEText(content))

# 파일첨부
with open("c1025/news.txt","rb") as f:
	attachment = MIMEApplication(f.read())
	attachment.add_header('Content-Disposition','attachment',filename = "news.txt")
	msg.attach(attachment)

s = smtplib.SMTP(smtpName,smtpPort)
s.starttls()
s.login(sendEmail,pw)
s.sendmail(sendEmail,recvEmail,msg.as_string())
print("msg :",msg.as_string())
s.quit()

print("메일이 발송되었습니다.")
			
	



# oracle18
# sql디벨로퍼 다운
# c://orasql 복사

# 윈도우r
# cmd
# sqlplus

