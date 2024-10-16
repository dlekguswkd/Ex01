# 정수형
a = 101
print(a, type(a))
print(isinstance(a, int))   # 101이 int니? (is~는 보통 물어보는거임)    -> True


# 2진수 8진수 16진수 -> 10진수로 표현
# 이진법 0b라는 기호임 뒤에 글자를 십진수로 알려줌 바이너리?
b = 0b1
print(b)

# 팔진수 0o라는 기호임 옥타곤?  0부터 7까지
c = 0o10
print(c)

# 16진수    10 -> A ... 15 -> F
d = 0x1A
print(d)


# 10진수로 표현 -> 2진수 8진수 16진수
print(bin(5))   # 2진수
print(oct(65))   # 8진수
print(hex(257))   # 16진수


# 큰수 (지수)
e = 2**1024         # **는 제곱
print(e, type(e))