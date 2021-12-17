f = open("input/01-1.txt", "r")

numberOfIncreases = 0
last = 0
for x in f:
	if int(x) > last:
		numberOfIncreases += 1
	last = int(x)

numberOfIncreases -= 1
print(numberOfIncreases)