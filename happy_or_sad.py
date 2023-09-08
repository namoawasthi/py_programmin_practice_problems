str = input()

h = ':-)'
s = ':-('

if(str.count(h) == 0 and str.count(s) == 0):
    print('none')
elif(str.count(h) > str.count(s)):
    print('happy')
elif(str.count(h) < str.count(s)):
    print('sad')
else:
    print('unsure')