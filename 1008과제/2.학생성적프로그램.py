students = []
chk = 0

while True:
  print()
  print("---[ 학생성적프로그램 ]---")
  print("ㅡ"*33)
  print("1 -> 학생성적입력")
  print("2 -> 학생성적출력")
  print("3 -> 학생성적수정")
  print("4 -> 학생성적검색")
  print("5 -> 학생성적삭제")
  print("6 -> 등수처리")
  print("7 -> 학생성적정렬")
  print("0 -> 프로그램 종료")
  print("ㅡ"*33)
  choice = int(input("실행하려는 항목 번호 입력>>"))
  if choice == 1:
    print("[  학생 성적 입력  ]")
    while True:
      print("메뉴로 이동 -> 0")
      print()
      stu = {}
      stu['no'] = len(students)+1
      stu['name'] = input(f"{stu['no']}번째 학생 이름 입력>")
      if stu['name'] == '0':
        break
      stu['kor'] = int(input("국어점수 입력>"))
      stu['eng'] = int(input("영어점수 입력>"))
      stu['math'] = int(input("수학점수 입력>"))
      stu['total'] = stu['kor'] + stu['eng'] + stu['math']
      stu['avg'] = stu['total']/3
      stu['rank'] = 0
      students.append(stu)
      print(stu['name'],"학생의 성적이 입력되었습니다.")

  elif choice == 2:
    print("[  학생 성적 출력  ]")
    if students == []:
      print("입력된 학생 성적이 없습니다.")
    else:
      print("번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수")
      print("ㅡ"*33)
      for i in students:
        print(f"{i['no']}\t{i['name']}\t{i['kor']}\t{i['eng']}\t{i['math']}\t{i['total']}\t{i['avg']:.2f}\t{i['rank']}")
      print()

  elif choice == 3:
    print("[  학생 성적 수정  ]")
    while True:
      print("메뉴로 이동 -> 0")
      search = input("수정할 학생 이름>>")
      if search == '0':
        break
      for i in students:
        if i['name'] == search:
          print(i['name'],"학생의 성적입니다.")
          print()
          print("번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수")
          print("ㅡ"*33)
          print(f"{i['no']}\t{i['name']}\t{i['kor']}\t{i['eng']}\t{i['math']}\t{i['total']}\t{i['avg']:.2f}\t{i['rank']}")
          print()
          print("-"*55)
          print("1 -> 국어 성적 수정")
          print("2 -> 영어 성적 수정")
          print("3 -> 수학 성적 수정")
          print("0 -> 성적 수정 취소")
          print("-"*55)
          choice = int(input("실행하려는 항목 번호 입력>>"))
          if choice == 1:
            print("[  국어 성적 수정  ]")
            print("현재 점수 :",i['kor'])
            i['kor'] = int(input("변경할 점수>>"))
          elif choice == 2:
            print("[  영어 성적 수정  ]")
            print("현재 점수 :",i['eng'])
            i['eng'] = int(input("변경할 점수>>"))
          elif choice == 3:
            print("[  수학 성적 수정  ]")
            print("현재 점수 :",i['math'])
            i['math'] = int(input("변경할 점수>>"))
          elif choice == 0:
            print(search,"학생의 성적수정을 취소합니다.")
            chk = 1
            break
          i['total'] = i['kor'] + i['eng'] + i['math']
          i['avg'] = i['total']/3
          print(i['name'],"학생 성적이 수정되었습니다.")
          print()
          chk = 1
      if chk == 0:
        print("검색 결과가 없습니다.")
        print()

  elif choice == 4:
    print("[  학생 성적 검색  ]")
    while True:
      print("메뉴로 이동 -> 0")
      search = input("검색할 학생 이름>>")
      if search == '0':
        break
      for i in students:
        if i['name'] == search:
          print(i['name'],"학생의 성적입니다.")
          print()
          print("번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수")
          print("ㅡ"*33)
          print(f"{i['no']}\t{i['name']}\t{i['kor']}\t{i['eng']}\t{i['math']}\t{i['total']}\t{i['avg']:.2f}\t{i['rank']}")
          print()
          chk = 1
      if chk == 0:
        print("검색 결과가 없습니다.")
        print()

  elif choice == 5:
    print("[  학생 성적 삭제  ]")
    while True:
      print("메뉴로 이동 -> 0")
      search = input("삭제할 학생 이름>>")
      if search == '0':
        break
      for i in students:
        if i['name'] == search:
          print()
          chk = 1
          print(search,"학생을 찾았습니다.")
          print("1. 성적을 삭제할래요(복구불가)\n2. 삭제 안할래요.")
          choice = int(input("실행하려는 항목 번호 입력>>"))
          if choice == 1:
            students.remove(i)
            print(search,"학생의 성적이 삭제되었습니다.")
          elif choice == 2:
            print(search,"학생의 성적의 삭제가 최소되었습니다.")
            break
          print()
      if chk == 0:
        print("검색 결과가 없습니다.")
        print()

  elif choice == 6:
    print("[  등수 처리  ]")
    for i in students:
      count = 1
      for j in students:
        if i['avg'] < j['avg']:
          count += 1
      i['rank'] = count
    print("학생의 등수처리를 완료했습니다.")
    print()

  elif choice == 7:
    print("[  학생 성적 정렬  ]")
    print("-"*55)
    print("1 -> 이름 순차정렬")
    print("2 -> 이름 역순정렬")
    print("3 -> 총점 순차정렬")
    print("4 -> 총점 역순정렬")
    print("5 -> 번호 순차정렬")
    print("0 -> 메뉴로 이동")
    print("-"*55)
    choice = int(input("실행하려는 항목 번호 입력>>"))
    if choice == 1:
      students.sort(key=lambda x:x['name'])
      print("이름으로 순차정렬되었습니다.")
    elif choice == 2:
      students.sort(key=lambda x:x['name'],reverse=True)
      print("이름으로 역순정렬되었습니다.")
    elif choice == 3:
      students.sort(key=lambda x:x['total'])
      print("총점으로 순차정렬되었습니다.")
    elif choice == 4:
      students.sort(key=lambda x:x['total'],reverse=True)
      print("총점으로 역순정렬되었습니다.")
    elif choice == 5:
      students.sort(key=lambda x:x['no'])
      print("번호로 순차정렬되었습니다.")
    elif choice == 0:
      print("메뉴로 이동합니다.")
      break

  elif choice == 0:
    print("[  프로그램 종료  ]")
    print("---프로그램을 종료합니다.---")
    break

