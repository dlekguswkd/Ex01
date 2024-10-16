# 연습문제 [문제 ifelse02.py]
# 과목번호를 입력받아 강의실 번호를 출력하는 프로그램을 작성하세요

# 과목 code값이
# 1이면 “R101호 입니다.”
# 2이면 “R202호 입니다.”
# 3이면 “R303호 입니다.”
# 4이면 “R404호 입니다.”
# 나머지는 “상담원에게 문의하세요” 를 출력하세요

# if문 조건문
# num = input("과목번호를 입력하세요. \n")
# int_num = int(num)

# if int_num == 1:
#     print("R101호 입니다.")
# elif int_num == 2:
#     print("R202호 입니다.")
# elif int_num == 3:
#     print("R303호 입니다.")
# elif int_num == 4:
#     print("R404호 입니다.")
# else :
#     print("상담원에게 문의하세요")


#  스위치문
code = int(input("과목번호를 입력해 주세요. \n"))

# break가 생략되어있는거임 그래서 없는건 구현할수없음
match code:
    case 1:
        print("R101호")
    case 2:
        print("R202호")
    case 3:
        print("R303호")
    case 4:
        print("R404호")
    case _:
        print("상담원")