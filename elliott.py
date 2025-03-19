team_name = 'elliott'
strategy_name = 'Open'
strategy_description = 'Play the center then next open spot.'

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
  if board[r][c] != ' ':
    c = 0
    r = 0
    while board[r][c] != ' ':
      c = c + 1
      if c > 2:
        c = 0
        r = 2
        if board[r][c] != ' ':
          c = 0
          r = 0
          while board[r][c] != ' ':
            c = c + 1
            if c > 2:
              c = 0
              r = r + 1
  
  return r, c