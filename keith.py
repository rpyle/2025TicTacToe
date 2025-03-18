import random
team_name = 'keith'
strategy_name = 'Center then Random'
strategy_description = 'Play center if available, then random'

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])
  print(print_board)
 
def move(player, board, score):
  r = 1
  c = 1

  while board[r][c] != ' ':
    r = random.randint(0,2)
    c = random.randint(0,2)
  
  return r, c