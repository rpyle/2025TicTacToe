team_name = 'sarmiento'
strategy_name = 'Double Down'
strategy_description = 'Make last call have a win either way.'

import random

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])
  print(print_board)

def move(player, board, score):
  r = 0
  c = 0
  if board[r][c] != ' ':
    c = c + 2
    r = r
    if board[r][c] != ' ':
      r = 1
      c = 1
      if board[r][c] != ' ':
        r = 0
        c = 0
      if board[r][c] != ' ':
        r = 2
        c = c
        while board[r][c] != ' ':
          r = random.randint(0,2)
          c = random.randint(0,2)
  return r, c