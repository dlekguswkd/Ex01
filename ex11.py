# 대소문자 관련 메소드

s = "i like Python"

print(s.upper())        # 대문자로 변환
print(s.lower())        # 소문자로 변환
print(s.swapcase())     # 대문자는 소문자로 소문자는 대문자로
print(s.capitalize())   # 문자열의 첫글자만 대문자로
print(s.title())        # 단어의 첫글자만 대문자로
print(s)                # 원본은 그대로 변하지않음


print("-------------------------")


# 검색 관련 메소드  (대소문자 구별함)
s = "I Like Python. I Like Java Also"

print(s.count('Like'))      # 2: 'Like' 가 몇개?   -> 갯수를 알려주는

print(s.find('Like'))       # 2: 첫번째 'Like' 의 시작 index번호    ->  몇번째 글자인지
print(s.find('Like', 5))    # 17: index번호가 5 이후에 처음 나타나는 'Like' index번호   ->  몇번째 글자인지
print(s.find('JS'))         # -1: 첫번째 'JS' 의 시작 index번호 없으면 -1  -> 결과없음 있을땐 양수로 표현
print(s.rfind('a'))         # 25: 오른쪽부터 첫번째 'a'의 index번호  -> 뒤에서 시작 r(오른쪽)
#print(s.lfind('Like'))     # lfind() 함수는 없음 주의  -> 이건 그냥 find

print("-------------------------")

#find() index() 비교
print(s.index('Like'))      #2 : 첫번째 'Like' 의 시작 index번호
#print(s.index('JS'))       #에러 : 첫번째 'JS' 의 시작 index번호,없으면 에러남         -> 사용시 조심해야함
print(s.rindex('Like'))     #17 : 오른쪽부터 첫번째 'like'의 index번호,없으면 에러남    -> 사용시 조심해야함

print("-------------------------")

# 결과가 true false
print(s.startswith('I Like'))       #true : 'I Like' 로 시작하면 true 아니면 false
print(s.startswith('Like', 2))      #true : 'Like' 가 index번호 2번에서 시작하면 true 아니면 false
print(s.endswith('Also'))           #true : 'Also' 로 끝나면 true 아니면 false
print(s.endswith('Java', 0, 24))    #false : index번호가 0부터 24번 사이에 'Java' 로 끝나면 true 아니면 false


print("-------------------------")

#편집 
# strip 은 양쪽만 없애주는거임
s = "   spam and ham   "
print("ㅣ"+s+"ㅣ")
print("ㅣ"+s.strip()+"ㅣ")        # 양쪽의 공백 삭제
print("ㅣ"+s.rstrip()+"ㅣ")       # 오른쪽 공백 삭제
print("ㅣ"+s.lstrip()+"ㅣ")       # 왼쪽 공백 삭제
print(s)                # 원본은 바뀌지않음

s = "<><abc><><defg><><>"
print(s.strip("<"))             #><abc><><defg><><> :양쪽끝의 '<'를 삭제 합니다.
print(s.strip(">"))             #<><abc><><defg><>< :양쪽끝의 '>'를 삭제 합니다.
print(s.strip("<>"))            # 양쪽에 < 랑 > 를 그냥 다 없애버림 
print(s.strip("<>a"))           # bc><><defg


#치환   (대소문자 구별)
s = "Hello Java Java java"
print(s.replace("Java", "Python"))      #Hello Python Python java #Java ---> Python 자바를 파이썬으로


#정렬
s = "king and queen"
print("ㅣ"+s.center(60)+"ㅣ")            #60칸에서 가운데
print(s.center(60, "-"))                 #60칸에서 가운데 공백은 '-'기로로 채우기
print(s.ljust(60, "-"))                  #60칸에서 왼쪽 공백은 '-'기로로 채우기
print(s.rjust(60, "-"))                  #60칸에서 오른쪽 공백은 '-'기로로 채우기

print("-------------------------")

# 판별
s01 = "1234"
s02 = "abcd"
s03 = "ABCD"

print(s01.isdigit())            #True: 문자열이 숫자이면 True 아니면 False  숫자로 바꿀수있는가?
print(s02.isdigit())            #False

print(s01.isalpha())            #False
print(s02.isalpha())            #True: 문자열이 알파벳이면 True 아니면 False, 한글? 글자로 바꿀수있는가?
print("-------------------------")
print("abcd".islower())         #True: 문자열이 소문자이면 True 아니면 False     다 소문자니?   한글은 false
print(s02.islower()) 
print(s03.isupper())            #True: 문자열이 대문자이면 True 아니면 False      다 대문자니?  한글은 false

print("-------------------------")
print("\n\n".isspace())         #True: 문자열이 공백이면 True 아니면 False      줄바꿈을 공백으로 보냐
print(" ".isspace())            #True: 문자열이 공백이면 True 아니면 False      공백을 공백으로 보냐
print("".isspace())             #False: 문자열이 공백이면 True 아니면 False     빈칸이 없는걸 공백으로 보냐
print(" a ".isspace())          #False: 문자열이 공백이면 True 아니면 False     중간에 글자 낀걸 공백으로 보냐

print("-------------------------")
print("25".zfill(10))               #0000000025     10칸을 25로 채워라    
print("1234".zfill(10))             #0000001234     
print("12345678912345".zfill(10))   #12345678912345   10칸이 넘으면 그냥 나옴
print(" abcd".zfill(10))            #00000 abcd         빈칸도 글자로 봄
print( "3".zfill(2) +":" + "7".zfill(2))    #사용예시 03시07분