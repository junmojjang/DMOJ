bugger = int(input())
side = int(input())
drink = int(input())
dessert = int(input())
Calorie = 0

if bugger == 1:
    Calorie = Calorie + 461
elif bugger == 2:
    Calorie = Calorie + 431
elif bugger == 3:
    Calorie = Calorie + 420
elif bugger == 4:
    Calorie = Calorie + 0

if side == 1:
    Calorie = Calorie + 100
elif side == 2:
    Calorie = Calorie + 57
elif side == 3:
    Calorie = Calorie + 70
elif side == 4:
    Calorie = Calorie + 0

if drink == 1:
    Calorie = Calorie + 130
elif drink == 2:
    Calorie = Calorie + 160
elif drink == 3:
    Calorie = Calorie + 118
elif drink == 4:
    Calorie = Calorie + 0

if dessert == 1:
    Calorie = Calorie + 167
elif dessert == 2:
    Calorie = Calorie + 226
elif dessert == 3:
    Calorie = Calorie + 75
elif dessert == 4:
    Calorie = Calorie + 0

print(f"Your total Calorie count is {Calorie}.")