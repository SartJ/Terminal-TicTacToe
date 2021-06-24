"""
OBJECTIVE:
-Building a 2 Player TIC TAC TOE game that runs on the TERMINAL/CMD.

PLANNING:
-We Take Player names as inputs.
-We randomly select a player who Starts off the game. (Tossing Phase)
-tic tac toe board will look like this, basically a 2D List
[
    [-, -, -],
    [-, -, -],
    [-, -, -]
]
-user_input = 1-9, will denote the Position where user wants to enter His/Her move on the board.
-Positions Labeled Below:

1  2  3
4  5  6
7  8  9

-If they enter anything other than 1-9: prompt(go again).
-Check if the user_input is already taken.
-Add it to the board.
-Check if the user won: checking rows, columns and diagonals.
-Toggle between users upon successful moves.

FUTURE IMPROVEMENTS:
(+) Adding GUI to it.
(+) Using classes and objects.
(+) Adding options to play against an AI. 
:D
"""
import random
import time


'''
Creating the tic tac toe board
'''
# 2D-Array containing the board data
board = [
    ['-','-','-'],
    ['-','-','-'],
    ['-','-','-']
]

# Used before the game starts, to clean the board..
def reset_board():
    b = [
        ['-','-','-'],
        ['-','-','-'],
        ['-','-','-']
    ]
    global board 
    board = b

# Used to print the current state of the board
def show_board():
    for i in board:
        for j in i:
            print(j, end = '   ')
        print()
        print()

'''
Toggle players:
'''
p1 = ''
p2 = ''
starter = '' # The player who starts
current = '' # It's his/her turn now..

# Let's know the names of the players
def get_names():
    global p1 
    p1 = input("Player 1 Name:")
    global p2 
    p2= input("Player 2 Name:")
    toss()


# Let us randomly choose the person who'll go first.
def toss():
    objects = [p1, p2]
    print('ROCKS! PAPERS! SCISSORS! ...')
    time.sleep(3)
    winner = random.choice(objects)
    global starter 
    starter = winner
    global current 
    current = starter
    print(f"{current} will start!")
    return

# This helps to toggle between player1 and player2
def toggle(c):
    global current
    if c == p1:
        current = p2
    else:
        current = p1
    

# Checks if the user input is already taken or not:
def is_empty(n):
    if board[n//3][n%3] != '-': # Thanks Aryan Rahman <3
        return False
    else:
        return True

# Whether more turns are possible or not
def game_over():
    global board
    if any('-' in x for x in board):
        return False
    else:
        return True


# Populate/Update tictactoe board's current state: Make a move.
def populate(c): 
    global p1
    if c == p1:
        return 'x'
    else:
        return 'o'

# Checks if the user has won or not:
def win_check():
    global board
    # Row-Wise win check:
    for i in board:
        num_of_x = i.count('x')
        if num_of_x == 3:
            return True
        num_of_o = i.count('o')
        if num_of_o == 3:
            return True
    # Column-Wise win check:
    for i in range(0,3):
        col = []
        for j in board:
            col.append(j[i])
        if col.count('x') == 3:
            return True
        if col.count('o') == 3:
            return True
        
    # Diagonal win check:
    x = [board[0][0], board[1][1], board[2][2]]
    y = [board[0][2], board[1][1], board[2][0]]
    if x.count('x') == 3:
        return True
    if x.count('0') == 3:
        return True
    if y.count('x') == 3:
        return True
    if y.count('o') == 3:
        return True
    return False

# Starts the game:
def start():
    reset_board()
    get_names()
    num_check = [0,1,2,3,4,5,6,7,8]
    winner_flag = False # A flag which will be turned true If someone wins 
    while(not(game_over())):
        print(f'{current} please enter your move (1-9) : ')
        # Handling non-numeric values:
        x = ''
        while True:
            x = input()
            if x.isnumeric():
                break
            else:
                print("Invalid input. Please try again (1-9).")
        tile_no = int(x)-1
        if not(tile_no in num_check):
            print("Invalid input. Try again")
        elif is_empty(tile_no):
            n = tile_no
            board[n//3][n%3] = populate(current) # Added to the board.
            #Check if the user won or not:
            if win_check():
                show_board()
                print(f"{current} has won!!")
                winner_flag = True
                break

            toggle(current)
            show_board()
        else:
            print("This Tile is not empty, try again.")
    if winner_flag:
        print("Please press 0 to play again or press 1 to Exit.")
        if int(input()) == 0:
            start()
    else:
        print("DRAW! Please press 0 to play again or press 1 to Exit.")
        if int(input()) == 0:
            start()


start()












