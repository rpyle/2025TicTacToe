import random
team_name = 'dolan'
strategy_name = 'Center then next open'
strategy_description = 'Play center if available, then next available'
    
def move(player, board, score):
  r = 0
  c = 0
  while board[r][c] != ' ':
    c = c + 1
    if c > 2:
      c = 0
      r = r + 1
  
  return r, c