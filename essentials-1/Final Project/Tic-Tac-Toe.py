from random import randrange

board = [
    [1, 2, 3],
    [4, "X", 6],
    [7, 8, 9]
]

def display_board(board):
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        print("|", end="")
        for cell in row:
            print(f"   {cell}   |", end="")
        print()
        print("|       |       |       |")
        print("+-------+-------+-------+")



def enter_move(board):
    while True:
        try:
            move = int(input("Enter your move: "))

            if move < 1 or move > 9:
                print("Choose a number between 1 and 9.")
                continue

            row = (move - 1) // 3
            col = (move - 1) % 3

            if board[row][col] in ["X", "O"]:
                print("That square is already occupied.")
                continue

            board[row][col] = "O"
            break

        except ValueError:
            print("Please enter a valid number.")

def make_list_of_free_fields(board):
    free = []

    for row in range(3):
        for col in range(3):
            if board[row][col] not in ["X", "O"]:
                free.append((row, col))

    return free

def victory_for(board, sign):
  
    for row in board:
        if row == [sign, sign, sign]:
            return True

 
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == sign:
            return True

  
    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True

    if board[0][2] == board[1][1] == board[2][0] == sign:
        return True

    return False

def draw_move(board):
    free = make_list_of_free_fields(board)

    if free:
        row, col = free[randrange(len(free))]
        board[row][col] = "X"

while True : 
    display_board(board)

    enter_move(board)

    if victory_for(board, "O"):
        display_board(board)
        print("You won!")
        break

    if not make_list_of_free_fields(board):
        display_board(board)
        print("Tie!")
        break

    draw_move(board)

    if victory_for(board, "X"):
        display_board(board)
        print("Computer won!")
        break

    if not make_list_of_free_fields(board):
        display_board(board)
        print("Tie!")
        break
