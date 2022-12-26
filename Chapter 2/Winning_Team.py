# ccc19j1
'''
농구에서 점수를 얻는 방법은 총 3가지로, 3점 슛과 2점 슛, 1점 자유투가 있다.
사과팀과 바나나팀의 농구 경기를 보면서 각 팀의 3점, 2점, 1점 성공 횟수를 기록했다.
게임에서 사과팀이 이겼는지 바나나팀이 이겼는지, 두 팀이 비겼는지 표시

- 출력은 단일 문자입니다. 
사과가 바나나보다 점수가 더 높으면 을 출력 A합니다.
바나나가 사과보다 점수가 더 높으면 을 출력 B합니다. 
그렇지 않으면 T동률임을 나타내기 위해 를 출력합니다.

- 총 6줄의 입력이 있습니다. 앞의 세 라인은 사과 팀에 대한 점수를 제공, 뒤의 세 라인은 바나나 팀의 점수를 제공
- 첫번째 라인은 사과 팀의 3점 슛 성공 횟수
- 두번째 라인은 사과 팀의 2점 슛 성공 횟수
- 세번째 라인은 사과팀의 1점 자유투 성공횟수
- 4,5,6번은 동일하게 바나나팀의 성공횟수 

- input = 10, 3, 7, 8, 9, 6
- output = B
'''

apple_1 = int(input())
apple_2 = int(input())
apple_3 = int(input())

banana_1 = int(input())
banana_2 = int(input())
banana_3 = int(input())

apple_total = (apple_1 * 3) + (apple_2 * 2) + (apple_3 * 1)
banana_total = (banana_1 * 3) + (banana_2 * 2) + (banana_3 * 1)

if apple_total > banana_total:
    print("A")
elif banana_total > apple_total:
    print("B")
else:
    print("T")