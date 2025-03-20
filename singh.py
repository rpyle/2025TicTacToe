import random

team_name = 'Singh'
strategy_name = 'Win by rows'
strategy_description = 'It will try to win the game by having three of its symbols match horizontally.'

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])
  print(print_board)

def move(player, board, score):
  if (board[0][0] == ' ' or board[0][1] == ' ' or board[0][2] == ' '):
    c = 0
    while(c <= 2):
      if(board[0][c] == ' '):
        return 0, c
      else:
        c = c + 1
  elif (board[1][0] == ' ' or board[1][1] == ' ' or board[1][2] == ' '):
    c = 0
    while(c <= 2):
      if(board[1][c] == ' '):
        return 1, c
      else:
        c = c + 1
  elif (board[2][0] == ' ' or board[2][1] == ' ' or board[2][2] == ' '):
    c = 0
    while(c <= 2):
      if(board[2][c] == ' '):
        return 2, c
      else:
        c = c + 1