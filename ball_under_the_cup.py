str = input()
loc = 1
for move in str:
	if(move == 'A' and loc == 1):
		loc = 2
	elif(move == 'A' and loc == 2):
		loc = 1
	elif(move == 'B' and loc == 2):
		loc = 3
	elif(move == 'B' and loc == 3):
		loc = 2
	elif(move == 'C' and loc == 1):
		loc = 3
	elif(move == 'C' and loc == 3):
		loc = 1
print(loc)