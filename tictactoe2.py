import pygame, sys
import numpy as np

pygame.init()

# CONSTANTS:
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLUMNS = 3
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55

# RGB Color Codes:
RED = (255, 0, 0)
BG_COLOR = (0, 0, 0)
LINE_COLOR = (168, 173, 180)
CIRCLE_COLOR = (127, 128, 62)
CROSS_COLOR = (204, 154, 82)

# SCREEN:
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption( 'TIC TAC TOE' )
screen.fill( BG_COLOR )

# board:
board = np.zeros( (BOARD_ROWS, BOARD_COLUMNS) )

# pygame.draw.line( screen, LINE_COLOR, (10,10), (300,300), 10 )

def draw_lines():
    # 1 horizontal:
    pygame.draw.line( screen, LINE_COLOR, (0,200), (600,200), LINE_WIDTH )
    # 2 horizontal:
    pygame.draw.line( screen, LINE_COLOR, (0,400), (600,400), LINE_WIDTH )

    # 1 vertical:
    pygame.draw.line( screen, LINE_COLOR, (200,0), (200,600), LINE_WIDTH )
    # 2 vertical:
    pygame.draw.line( screen, LINE_COLOR, (400,0), (400,600), LINE_WIDTH )

def draw_figures():
    for row in range( BOARD_ROWS ):
        for col in range( BOARD_COLUMNS ):
            if board[row][col] == 1:
                pygame.draw.circle( screen, CIRCLE_COLOR, (int(col * 200 + 100), int(row * 200 + 100)), CIRCLE_RADIUS, CIRCLE_WIDTH )
            elif board[row][col] == 2:
                pygame.draw.line( screen, CROSS_COLOR, (col * 200 + SPACE, row * 200 + 200 - SPACE), (col * 200 + 200 - SPACE, row * 200 + SPACE), CROSS_WIDTH )
                pygame.draw.line( screen, CROSS_COLOR, (col * 200 + SPACE, row * 200 + SPACE), (col * 200 + 200 - SPACE, row * 200 + 200 - SPACE), CROSS_WIDTH )
def mark_square(row, col, player):
    board[row][col] = player

def square_available(row, col):
    return board[row][col] == 0

def board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLUMNS):
            if board[row][col] == 0:
                return False
    return True



draw_lines()


player = 1


# mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:


            mouseX = event.pos[0] # x
            mouseY = event.pos[1] # y
            
            clicked_row = int(mouseY // 200)
            clicked_col = int(mouseX // 200)
            
            if square_available( clicked_row, clicked_col ):
                if player == 1:
                    mark_square( clicked_row, clicked_col, 1 )
                    player = 2

                elif player == 2:
                    mark_square( clicked_row, clicked_col, 2 )
                    player = 1
                
                draw_figures()


    pygame.display.update()
