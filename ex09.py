# 문자열

s = ""                      # '' 를 사용해도 된다
str1 = "hello world"
str2 = "안녕 세상"

print(s, str1, str2)
print(type(s), type(str1), type(str2))          # 자료형
print(isinstance(str2, str))                    # 결과값 True

print(type(str1) == str)    


# 나는 "정우성" 입니다.
str3 = '나는 "정우성" 입니다.'
# str3 = "나는 \"정우성\" 입니다."      두가지 다 가능
print(str3)


# 나는 '박명수' 입니다.
str4 = "나는 '박명수' 입니다."
# str4 = '나는 \'박명수\' 입니다.'
print(str4)

print("-------------------------")

s01 = "aaa"
s02 = "aaa"
print(s01, id(s01))
print(s02, id(s02))

s02 = "bbb"
print(s01, id(s01))
print(s02, id(s02))

print("-------------------------")

# 이상황은 주석이 아닌 문자열을 몇줄로 쓴다고 알려주는거임
str5 = """ABCDEFG 
abcdefg 
"가나다"라마바사 
123456789"""

print(str5)


# Hello World i'd say "hello World"
print("Hello World i'd say \"hello World\"")        # "를 기본으로 사용
print('Hello World i\'d say "hello World"')         # '를 기본으로 사용

print("Hello \nWorld i'd say \"hello World\"")     # \n 줄바꿈
print("hello!!!!!\rWorld")                         # \r 커서가 현재줄의 맨앞으로 간다 
                                                    # 위에 다시 쓰는거라서 원래있던애들은 남아있는채로 덮여쓰기임
print("hello\bworld")                               # \b 백스페이스 이것도 마찬가지임 뒤로 한칸가서 다시쓰는거임

print("hello\tw\torld")                             # \t 탭  8칸? 띄어짐