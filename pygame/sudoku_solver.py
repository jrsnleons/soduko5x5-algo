import numpy as np
from colorama import Fore, Style

array = [[0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0,]]

def output_table(array):
    print("    1 2 3 4 5")
    print("   -----------")
    for count, r in enumerate(array):
        print(count + 1 , end = " | ")
        for c in r:
            if c != 0:
                print(Fore.RED + str(c), end = " " + Fore.RESET)
            else:
                print(c, end = " ")
        print() 

def addnum(col, row, array, num):
    # Adds to the array
    array[col-1][row-1] = num

def init_given_table(array):
    n = 1
    while n <= 5:
        user_input = input("Enter the coordinates where you want to add " + str(n) + " [x y]: ").split()
        # Checks if the user provided two values
        if len(user_input) == 2:
            x, y = map(int, user_input)
            # Checks if the input is a valid number from 1 - 5
            if x < 6 and x > 0 and y < 6 and y > 0 and array[x-1][y-1] == 0:
                addnum(x, y, array, n)
                output_table(array)
                n += 1
            elif array[x-1][y-1] != 0: 
                print("Please only input on empty fields")
            else:
                print("Please only input valid numbers (1-5)")
        else:
            print("Please input 2 values [x y]:")

def is_valid_move(col, row, num, array):
    # Check if the number is already in the row or column
    if num in array[row] or num in [array[i][col] for i in range(5)]:
        return False
    return True

def solve_sudoku(array):
    for row in range(5):
        for col in range(5):
            if array[row][col] == 0:
                for num in range(1, 6):
                    if is_valid_move(col, row, num, array):
                        array[row][col] = num
                        # Check each iteration
                        # output_table(array)
                        if solve_sudoku(array):
                            return True
                        array[row][col] = 0  # Backtrack if the current move doesn't lead to a solution
                return False
    return True