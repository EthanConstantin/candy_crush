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
                """Here i check all rows and columns except for the first and last, so i dont index out of range"""
                """print(row, col)"""
                if 1 <= row <= 6:
                    """Checks to see if the element has a duplicate to the left and right of it, making it a match"""
                    if grid[row][col] == grid[row + 1][col] == grid[row - 1][col]:
                        """If it confirms a match has been made, it replaces the matched elements with new,
                        random elements"""
                        grid[row][col] = random.randint(1, 5)
                        grid[row + 1][col] = random.randint(1, 5)
                        grid[row - 1][col] = random.randint(1, 5)
                        matches_found += 1
                    """Checks to see if the element has a duplicate above and below it, making it a match"""
                if 1 <= col <= 6:
                    if grid[row][col] == grid[row][col + 1] == grid[row][col - 1]:
                        grid[row][col] = random.randint(1, 5)
                        grid[row][col + 1] = random.randint(1, 5)
                        grid[row][col - 1] = random.randint(1, 5)
                        matches_found += 1
                """If at least 1 match has been found, it runs the function again to see if there are matches, because
                there is a chance the new random elements are also matches as well"""
                if matches_found > 0:
                    starting_match_check()
    starting_match_check()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Presenting the board
def show_grid():
    """Formatting an easy-to-understand grid with an x and y-axis, replacing the numbers with letters"""
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
            """Replacing matches with with elements 3 tiles above it, to simulate falling"""
            """print(row, col)"""
            if 1 <= row <= 6:
                """Checks to see if the element has a duplicate to the left and right of it, making it a match"""
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

    """Returning the matches found for only the first instance the function is run"""
    global times_ran
    global score
    if times_ran == 0:
        score += matches_found
    """Making sure none of the new random letters make a match"""
    if matches_found > 0:
        times_ran += 1
        check_matches()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Swapping 2 letters
def update_grid():
    """Asking for user's desired action"""
    """input for the co-ordinates of the letter the user wants to move"""
    x = int(input("What is the column of the piece you want to move? ")) - 1
    while x < 1 or x > 7:
        x = int(input("There are only 8 columns on the board, make sure you choose a number between one and eight. "))
    y = int(input("what is the row of the piece you want to move? ")) - 1
    while y < 1 or y > 7:
        y = int(input("There are only 8 rows on the board, make sure you choose a number between one and eight. "))
    swap_direction = input("what direction do you want to move the letter in? ").strip().lower()
    possible_swaps = ["up", "down", "left", "right"]
    """Checking if the swap direction is valid, and the user isn't trying to move a piece off the grid"""
    while (swap_direction == "up" and y == 0) or (swap_direction == "down" and y == 7) \
            or (swap_direction == "left" and x == 0) or (swap_direction == "right" and x == 7)\
            or (swap_direction not in possible_swaps):
        swap_direction = input("Please choose a valid direction. ")
    """Swapping the place of 2 LETTERS on the grid, depending on the direction the user specified"""
    if swap_direction == "up":
        grid[y - 1][x], grid[y][x] = grid[y][x], grid[y - 1][x]
    if swap_direction == "down":
        grid[y + 1][x], grid[y][x] = grid[y][x], grid[y + 1][x]
    if swap_direction == "left":
        grid[y][x - 1], grid[y][x] = grid[y][x], grid[y][x - 1]
    if swap_direction == "right":
        grid[y][x + 1], grid[y][x] = grid[y][x], grid[y][x + 1]
    global moves
    moves += 1

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# This is a function to actually run the game, and call all the other functions I've defined so far
def run_lvl(lvl):
    matches_needed, moves_needed = lvl
    print(f"For this level, you need to get {matches_needed} matches "
          f"in {moves_needed} moves or less to win! Good luck!")
    new_random_grid()
    global score
    score = 0
    global moves
    moves = 0
    while score < matches_needed and moves < moves_needed:
        show_grid()
        update_grid()
        global times_ran
        times_ran = 0
        check_matches()
        print(f"\nMoves: {moves} \nScore: {score} \nYou need to get {matches_needed - score} matches in "
              f"{moves_needed - moves} moves to win")
    if score >= matches_needed and moves >= moves_needed:
        print("You just barely clutched that win! Good job!")
        return True
    else:
        if score >= matches_needed:
            print("Good job! You beat the level!\n")
            return True
        if moves >= moves_needed:
            print(f"You lost. You only needed {matches_needed - score} matches more to win.")
            return False


# The first number is the matches you need to get in that level, and the second number is how many moves you have
lvl1 = 7, 15
lvl2 = 8, 14
lvl3 = 9, 10
lvl4 = 8, 8
lvl5 = 9, 7

# Running the game
print("Try and beat all 5 levels in this match 3 game in as few moves as you can.")
if run_lvl(lvl1) and run_lvl(lvl2) and run_lvl(lvl3) and run_lvl(lvl4) and run_lvl(lvl5) == True:
    print("Congratulations! You beat the whole game!")
else:
    print("Play again soon!")
