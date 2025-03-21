team_name = 'Denaut'
strategy_name = 'vertical then random'
strategy_description = 'it goes from top right to top right then random afterwards or the next open spot from the bottom right upwards.'
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
  c = 2
  while board[r][c] != ' ':
    r = 0
    x = 0 
    c = 2
    
    while x < 2:
      r = r + 1 
      x = x + 2
      while x <= 2 < 8:
         r = random.randint(0,2)
         c = random.randint(0,2)
         x = x + 1
    
    
  return r, c