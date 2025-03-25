
team_name = 'Reeves'
strategy_name = '3 chances'
strategy_description = 'Start with the center, then take corners to create multiple winning chances.'
import random 
def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])
  print(print_board)

def move(player, board, score):

    if board[1][1] == ' ': # best spot in the game
        return 1, 1


    for r, c in [(0, 0), (0, 2), (2, 0), (2, 2)]: # Takes the cornners 
        if board[r][c] == ' ':
            return r, c


    for r, c in [(0, 1), (1, 0), (1, 2), (2, 1)]: # takes the edges 
        if board[r][c] == ' ':
            return r, c

    return random.choice([(r, c) for r in range(3) for c in range(3)]) # fall back plan hopfully beats Random Player
