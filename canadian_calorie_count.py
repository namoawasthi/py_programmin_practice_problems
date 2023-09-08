bg = int(input())
so = int(input())
drnk = int(input())
desrt = int(input())

if(bg == 1):
    bg_cal = 461
elif(bg == 2):
    bg_cal = 431
elif(bg == 3):
    bg_cal = 420
else:
    bg_cal = 0

if(drnk == 1):
    drnk_cal = 130
elif(drnk == 2):
    drnk_cal = 160
elif(drnk == 3):
    drnk_cal = 118
else:
    drnk_cal = 0

if(so == 1):
    so_cal = 100
elif(so == 2):
    so_cal = 57
elif(so == 3):
    so_cal = 70
else:
    so_cal = 0

if(desrt == 1):
    desrt_cal = 167
elif(desrt == 2):
    desrt_cal = 266
elif(desrt == 3):
    desrt_cal = 75
else:
    desrt_cal = 0

total_cal = bg_cal + drnk_cal + so_cal+ desrt_cal

print(f'Your total Calorie count is {total_cal}.')