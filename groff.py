import random
team_name = 'groff'
strategy_name = 'Line, Random'
strategy_description = 'Try to get the final column, and then go random.'

Iteration = 1

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])
  print(print_board)

def move(player, board, score):
  global Iteration
  r = 0
  c = 2
  while board[r][c] != ' ':
    if Iteration < 4:
      r = r + 1
      Iteration = Iteration + 1
      if c > 2:
        c = 0
        r = r + 1
      if r > 2: 
        r = 0

    else:
      r = random.randint(0,2)
      c = random.randint(0,2)
      Iteration = Iteration + 1
    


  
  return r, c