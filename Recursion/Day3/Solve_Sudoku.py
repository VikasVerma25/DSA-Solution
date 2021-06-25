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
    if n in board[0]:
        return False
    # element is in same coloumn
    if n in board[:,1]:
        return False


def nextempty(board,l):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                l = [row, col]
                return True
    return False

def solveSudoko(board):
    l = []    # for storing row and col
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