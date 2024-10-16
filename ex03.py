# bool형 (참, 거짓)
a = 1
b = a<10
print(b, type(b))    # True  bool


# bool형 연산
# True -> 1, False -> 0
print(True + True)      # 1 + 1   2
print(1 == True)        # 1 == 1  True
print(0 == False)       # 0 == 0  True


# bool형과 정수형 연산
b1 = True
b2 = False
print(b1+10)        # True + 10 -> 1 + 10 -> 11
print(b2+10)        # True + 10 -> 0 + 10 -> 10