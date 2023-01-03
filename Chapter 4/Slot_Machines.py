# ccc00s1

'''
카지노에는 3개의 슬롯머신이 있고, 칩이 다 떨어질 때까지 슬롯머신을 순서대로 플레이
예를 들어 첫 번째 슬롯머신을 플레이하고, 두번째, 세번째 슬롯머신을 플레이,
그리고 다시 첫번째, 두번째, 세번째로 플레이

첫번째 슬롯머신에서 35번 플레이 할때마다 칩 30개 획득
두번째 슬롯머신에서 100번 플레이 할때마다 칩 60개 획득
세번째 슬롯머신에서 10번 플레이 할때마다 칩 9개 획득
그 외에는 어떤 상금도 없다.

입력
첫 번째 라인은 칩의 개수 n
두 번째 라인은 첫 번째 슬롯머신이 마지막으로 상금을 지불한 이후로 플레이된 횟수
세 번째 라인은 두 번째 슬롯머신이 마지막으로 상금을 지불한 이후 플레이된 횟수
네 번째 라인은 세 번째 슬롯머신이 마지막으로 상금을 지불한 이후 플레이된 횟수

출력
Martha plays x times before going broke. -> x는 마르타가 칩이 없을 때까지 플레이한 횟수
'''

chips = int(input())
first = int(input())
second = int(input())
third = int(input())
count = 0
machine = 0
while chips >= 1:
    chips = chips -1

    if machine == 0:
        first += 1
        if first == 35:
            chips += 30
            first = 0

    elif machine == 1:
        second += 1
        if second == 100:
            chips += 60
            second = 0

    elif machine == 2:
        third += 1
        if third == 10:
            chips += 9
            third = 0
    count += 1
    machine += 1
    if machine == 3:
        machine = 0
print(count)
