# coci16c1p1

'''
페로는 한달에 데이터는 x MB 제공하는 휴대전화 공급자의 데이터 요금제를 사용중
특정 달에 사용하지 않은 데이터는 다음 달로 이월
예를 들어 x가 10, 페로가 4MB사용했다면 나머지 6MB는 그 다음 달로 이월(다음 달에는 10 + 6 = 16MB사용가능)

입력
- 페로에게 매월 주어지는 데이터 량 x를 포함한 라인으로 x는 1에서 100사이 정수
- 페로가 데이터 요금제를 사용한 개월 수 n을 포함한 라인으로 n은 1에서 100사이 정수
- 데이터 요금제 사용 기간 동안 페로가 사용한 데이터량을 월별로 한 줄씩 제공하는 n개의 라인, 각 숫자는 최소 0이며 사용 가능한 MB를 초과 X

출력
- 페로가 다음 달에 사용할 수 있는 메가바이트 수를 출력
'''

month_mb = int(input())
n = int(input())

total_mb = month_mb * (n+1)

for _ in range(n):
    used = int(input())
    total_mb = total_mb - used

print(total_mb)