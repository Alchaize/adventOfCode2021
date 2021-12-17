f = open("input/03-1.txt", "r")

totalNumbers = 1
numOfOnes = []

x = f.readline()

for a in x[0:len(x)-1]:
	numOfOnes.append(int(a))

for x in f:
	totalNumbers += 1
	for y in range(len(x)):
		if x[y] == '1':
			numOfOnes[y] += 1


gammaRate = []
epsilonRate = []

totalNumbers //= 2

for x in numOfOnes:
	if x > totalNumbers:
		gammaRate.insert(0, 1)
		epsilonRate.insert(0, 0)
	else:
		gammaRate.insert(0, 0)
		epsilonRate.insert(0, 1)

gr, er = 0, 0
for x in range(len(gammaRate)):
	if gammaRate[x] == 1:
		gr += pow(2, x)
	
	if epsilonRate[x] == 1:
		er += pow(2, x)

print(gr*er)