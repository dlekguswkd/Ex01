# 대입문
a = 3
b = 5
c = a + b
print(a, b, c)


# 대입문 오류
# 1 + 3 = a
# a를 4에 대입하라 (오른쪽꺼를 왼쪽에 대입하라는 뜻임)


# ; 쓸땐 두가지를 한줄에 쓰고싶을때 끝맺음을 해주는역할 하지만 보통 저렇게 안씀
e = 3.5; f = 5.3
print(e, f)


# 여러 변수를 한번에 대입
"""
g = 3.5
h = 5.3
i = 100
"""
g, h, i = 3.5, 5.3, 100
print(g, h, i)
# 순서대로 잘 들어감 대신 주의할점 갯수가 왼쪽 오른쪽 맞아야 함 아니면 오류


# 여러 개를 같은 값 10으로 대입
"""
x = 10
y = 10
x = 10
"""
x=y=z=10
print(x, y, z)


# 값 교환하기 -> 다른 언어에서는 임시변수를 만들어야함
j = 3.5
k = 100
print(j, k)
"""
temp = j  임시변수 시용
j = k
k = temp
print(j, k)
"""
j, k = k, j     # 방식이 여러변수 한번에 대입
print(j, k)


# 같은 이름의 변수 사용 (그래서 보통 변수는 위에 선언)
num = 1
print(num, type(num))

num = "hello"
print(num, type(num))
# 자료형이 바껴버림 오류는 안뜸
