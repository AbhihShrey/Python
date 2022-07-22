# create a two dimentional array for the grid
# When the player moves, ask them for a column and row.
# -> the spot in which the player moved, place an x or o depending on whether it is player 1 or 2.
# Check for win

grid = [["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"]]


def print_grid(grid):
    print("+-+-+-+")
    for row in range(len(grid)):
        col_str = "|"
        for column in range(len(grid[row])):
            col_str = col_str + grid[row][column] + "|"
        print(col_str)
        print("+-+-+-+")


def check_valid(grid, row, col):
    if row < 0 or row > 2:
        return False
    if col < 0 or col > 2:
        return False
    if grid[row][col] != "-":
        return False
    return True


def ask_input(player):
    player_row = int(input(f"{player} Enter a row: "))
    player_column = int(input(f"{player} Enter a column: "))
    player_row_real = player_row - 1
    player_column_real = player_column - 1

    return (player_row_real, player_column_real)


def check_win(grid, player1):
    symbol = "X" if player1 else "O"

    # Check if any rows are winners
    for row in range(len(grid)):
        # Check if this row is a WINNER
        found = True
        for col in range(len(grid[row])):
            if grid[row][col] != symbol:
                found = False
        if found:
            return True

    # Check if any cols are winners
    for col in range(len(grid)):
        found = True
        for row in range(len(grid[col])):
            if grid[row][col] != symbol:
                found = False
        if found:
            return True

    # Check left to right diagonal
    row = 0
    col = 0
    found = True
    while found and (row < 3 and col < 3):
        if grid[row][col] != symbol:
            found = False
        row = row + 1
        col = col + 1
    if found:
        return True

    # Check right to left diagonal
    row = len(grid)-1
    col = 0
    found = True
    while found and (row >= 0 and col < 3):
        if grid[row][col] != symbol:
            found = False
        row = row - 1
        col = col + 1
    if found:
        return True

    return False


win = False
while True:
    row, col = ask_input("Player1")
    while not check_valid(grid, row, col):
        row, col = ask_input("Player1")

    grid[row][col] = "X"
    win = check_win(grid, True)
    if win:
        print("Player1 WON!!")
        print_grid(grid)
        break

    print_grid(grid)

    row, col = ask_input("Player2")
    while not check_valid(grid, row, col):
        row, col = ask_input("Player2")

    grid[row][col] = "O"
    win = check_win(grid, False)
    if win:
        print("Player2 WON!!")
        print_grid(grid)
        break

    print_grid(grid)
