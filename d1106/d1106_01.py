### 데이터 분석 ###
# 라이브러리 설치
# pandas - 데이터분석 - 문자/수치 가능
# pip install pandas

# numpy - 데이터분석 - 수치만 가능
# 

# matplotlib - 데이터시각화
# pip install matplotlib

# 엑셀파일(xlsx,xls)열기
# pip install xlrd
# pip install openpyxl

#-----------------------------------------

import pandas as pd
# pandas
# 1차원 - Series
# 2차원 - DataFrame

# Series
# 1차원 (정수,실수,문자열 등)
temp = pd.Series([-20,-10,10,20])
print(temp)

print(temp[0])
print(temp[1])
print(temp[3])

temp = pd.Series([-20,-10,10,20],index=['jan','feb','mar','apr'])
print(temp)
print(temp['jan'])
print(temp['feb'])
print(temp['mar'])
#-----------------------------------------


# a = [-20,-10,10,20]
# print(a)



#create new jupiter notebook

# 저장

# python:select interpreter