import keyword


# 주석

# 변수명 (자료형 안써도됨, 마침표; 안씀)
friend = 1
a = 10
myname = "정우성"
my_name = '유재석'
_myname = "이효리"
member01 = "강호동"

print(friend)
print(a)
print(myname)
print(my_name)
print(_myname)
print(member01)


''' 전체주석 '나 " 세개쓰기 (이건 다 안되는 예시)
friend$ = 1
a! = 10
@myName = '홍길동'
1abc = 10
def = 10
'''

# 파이썬 예약어 확인
# keyword는 위에 import해줘야 사용가능
print(keyword.kwlist)       # 예약어의 리스트
print(len(keyword.kwlist))  # len은 갯수 35

