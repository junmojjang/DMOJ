# coci08c3p2

'''
루카는 수업 시간에 비밀 문장을 쓰고 있다. 그는 선생님이 읽을 수 없도록 원래의 문장에 어떤 인코딩을 해서 작성을 한다.
문장의 각 모음 뒤에 문자 p와 해당 모음을 다시 추가. 선생님이 루카가 인코딩한 문장을 습득했다. 루카의 원문을 알아내자

입력
한 줄의 텍스트

출력
루카가 보내려 했던 원문
'''

sentence = input()
result = ''
i = 0

while i < len (sentence):
    result = result + sentence[i]
    if sentence[i] in 'aeiou':
        i = i + 3
    else:
        i = i + 1

print(result)