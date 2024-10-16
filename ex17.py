# 조건문

num = input("숫자를 입력하세요\n")
print(type(num))            # str 문자열임
int_num = int(num)

# 들여쓰기 중요함 그게 {} 대신임
if int_num>0:
    print("양수")
elif int_num<0:
    print("음수")
else:
    print("0입니다.")