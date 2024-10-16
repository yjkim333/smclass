import os

# os.path.exists() -> 현재 폴더가 존재하는지 확인
# os.mkdir() -> 현재 폴더만 생성
# os.makedirs() -> 현재 폴더, 하위폴더까지 생성

# 폴더가 없을 시 폴더 생성
if not os.path.exists("c:/bbb"):
	# print("폴더 없음")
	os.mkdir("c:/bbb") # 폴더 생성
	# os.makedirs("c:/ccc/bbb") # 폴더 생성
# else:
	# print("폴더 있음")

f = open("c:/bbb/c.txt","w",encoding="utf-8")
f.write("안녕하세요")
f.close()