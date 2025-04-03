team_name = 'Johnson'
strategy_name = 'Next Open from top right corner' 
strategy_description = 'Play the next open spot from the top right corner.'

def move(player, board, score):
  r = 2
  c = 0
  while board[r][c] != ' ':
    
    c = c + 1
    if c > 2:
      c = 0
      r = r + 1
    if r > 2:
      r = 0
  if board[r][c] == ' ':    
    return r, c
  else:
    c = c + 1
    if c > 2:
      c = 0
      r = r + 2
    if r > 2:
      r = 0
  return r, c