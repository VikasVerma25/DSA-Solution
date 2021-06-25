# You're given a two-dimensional array that represents a 9x9 partially filled 
# Sudoku board. Write a function that returns the solved Sudoku board. Sudoku 
# is a famous number-placement puzzle in which you need to fill a 9x9 grid with 
# integers in the range of 1-9. Each 9x9 Sudoku board is split into 9 3x3 subgrids.
# The objective is to fill the grid such that each row, column, and 3x3 subgrid 
# contains the numbers 1-9 exactly once. In other words, no row may contain 
# the same digit more than once, no column may contain the same digit more 
# than once, and none of the 9 3x3 subgrids may contain the same digit more 
# than once. Your input for this problem will always be a partially filled 9x9 
# twodimensional array that represents a solvable Sudoku puzzle. 

def isvalid(n, board, row, col):
    # element is in same row
    if n in board[row]:
        return False
    # element is in same coloumn
    for i in range(9):
        if board[i][col] == n:
            return False

    rbox = row//3*3
    cbox = col//3*3
    # element in current box
    for i in range(rbox, rbox+3):
        for j in range(cbox, cbox+3):
            if board[i][j] == n:
                return False
    return True

def nextempty(board, l):
    # find the next empty space
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                l[0], l[1] = row, col
                return True
    return False

def solveSudoko(board):
    l = [0,0]    # for storing row and col
    # if no empty space is there then the board is solved
    if not nextempty(board, l):  
        return True              
    row, col = l[0], l[1]
    for n in range(1,10): 
        # check if number will be valid at this position           
        if isvalid(n, board, row, col):
            board[row][col] = n
            # check if we get true from recursive calls
            if solveSudoko(board):
                return True
            # backtracking, again set to zero
            board[row][col] = 0
    # if can't insert any number then return false
    return False      

def sudoko(board):
    if solveSudoko(board):
        print(board)
    else:
        print("can't be solved")

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7],
]
sudoko(board)