team_name = 'Bennett'
strategy_name = '3 Corners'
strategy_description = 'Get 3 corners'

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
    c = c + 2
    if c > 2:
      c = 0
      r = r + 2
  
  return r, c