# 리스트
# in - 데이터가 있는지 없는지 확인
# count() - 데이터 갯수
# find() - 데이터가 있는 위치 -> 없으면 -1     => find(검색어,시작위치,끝위치)로 쓸 수 있다.
# index() - 데이터가 있는 위치 -> 없으면 에러

fruit = "사과,배,딸기,포도,복숭아,배,사과,배,딸기"
# 배가 있는 위치를 모두 출력하시오.
# print(fruit.find('배'))

search = input("과일 이름 입력")
print("모든 글자 : ",fruit)
idx = 0
if fruit.count(search)>0:
  print(f"{search} 글자가 있습니다.")
  for i in range(fruit.count(search)):
      print(search,"글자가 있는 위치 : ",fruit.find(search,idx)) # find(찾을 문자, 시작index, 끝index)
      idx = fruit.find(search,idx)+1
else:
  print(search," (이)라는 글자는 없습니다.")


# idx = 0
# if fruit.count('배')>0:
#   for i in range(fruit.count('배')):
#     for i in range(idx,len(fruit)):
#       print(fruit.find('배'))
#       idx = fruit.find('배')+1
#       break
# else:
#   print("배라는 글자는 없습니다.")


# # ## count -> 문자열에서 갯수 확인
# fruit = "사과,배,딸기,포도,복숭아,배,사과,배,딸기"
# # print(fruit.count("사과"))
# # print(fruit.count("포도"))

# # 과일이름을 입력받아 있으면 있다, 개수가 몇개있다, 없으면 없다
# search = input("과일 검색")
# if search in fruit:
#   print(search,"가 있습니다. 개수 : ",fruit.count(search))
#   print(fruit.find(search))    # find() -> search가 있는 위치의 index를 알려줌 - 없어도 에러 안남
#   # print(fruit.index(search)) # index() -> search가 있는 위치의 index를 알려줌
# else:
#   print(search,"가 없습니다.")
#   print(fruit.find(search))   # find() -> search가 있는 위치의 index를 알려줌  => 없으면 -1 리턴
#   #print(fruit.index(search)) # index() -> search가 있는 위치의 index를 알려줌 => 없으면 에러


# ## count -> 리스트에서 갯수 확인
# fruit = ['사과','배','딸기','포도','복숭아','배','사과','배','딸기']
# print (fruit.count('배'))
# print (fruit.count('사과'))


# fruit = ['사과','배','딸기','포도','복숭아']
# #글을 입력받아 입력한 과일이 있으면 있어요. 없어요 출력
# name = input("과일 이름 입력")
# if name in fruit:
#   print(name," 있어요")
# else:
#   print(name," 없어요")


# fruit = "사과,배,딸기,포도"  #문자열은 index같이 됨
# if '배' in fruit:
#   print("배라는 글자가 있어요")
# else:
#   print("배라는 글자가 없어요")


# fruit = ['사과','배','딸기','포도','배']
# if '배' in fruit: # 1번의 비교로 있는지 없는지 확인
#   print("배가 있어요.")
# else:
#   print("배가 없어요.")