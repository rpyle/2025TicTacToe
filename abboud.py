team_name = 'Abboud'
strategy_name = 'Middle-Slash'
strategy_description = 'Play the next open spot.'

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
  while board[r][c] != ' ':
    c = c - 1
    if c < 0:
      c = 2
      r = r - 1
  
  return r, c