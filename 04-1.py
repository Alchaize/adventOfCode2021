def isBingo(board, x, y):
	if sum(board[x]) == -5:
		return True
	if sum([x[y] for x in board]) == -5:
		return True
	return False	

def computeBingo(board, number):
	# Find numbers to mark, convert them to -1 (= marked)
	for row in range(5):
		for col in range(5):
			if number == board[row][col]:
				board[row][col] = -1
				# Check if bingo
				if isBingo(board, row, col):
					return sum([0 if board[i][j] == -1 else board[i][j] for i in range(5) for j in range(5)])

	return None

def searchForBingo(boards, number):
	for board in range(len(boards)):
		bingoScore = computeBingo(boards[board], number)

		if bingoScore is not None:
			return bingoScore * number


	return None


# Read file information
f = open("input/04-1.txt", "r")

# Get information on first line
turns = f.readline()
turns = turns[:len(turns)-1].split(',')
turns.reverse()
f.readline()

# Vars
boards = []
temp = []

# Get boards information
for x in f:
	if x != '\n':
		# Split string into list
		y = x[:len(x)-1].split(" ")
		# Remove empty strings
		while len(y) > 5:
			y.remove('')
		# Store part of a board
		temp.append(y)
	else:
		boards.append(temp.copy())
		temp.clear()

boards.append(temp)

f.close()
# End of file reading

# Convert the strings/chars to integers
# Turns
for x in range(len(turns)): 
	turns[x] = int(turns[x])
# Boards
for x in boards:			
	for y in range(len(x)):
		for z in range(len(x[y])):
			x[y][z] = int(x[y][z])

# Keep track of what numbers have been drawn
numbersDrawn = []
latestNumber = None
score = None

# Main loop
while turns:
	latestNumber = turns.pop()
	numbersDrawn.append(latestNumber)

	score = searchForBingo(boards, latestNumber)
	if score is not None:
		break

print(score)