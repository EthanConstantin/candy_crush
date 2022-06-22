# Making the board
import random
grid = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []
]


def new_random_grid():
    """Randomizing the 8 by 8 board that the user will play on"""
    for row in range(8):
        for col in range(8):
            grid[row].append(random.randint(1, 5))

    def starting_match_check():
        """Making the initial board have no starting matches"""
        matches_found = 0
        for row in range(len(grid)):
            for col in range(len(grid)):
                """print(row, col)"""
                if 1 <= row <= 6:
                    if grid[row][col] == grid[row + 1][col] == grid[row - 1][col]:
                        grid[row][col] = random.randint(1, 5)
                        grid[row + 1][col] = random.randint(1, 5)
                        grid[row - 1][col] = random.randint(1, 5)
                        matches_found += 1
                if 1 <= col <= 6:
                    if grid[row][col] == grid[row][col + 1] == grid[row][col - 1]:
                        grid[row][col] = random.randint(1, 5)
                        grid[row][col + 1] = random.randint(1, 5)
                        grid[row][col - 1] = random.randint(1, 5)
                        matches_found += 1
                if matches_found > 0:
                    starting_match_check()
    starting_match_check()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Presenting the board
def show_grid():
    """Formatting the grid"""
    letters = {1: "Q", 2: "R", 3: "S", 4: "T", 5: "U"}
    print("      1     2     3     4     5     6     7     8")
    print("   -------------------------------------------------")
    for i in range(len(grid)):
        print(i + 1, end="  |  ")
        for j in grid[i]:
            print(letters[j], end="  |  ")
        print("\n   -------------------------------------------------")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Checking if any matches have been made after the player moves
def check_matches():
    matches_found = 0
    for row in range(len(grid)):
        for col in range(len(grid)):
            """Simulating falling"""
            if 1 <= row <= 6:
                if grid[row][col] == grid[row + 1][col] == grid[row - 1][col]:
                    matches_found += 1
                    for i in range(1, -7, -1):
                        """This check is so that it doesnt try and replace items outside of the grid's range"""
                        if row + i - 3 >= 0:
                            grid[row + i][col] = grid[row + i - 3][col]
                        else:
                            grid[row + i][col] = random.randint(1, 5)
            if 1 <= col <= 6:
                if grid[row][col] == grid[row][col + 1] == grid[row][col - 1]:
                    matches_found += 1
                    for i in range(0, -8, -1):
                        """This check is so that it doesnt try and replace items outside of the grid's range"""
                        if row + i - 1 >= 0:
                            grid[row + i][col + 1] = grid[row + i - 1][col + 1]
                            grid[row + i][col] = grid[row + i - 1][col]
                            grid[row + i][col - 1] = grid[row + i - 1][col - 1]
                        else:
                            grid[row + i][col + 1] = random.randint(1, 5)
                            grid[row + i][col] = random.randint(1, 5)
                            grid[row + i][col - 1] = random.randint(1, 5)

    # global times_ran
    # global score
    # if times_ran == 0:
    #     score += matches_found
    # if matches_found > 0:
    #     times_ran += 1
    #     check_matches()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Swapping 2 letters
def update_grid():
    """Asking for user's desired action"""
    x = int(input("What is the column of the piece you want to move? ")) - 1
    while x < 0 or x > 7:
        x = int(input("There are only 8 columns on the board, make sure you choose a number between one and eight. "))-1
    y = int(input("what is the row of the piece you want to move? ")) - 1
    while y < 0 or y > 7:
        y = int(input("There are only 8 rows on the board, make sure you choose a number between one and eight. "))-1
    swap_direction = input("what direction do you want to move the letter in? ").strip().lower()
    possible_swaps = ["up", "down", "left", "right"]
    while (swap_direction == "up" and y == 0) or (swap_direction == "down" and y == 7) \
            or (swap_direction == "left" and x == 0) or (swap_direction == "right" and x == 7)\
            or (swap_direction not in possible_swaps):
        swap_direction = input("Please choose a valid direction. ")
    """Swapping the place of 2 letters"""
    if swap_direction == "up":
        grid[y - 1][x], grid[y][x] = grid[y][x], grid[y - 1][x]
    if swap_direction == "down":
        grid[y + 1][x], grid[y][x] = grid[y][x], grid[y + 1][x]
    if swap_direction == "left":
        grid[y][x - 1], grid[y][x] = grid[y][x], grid[y][x - 1]
    if swap_direction == "right":
        grid[y][x + 1], grid[y][x] = grid[y][x], grid[y][x + 1]


new_random_grid()
show_grid()
update_grid()
check_matches()
show_grid()