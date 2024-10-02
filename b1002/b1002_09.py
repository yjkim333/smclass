fruit = "사과,배,딸기,포도,복숭아,배,사과,배,딸기"
fruits = fruit.split(",")
# print(fruits)
# print(len(fruits))
# 리스트인 경우 검색해서 해당되는 index를 출력하시오.
# 배에 해당되는 인덱스 번호 출력
search = input("과일이름 입력")

for idx,i in enumerate(fruits):
  if i == search:
    print(search," 위치 : ",idx)


# print(fruit.find('배',0))
# print(fruit.find('배',fruit.find('배',0)+1))

# print(fruit.find('딸기',0))
# print(fruit.find('딸기',6))
# print(fruit.find('딸기')+1)