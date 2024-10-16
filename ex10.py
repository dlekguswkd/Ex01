# 문자열의 연산

str1 = "FirstString"
str2 = "SecondString"

print(str1 + str2)

print(str1*3)       # 3번 반복됨

print("-"*30)
print("My program")
print("-"*30)
# print("-"+30)     이건 오류뜸 숫자하고 문자는 못더함


s = "First String"
# 문자 배열로 들어가있음
print(s[0], s[1], s[4])         # 한칸씩 공백이 들어있음 -> 3개를 보내는거고
print(s[0] + s[1] + s[4])       # 다 붙어져있음         -> 데이터 1개

# 같은 의미 (마지막글자)
print(s[11])                   
print(s[-1])                    # 뒤에서부터 반대로도 가능 (몇글자인지 안세도 되서 편함)

# 같은표현 (첫번째글자)
print(s[0])
print(s[-12])  

# [0], [-0] 똑같음 첫번째 글자
print(s[0], s[-0])  

# F r _ S g
print(s[0], s[2], s[5], s[6], s[11])
print(s[-12], s[-10], s[-7], s[-6], s[-1])

print("-"*30)

# 3개 다 같은표현
print(s[0]+s[1]+s[2]+s[3]+s[4])
print(s[0:5])       # 시작번호(포함): 끝번호(자기포함x)  -> 0번방부터 4번째방까지
print(s[:5])        # 0번은 생략가능 처음부터~

print("-"*30)
print(s[1:9:2])       # 첫번째방부터 8번째방까지 두칸씩 뛰어넘기 2씩증가

print(s[3:11])      # -> 마지막글자가 안나옴 10번째방까지나오는거기때문
print(s[3:])        # 끝까지에서도 생략가능 3부터 끝까지

print(s[:])         # 처음부터 끝까지
print(s[-6:-2])     

print(s[::2])       # 처음부터 끝까지 두개씩
print(s[::-1])      # 처음부터 끝까지인데 뒤에서부터 거꾸로 -> 문자열을 역으로 출력함

# 빈칸 글자 넣기
# s[5] = 'a'
# print(s)    오류뜸 -> 전체는 변경되지만 부분은 변경 불가 -> s를 그냥 바꿔야함
s = "FirstaString"      # 이렇게 전체를 변경해주는건 가능

name = "이효리"
name2 = name[::-1]

print(name, name2)
print("이효리" == name[::-1])

name = "토마토"
name2 = name[::-1]

print(name, name2)
print("토마토" == name[::-1])