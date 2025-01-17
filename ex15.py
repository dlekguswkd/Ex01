# 연습하기

age = 33
num = 123.456789
name = "홍길동"

# 정수 출력
# 나이: 33
print(f"나이: {age}")

# 나이: (최소 너비 5): 33
print(f"나이: {age:5d}")

# 나이 (0으로 채우기, 3자리): 033
print(f"나이: {age:05d}")

# 오른쪽 정렬 (5자리): 33
print(f"나이: {age:>5d}")
# 왼쪽 정렬 (5자리): 33
print(f"나이: {age:<5d}")
# 가운데 정렬 (5자리): 33
print(f"나이: {age:^5d}")

print("---------------------------")

# 실수 출력
# 숫자: 123.456789
print(f"숫자: {num}")

# 숫자 (소수점 둘째 자리): 123.46
print(f"숫자: {num:.2f}")

# 숫자 (소수점 셋째 자리): 123.457
print(f"숫자: {num:.3f}")

# 숫자 (오른쪽 정렬, 최소 15자리): 123.46
print(f"숫자: {num:>15f}")
# 숫자 (왼쪽 정렬, 최소 15자리): 123.46
print(f"숫자: {num:<15f}")
# 숫자 (가운데 정렬, 최소 15자리): 123.46
print(f"숫자: {num:^15f}")

print("---------------------------")

# 문자열 출력
# 이름: 홍길동
print("이름: "+name)
print(f"이름: {name}")

# 이름 (최소 너비 10): 홍길동
print(f"이름: {name:10}")

# 이름 (오른쪽 정렬, 10자리): 홍길동
print(f"이름: {name:>10}")
# 이름 (왼쪽 정렬, 10자리): 홍길동
print(f"이름: {name:<10}")
# 이름 (가운데 정렬, 10자리): 홍길동
print(f"이름: {name:^10}")