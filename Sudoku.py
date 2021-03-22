# This program given an unfinished sudoku board will correctly solve the sudoku board
import random

# here is the default board, later I will implement a method to randomize a board to play with
board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]

# use this board to insert your own values and use the board above for the 
# randomization method
custom_board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]


# need to print the board so we can visualize the sudoku board appropriately
def sudoku_print(board):
    print(" ")
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print(" ")
        for j in range(9):
            if j == 8:
                print(board[i][j])
            elif j % 3 == 0 and j != 0:
                print(" ", end="")
                print(board[i][j], end="")
            else:
                print(board[i][j], end= "")
    print(" ")



# need a function to find the next available position to test
def find_next_available_position(board):
    # loop through the board and find the first position in the 
    # board that has a 0
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i , j)
    return None




def is_num_valid(board, num, position):
    # check the row to see if num is valid
    for i in range(9):
        if num == board[position[0]][i]:
            return False
    # check the column to see if the num is valid
    for j in range(9):
        if num == board[j][position[1]]:
            return False
    # check the 3x3 box to see if the num is valid
    # this will give us the x and y coordinate for what box
    # we want to search. there are only 9 boxes total
    xbox = position[1] // 3
    ybox = position[0] // 3

    for i in range(ybox * 3, ybox* 3 + 3):
        for j in range(xbox * 3, xbox * 3 + 3):
            if num == board[i][j]:
                return False

    return True


def sudoku_solve_board(board):
    # find next available position
    next_position = find_next_available_position(board)
    #the board is not finished so there is an open spot
    if next_position:
        row, column = next_position
    else:
        #this means the board has been finished. return true
        return True
    # since there is an open spot in the board, try numbers 1-9 until you find 
    # a valid number and if no answers are valid go back to the previous open spot and try again
    for i in range (1, 10):
        if is_num_valid(board, i, (row, column)):
            board[row][column] = i
            if sudoku_solve_board(board):
                return True

        board[row][column] = 0

    return False

''' this is a future function that solves the board using a different method than my 
    first back tracking method
def sudoku_solve_by_every_number(board):
    # while board is not completed
    while(find_next_available_position(board)):
        next_position = find_next_available_position(board)'''
        

''' The problem with this randomization is that it often generates boards where the numbers placed inside
    do not violate any of the rules, however the board is simply an unsolvable board. I set the second for loop
    for in range(4) to try to minimize the amount of boards that are unsolvable '''
def randomize_sudoku_board(board):
    ''' go through each row 3-4 times and place a valid number that does not violate
    the rules of the game.'''
    '''I could make this method better by assuring that the board that is generated is a solvable board'''
    for i in range(9):
        for _ in range(4):
            random_number =  random.randint(1, 9)
            random_position = random.randint(0,8)
            if is_num_valid(board, random_number, (i, random_position)):
                board[i][random_position] = random_number
    return board
                






sudoku_print(board)
#sudoku_solve_board(board)
board = randomize_sudoku_board(board)
sudoku_print(board)
sudoku_solve_board(board)
sudoku_print(board)
