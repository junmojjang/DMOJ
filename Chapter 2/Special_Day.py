#ccc15j1

# 2월 18일 이후면 "After"출력, 2월 19일 이전이면 "Before"출력, 2월 18일이면 "Special" 출력
# 맨처음에 month >= 2 and day >= 18하였지만 이렇게 된다면 3월, 4월 등도 18일 이후만 'after'를 출력하기에 밑에 조건 하나더 추가

month = int(input())
day = int(input())

if (month == 2) and (day ==18):
    print("Special")
elif (month >= 2) and (day > 18):
    print("After")
elif (month > 2) and (day > 1):
    print("After")
else:
    print("Before")