# wc17c3j3
'''
암호는 8자리에서 12사이의 문자열이며 모든 문자에 소문자 3자이상, 대문자 2자이상, 숫자 1자 이상을 포함해야한다.

입력: 단일 문자열인 암호
출력: 암호가 유효 -> Valid, 암호가 무효 -> Invalid
'''

password = str(input())
upper = 0
lower = 0
number = 0

if len(password) >= 8 and len(password) <= 12:
    for i in password: # 여기서 len(password)를 썼는데 에러가 계속 나왔음 생각해보니 len을 쓰면 안된다..!
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        else:
            number += 1

if (upper >= 2) and (lower >= 3) and (number >=1):
    print("Valid")
else:
    print("Invalid")