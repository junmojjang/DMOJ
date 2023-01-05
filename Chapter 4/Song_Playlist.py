# ccc08j2
'''
각각 A, B, C, D, E라는 5곡의 노래가 있다.
좋아하는 이 노래들로 재생목록을 만들어 앱에서 관리한다. 처음에 노래는 A, B, C, D, E순서로 재생되며, 앱에는 4개의 버튼이있다.

- 버튼1) 재생목록의 첫 번째 곡을 재생목록의 끝으로 이동
- 버튼2) 재생목록의 마지막 곡을 재생목록의 시작 부분으로 이동
- 버튼3) 재생목록의 처음 두 곡의 위치를 바꾼다.
- 버튼4) 재생목록을 재생

입력 
- 한쌍의 라인으로 구성, 첫 번째 라인은 버튼번호(1,2,3,4)를 제공, 두번 째 라인은 사용자가 해당 버튼을 누른 횟수(1~10)까지 제공

출력
- 버튼을 모두 누른 후 재생목록의 노래 순서를 출력, 한줄로 출력되며 그 안에는 각 노래를 구분하는 공백이 있어야 한다. 
'''

songs = 'ABCDE'
button = 0

while button != 4:
    button = int(input())
    presses = int(input())
    for i in range(presses):
        if button == 1:
            songs = songs[1:] + songs[0]
        elif button == 2:
            songs = songs[-1] + songs[:-1]
        elif button == 3:
            songs = songs[1] + songs[0] + songs[2:]
ouput = ''
for song in songs:
    output = output + song + ' '

print(output[:-1])