f = open("input/02-1.txt", "r")

x = 0
y = 0


for a in f:
	line = a.partition(" ")

	if "up" in line[0]:
		y -= int(line[2])
	else:
		if "down" in line[0]:
			y += int(line[2])
		else:
			if "forward" in line[0]:
				x += int(line[2])

print(x*y)

f.close()