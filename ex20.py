# 반복문 for문

# 잘넣어놓은걸 꺼내는
animal_list = ["cat", "cow", "tiger"]

for animal in animal_list:
    print(animal)


print("-------------------------")

# 값을 꺼내는게 아닌 
for no in range(10):        # 10개 뽑아줘 라서 0부터 9까지  0부터의 0은 생략가능
    print(no)
print("-------------------------")
for no in range(0,10):        # 10개 뽑아줘 라서 0부터 9까지 위랑 같은 표현
    print(no)
for no in range(5,10):        # 5부터 9까지 위랑 같은 표현
    print(no)
print("-------------------------")
for no in range(0,10,3):        # 0부터 9까지 3증가씩
    print(no)

print("-------------------------")
# [예제 for03.py] 아래와 같이 출력하는 프로그램을 작성하세요 0 2 4 6 8
for no in range(0,10,2):
    print(no)

print("-------------------------")
# [예제 for03.py] 아래와 같이 출력하는 프로그램을 작성하세요 5 4 3 2 1 0 -1 -2 -3 -4 -5
for no in range(5, -6, -1):
    print(no)

print("-------------------------")

# 구구단 전체
print("----구구단전체-----")
for dan in range(2,10):
    for i in range(1,10):
        print(f"{dan}*{i}={dan*i}")


# [문제 for04.py] 숫자를 입력받아 입력한 숫자(단)의 구구단을 출력하세요 (for문으로작성)
print("----구구단-----")
dan = int(input("숫자를 입력해주세요. \n"))

for no in range(1,10):
    print(f"{dan}*{no}={dan*no}")