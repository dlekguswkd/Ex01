# 확장연산자

# i = i +1
# i += 1
# # 두개가 같은 표현임

x = 3
# x = x + 3
x += 3
print(x)


y = 2
# y = y**2
y**=2
print(y) # y = y**3 -->64

print("----------------------------")

# 관계 연산자
print(1 > 3)        # False
print(2 < 4)        # True
print(4 <= 5)       # True
print(4 >= 5)       # False
print(6 == 9)       # False
print(6 != 9)       # True

print("----------------------------")

# 객체의 대소 (구간) 비교하는 연산
# a가 0보다 크고 10보다 작다
# (0 < a or a< 10)
a = 6
print(0<a<10)       # 두개를 한번에 표현할수있다
print(0<a and a< 10)

print("----------------------------")

a = 10
b = 20
c = a
d = 11
e = 11

# 주소값(고유번호?)알려주는 id
print(id(a))
print(id(b))
print(id(c))
print(id(d))
print(id(e))
# a 와 c , d 와 e 의 주소가 같음 ->  같은 숫자면 똑같은게 있는지 찾아보고 똑같은 주소를 가르킴

print("----------------------------")

# 값 비교 == , 주소비교 is
print( a==b )       # False 값비교
print( a is b )     # False 주소비교
print( a is c )     # True  주소비교
print( a is d)      # False 주소비교
print( d is e)      # True  주소비교

print("----------------------------")

# 논리 연산자
print(True and True)
print(False and True)   # False

print(False or True)    # True

print(not True)         # False
print(not (False or True))    # False

print("----------------------------")

# 내장 수치 함수
print(abs(-3))      # 절대값 3
print(abs(3))       # 절대값 3

print(int(3.1415))  # 정수형으로 실수 -> 정수  3
# print(int(3+4j))    # 복소수 -> 정수 오류남
print(int("4"))     # 문자열 -> 정수    4
# print(int("4.34"))     # 문자열,실수형 -> 정수 오류남

print(float(3))         # 정수 -> 실수형 3.0
print(float("4"))     # 문자열 -> 실수    4.0
# print(float(4+5j))     # 복소수 -> 실수    오류남

print(complex(3))       # 복소수형으로 정수 -> 복소수  3+ 0j
print(complex("3"))       # 복소수형으로 문자열 -> 복소수  3+ 0j
print(complex("3+0j"))       # 복소수형으로 정수 -> 복소수  3+ 0j

print(pow(2, 10))           # 2**10     1024


