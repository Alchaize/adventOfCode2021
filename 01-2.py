f = open("input/01-1.txt", "r")

numberOfIncreases = 0

buffer = []

for x in range(4):
	buffer.append(int(f.readline()))

temp = None
while True:
	if buffer[0] + buffer[1] + buffer[2] < buffer[1] + buffer[2] + buffer[3]:
		numberOfIncreases += 1
	temp = f.readline()
	if not temp:
		break
	buffer.pop(0)
	buffer.append(int(temp))

print(numberOfIncreases)

f.close()