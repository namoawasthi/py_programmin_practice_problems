n = int(input())
yesterday = input()
today = input()
filled_spaces = 0

for i in range(n):
    if(yesterday[i] == today[i] == 'C'):
        filled_spaces+=1
print(filled_spaces)