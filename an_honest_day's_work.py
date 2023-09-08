p = int(input())
b = int(input())
d = int(input())

number_of_bottle_caps_painted = p//b
remaining_paint = p%b
money_made = number_of_bottle_caps_painted * d + remaining_paint
print(money_made)