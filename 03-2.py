def calcBits(lst, index):
	ones = 0
	zeroes = 0

	for x in lst:
		if x[index] == '1':
			ones += 1
		else:
			zeroes += 1

	return (ones, zeroes)


f = open("input/03-1.txt", "r")

# Store data from file
bank = []

for x in f:
	bank.append(x.rstrip('\n'))

f.close()

numberLength = len(bank[0])
oxygen = bank.copy()
carbon = bank.copy()
bank.clear()

# Very good name for a list containing indices of what I will remove
yo = []

# Calculate which binary number is the oxygen thing
for x in range(numberLength):

	(numOnes, numZeroes) = calcBits(oxygen, x)

	# If fewer zeroes, remove numbers with zeroes here
	if numOnes >= numZeroes:
		for y in range(len(oxygen)):
			if (oxygen[y])[x] == '0':
				yo.insert(0, y)
	else:
		# Fewer ones -> remove numbers with ones here
		for y in range(len(oxygen)):
			if (oxygen[y])[x] == '1':
				yo.insert(0, y)

	# Remove items now that we've looked through the list
	for y in yo:
		oxygen.pop(y)
	yo.clear()

	# Don't continue if we only have one left
	if len(oxygen) == 1:
		break

# Calculate which binary number is the carbon thing
for x in range(numberLength):

	(numOnes, numZeroes) = calcBits(carbon, x)

	# If more ones, remove numbers with ones here
	if numOnes >= numZeroes:
		for y in range(len(carbon)):
			if (carbon[y])[x] == '1':
				yo.insert(0, y)
	else:
		# More zeroes -> remove numbers with zeroes here
		for y in range(len(carbon)):
			if (carbon[y])[x] == '0':
				yo.insert(0, y)

	# Remove items now that we've looked through the list
	for y in yo:
		carbon.pop(y)
	yo.clear()

	# Don't continue if we only have one left
	if len(carbon) == 1:
		break

# Convert binary in a string to decimal as an integer
oxy, car = int(oxygen[0],2), int(carbon[0],2)

# Result
print(oxy * car)