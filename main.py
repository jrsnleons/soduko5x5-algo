import numpy as np

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
            print(c, end = " ")
        print() 

def addnum(col, row, array, num):
    array[col-1][row-1] = num

def init_given_table(array):
    n = 1
    while n <= 5:
        r = 0
        c = 0
        x, y = input("Enter the coordinates where you want to add " + str(n) + " [x y]: ").split()
        x = int(x)
        y = int(y)
        if(x < 6 and x > 0 and y < 6 and y > 0) :
            addnum(x, y, array, n)
            output_table(array)
            n+=1
        else:
            print("Please only input valid numbers (1-5)")



output_table(array)
init_given_table(array)