import random
team_name = 'pyle'
strategy_name = 'Random'
strategy_description = 'Pyle randomly plays a random open spot.'
    
def move(player, board, score):
  r = random.randint(0,2)
  c = random.randint(0,2)

  while board[r][c] != ' ':
    r = random.randint(0,2)
    c = random.randint(0,2)
  
  return r, c