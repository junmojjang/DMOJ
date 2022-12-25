''' 
- 입력은 소문자와 공백만 있는 텍스트입니다(ASCII 코드 32). 얼마나 많은 단어가 있는지 세어야 합니다.
- input = "problem one is really long"
- ouput = "5"

'''

# 풀이 -> 단어는 공백으로 구분되어 있다. 따라서 공백의 갯수를 세어보자 하지만 마지막은 공백이 없음으로 +1

line = input()
total_words = line.count(" ")+1
print(total_words)
