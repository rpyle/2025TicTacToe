import random as random

#player = 0
#score = 0
#board = [['O', ' ', ' '],
#         [' ', ' ', ' '],
#         ['X', ' ', ' ']]

team_name = 'poore'
strategy_name = 'CenterThenCheckTwosThenRandomOpen'
strategy_description = 'Play center first, then block two in a rows, then play a random open.'




def move(player, board, score):
    global r, c
    stop = 0
    if board[0][0] == ' ' and board[0][1] == ' ' and board[0][2] == ' ' and board[1][0] == ' ' and board[1][1] == ' ' and board[1][2] == ' ' and board[2][0] == ' ' and board[2][1] == ' ' and board[2][2] == ' ':
        r = 1
        c = 1
        stop = 1
    r=0
    c=0
    if board[0][0] != ' ' and stop == 0:
        occupied = board[0][0]
        if board[0][1] == occupied:
            r=0
            c=2
            if board[r][c] == ' ':
                stop = 1
    if board[0][0] != ' ' and stop == 0:
        occupied = board[0][0]
        if board[0][2] == occupied:
            r=0
            c=1
            if board[r][c] == ' ':
                stop = 1
    if board[0][0] != ' ' and stop == 0:
        occupied = board[0][0]
        if board[1][0] == occupied:
            r=2
            c=0
            if board[r][c] == ' ':
                stop = 1
    if board[0][0] != ' ' and stop == 0:
        occupied = board[0][0]
        if board[2][0] == occupied:
            r=1
            c=0
            if board[r][c] == ' ':
                stop = 1
    if board[0][0] != ' ' and stop == 0:
        occupied = board[0][0]
        if board[1][1] == occupied:
            r=2
            c=2
            if board[r][c] == ' ':
                stop = 1
    if board[0][0] != ' ' and stop == 0:
        occupied = board[0][0]
        if board[2][2] == occupied:
            r=1
            c=1
            if board[r][c] == ' ':
                stop = 1
    if board[0][1] != ' ' and stop == 0:
        occupied = board[0][1]
        if board[0][1] == occupied:
            r=0
            c=2
            if board[r][c] == ' ':
                stop = 1
    if board[0][1] != ' ' and stop == 0:
        occupied = board[0][1]
        if board[0][2] == occupied:
            r=0
            c=0
            if board[r][c] == ' ':
                stop = 1
    if board[0][1] != ' ' and stop == 0:
        occupied = board[0][1]
        if board[1][1] == occupied:
            r=2
            c=1
            if board[r][c] == ' ':
                stop = 1
    if board[0][1] != ' ' and stop == 0:
        occupied = board[0][1]
        if board[2][1] == occupied:
            r=1
            c=1
            if board[r][c] == ' ':
                stop = 1
    if board[0][2] != ' ' and stop == 0:
        occupied = board[0][2]
        if board[1][1] == occupied:
            r=2
            c=0
            if board[r][c] == ' ':
                stop = 1
    if board[0][2] != ' ' and stop == 0:
        occupied = board[0][2]
        if board[1][2] == occupied:
            r=2
            c=2
            if board[r][c] == ' ':
                stop = 1
    if board[0][2] != ' ' and stop == 0:
        occupied = board[0][2]
        if board[2][0] == occupied:
            r=1
            c=1
            if board[r][c] == ' ':
                stop = 1
    if board[0][2] != ' ' and stop == 0:
        occupied = board[0][2]
        if board[2][2] == occupied:
            r=1
            c=2
            if board[r][c] == ' ':
                stop = 1
    if board[1][0] != ' ' and stop == 0:
        occupied = board[1][0]
        if board[1][1] == occupied:
            r=1
            c=2
            if board[r][c] == ' ':
                stop = 1
    if board[1][0] != ' ' and stop == 0:
        occupied = board[1][0]
        if board[1][2] == occupied:
            r=1
            c=0
            if board[r][c] == ' ':
                stop = 1
    if board[1][0] != ' ' and stop == 0:
        occupied = board[1][0]
        if board[2][0] == occupied:
            r=0
            c=0
            if board[r][c] == ' ':
                stop = 1
    if board[1][1] != ' ' and stop == 0:
        occupied = board[1][1]
        if board[1][2] == occupied:
            r=1
            c=0
            if board[r][c] == ' ':
                stop = 1
    if board[1][1] != ' ' and stop == 0:
        occupied = board[1][1]
        if board[2][0] == occupied:
            r=0
            c=2
            if board[r][c] == ' ':
                stop = 1
    if board[1][1] != ' ' and stop == 0:
        occupied = board[1][1]
        if board[2][1] == occupied:
            r=0
            c=1
            if board[r][c] == ' ':
                stop = 1
    if board[1][1] != ' ' and stop == 0:
        occupied = board[1][1]
        if board[2][2] == occupied:
            r=0
            c=0
            if board[r][c] == ' ':
                stop = 1
    if board[1][2] != ' ' and stop == 0:
        occupied = board[1][2]
        if board[1][2] == occupied:
            r=1
            c=0
            if board[r][c] == ' ':
                stop = 1
    if board[1][2] != ' ' and stop == 0:
        occupied = board[1][2]
        if board[2][2] == occupied:
            r=0
            c=2
            if board[r][c] == ' ':
                stop = 1
    if board[2][0] != ' ' and stop == 0:
        occupied = board[2][0]
        if board[2][1] == occupied:
            r=2
            c=2
            if board[r][c] == ' ':
                stop = 1
    if board[2][0] != ' ' and stop == 0:
        occupied = board[2][0]
        if board[2][2] == occupied:
            r=2
            c=1
            if board[r][c] == ' ':
                stop = 1
    if board[2][1] != ' ' and stop == 0:
        occupied = board[2][1]
        if board[2][2] == occupied:
            r=2
            c=0
            if board[r][c] == ' ':
                stop = 1

    if stop == 0:
        while board[r][c] != ' ':
            r = random.randint(0,2)
            c = random.randint(0,2)

    return r, c

#move(player, board, score)
#print(r)
#print(c)
