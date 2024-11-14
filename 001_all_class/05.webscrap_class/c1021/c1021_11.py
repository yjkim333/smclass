import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com/index.htm"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

# soup 변환
soup = BeautifulSoup(res.text,"lxml")

# print(soup.find("div",{"class":"hot_issue"}))
# print(soup.find("li",{"class":"issue_list04"}).find("dl"))
# print(soup.find("div",{"class":"hot_issue"}).find("ul",{"class":"sub_list"}).find("li",{"class":"issue_list04"}))
title = soup.find("div",{"class":"hot_issue"}).find("ul",{"class":"sub_list"}).find("li",{"class":"issue_list04"}).dl.dt.a.next.next.text
