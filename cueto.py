import random
team_name = 'cueto'
strategy_name = '50/50 cats game'
strategy_description = 'tries to capture the opponent in a cat game.'

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
  if board[r][c] != ' ':
    c = c-2
    r = r-2
    if board[r][c] != ' ':
      r= 0
      c= 2
      if board[r][c] != ' ':
        r=1
        c=1
        if board[r][c] != ' ':
          r= 0
          c= 1
          if board[r][c] != ' ':
            r= 1
            c= 2
            while board[r][c] != ' ':
              r = random.randint(0,2)
              c = random.randint(0,2)
  return r, c


