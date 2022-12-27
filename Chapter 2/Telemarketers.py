# ccc18j1

'''
전화번호가 네 자리라고 가정, 다음 세 가지 조건을 모두 충족하는 4자리 숫자는 텔레마케터의 전화번호
- 첫 번째 숫자는 8 or 9
- 네 번째 숫자는 8 or 9
- 두 번째와 세 번째 숫자는 동일
ex) 8119 -> 텔레마케터 전화번호
텔레마케터의 전화번호를 확인하고 받을지 무시할것인지 판단

- 입력: 한 라인에 숫자 하나씩, 총 네자리 숫자를 제공하는 4줄의 입력
- 출력: 전화번호가 텔레마케터의 번호라면 ignore출력, 그렇지 않으면 answer출력
'''

num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
num_4 = int(input())

if ((num_1 == 9 or num_1 == 8) and (num_4 == 9 or num_4 == 8) and (num_2 == num_3)):
    print("ignore")
else:
    print("answer")
