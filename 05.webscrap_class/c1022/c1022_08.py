import os
import requests
from bs4 import BeautifulSoup
url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=9&backgroundColor="
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    'Accept-Language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료
# print(res.text)
soup = BeautifulSoup(res.text,"lxml")
# print(soup.prettify())

# 제목,금액,평점,평가수,링크주소,이미지

data = soup.select_one("ul#productList")
lists = data.select("li")
# print(data.select_one("dd"))
# 금액 90만원이상, 평점 4.5 이상, 평가수 100명 이상
n_lists = []
for i in range(len(lists)):
	try:
		price = int(lists[i].select_one("strong.price-value").text.replace(",",""))
		rating = float(lists[i].select_one("em.rating").text)
		rating_count = int(lists[i].select_one("span.rating-total-count").text[1:-1])		# 문자열 슬라이싱
		if price >= 900000 and rating >= 4.5 and rating_count >= 100:
			n_list = []
			link = "http://www.coupang.com"+lists[i].select_one("a")['href']
			product = lists[i].select_one("div.name").text
			img = "http:"+lists[i].select_one("dt.image").select_one("img")['src']
			# print("링크주소 :",link)
			# print("제품명 :",product)
			# print("금액 :",price)
			# print("평점 :",rating)
			# print("평가수 :",rating_count)
			# print("이미지 :",img)
			# print("."*100)
			n_list = [product,price,rating,rating_count,link,img]
			n_lists.append(n_list)
	
	except Exception as e:
		print("에러 :",e)

# print(n_lists)

while True:
	print()
	print("1. 금액 순차정렬")
	print("2. 금액 역순정렬")
	print("3. 평점 순차정렬")
	print("4. 평점 역순정렬")
	print("0. 종료")
	print("ㅡ"*25)
	choice = input("원하는 번호 입력 >> ")

	if choice == '1':
		n_lists.sort(key=lambda x:x[1])
		print(n_lists)
	elif choice == '2':
		n_lists.sort(key=lambda x:x[1],reverse=True)
		print(n_lists)
	elif choice == '3':
		n_lists.sort(key=lambda x:x[2])
		print(n_lists)
	elif choice == '4':
		n_lists.sort(key=lambda x:x[2],reverse=True)
		print(n_lists)
	elif choice == '0':
		print("프로그램 종료")
		break







# print("링크주소 :","http://www.coupang.com"+lists[0].select_one("a")['href'])
# print("제품명 :",lists[0].select_one("div.name").text)
# price = int(lists[0].select_one("strong.price-value").text.replace(",",""))
# print("금액 :",price)
# rating = float(lists[0].select_one("em.rating").text)
# print("평점 :",rating)
# rating_count = int(lists[0].select_one("span.rating-total-count").text[1:-1])		# 문자열 슬라이싱
# print("평가수 :",rating_count)
# print("이미지 :","http:"+lists[0].select_one("dt.image").select_one("img")['src'])
