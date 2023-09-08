month = int(input())
day = int(input())

if(day < 18):
    if(month == 2):
        print('Before')
    elif(month > 2):
        print('After')
    else:
        print('Before')
elif(day == 18):
    if(month == 2):
        print('Special')
    elif(month > 2):
        print('After')
    else:
        print('Before')
else:
    if(month == 2):
        print('After')
    elif(month > 2):
        print('After')
    else:
        print('Before')