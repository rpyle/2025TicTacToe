team_name = 'coon'
strategy_name = 'MCS'
strategy_description = 'It playes the middle, then the corners, and then the sides'

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
  rlist = [2, 1, 0, 1, 2, 2, 0, 0]
  clist = [1, 2, 1, 0, 2, 0, 2, 0]

  while board[r][c] != ' ':
    r = rlist.pop()
    c = clist.pop()
  return r, c