board = []

for _ in range(9):
    row = input()
    
    if len(row) != 9 or not row.isdigit():
        print("No")
        exit()
    
    board.append([int(digit) for digit in row])

valid = True

# Check rows
for row in board:
    if set(row) != set(range(1, 10)):
        valid = False

# Check columns
for col in range(9):
    column = [board[row][col] for row in range(9)]
    if set(column) != set(range(1, 10)):
        valid = False

# Check 3x3 sub-squares
for row in range(0, 9, 3):
    for col in range(0, 9, 3):
        square = []

        for r in range(row, row + 3):
            for c in range(col, col + 3):
                square.append(board[r][c])

        if set(square) != set(range(1, 10)):
            valid = False

if valid:
    print("Yes")
else:
    print("No")
