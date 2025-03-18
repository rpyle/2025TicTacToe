team_name = 'coon'
strategy_name = 'Last Open'
strategy_description = 'Play the last open spot.'
import random

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])
  print(print_board)

def move(player, board, score):
  r = 2
  c = 2
  l = 1
  cornerlist = [0, 2]

  while board[r][c] != ' ':
    c = random(cornerlist)
    r = random(cornerlist)
    l = l + 1
    if l > 10:
      c = random 
  
  return r, c