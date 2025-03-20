team_name = 'gans'
strategy_name = 'middle next'
strategy_description = 'Play center then the next open spot.'

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
    c = c + 1
    if c > 2:
      c = 0
      r = r + 1
      if r > 2:
        r=0
  print (r,c)
  return r, c