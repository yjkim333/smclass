stu_title = ['번호','이름','국어','영어','수학','과학','합계','평균']
stu_datas = [[1,'홍길동',100,100,100,99],[2,'유관순',70,70,100,99],[3,'이순신',80,60,100,99],[4,'김구',10,10,40,99],[5,'김유신',80,70,100,99]]

#append 로 합계 평균 추가해서 출력하시오
stu_datas[0].append(stu_datas[0][2]+stu_datas[0][3]+stu_datas[0][4]+stu_datas[0][5])
stu_datas[0].append((stu_datas[0][2]+stu_datas[0][3]+stu_datas[0][4]+stu_datas[0][5])/4)
print(stu_datas)
print("               [  학생성적 프로그램  ]")
for s_t in stu_title:
  print("{}".format(s_t),end='\t')
#print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(stu_title[0],stu_title[1],stu_title[2],stu_title[3],stu_title[4],stu_title[5],stu_title[6],stu_title[7]))
print()
print("ㅡ"*33)

for s in stu_datas:
  s.append(s[2]+s[3]+s[4]+s[5])
  s.append((s[2]+s[3]+s[4]+s[5])/4)
  print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{:.1f}".format(s[0],s[1],s[2],s[3],s[4],s[5],s[6],s[7]))

