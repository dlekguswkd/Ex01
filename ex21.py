# enumerate() 함수

color_List = ["red", "orange", "yellow", "green", "blue"]

for color in color_List:
    print(color)


# index 번호도 같이 줌
for index, color in enumerate(color_List):
    print(index, color)


for index, color in enumerate(color_List):
    if index>3:
        break
    else:
        print(index, color)