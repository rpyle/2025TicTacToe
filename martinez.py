import random

team_name = 'martinez'
strategy_name = '4 Corners Random'
strategy_description = 'Play corners if possible, then random.'

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
  while board[r][c] != ' ':
    if board[0][0] == ' ':
      r = 0
      c = 0
    elif board[2][0] == ' ':
      r = 2
      c = 0
    elif board[0][2] == ' ':
      r = 0
      c = 2
    elif board[2][2] == ' ':
      r = 2
      c = 2

    r = random.randint(0,2)
    c = random.randint(0,2)  
  
  return r, c