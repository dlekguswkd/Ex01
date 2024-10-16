# 출력

print("orange" "banan" "apple")
print("orange"+"banan"+"apple")
print("orange", "banan", "apple")

print("---------------------------")

# sep=" " 이게 디폴트임 생략되어있을때
print("orange", "banan", "apple", sep=",")      # 중간의 값을 정해주는것


# end="\n" 이게 디폴트임 생략되어있을때
# print("orange", "banan", "apple", end="===")    # 맨끝에 붙여줌   
print("orange", "banan", "apple", end=" 이다")      # 기본값인 줄바꿈이 사라짐
print("---------------------------")                # 그래서 옆에 나옴
print("==============================================")

print("orange", "banan", "apple", sep=",", end=" 이다")      # 기본값인 줄바꿈이 사라짐
print("---------------------------")                        # 그래서 옆에 나옴

# 기본값 sep=" " end="\n"  -> 변경해서 쓸수있다 