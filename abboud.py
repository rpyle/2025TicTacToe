import random
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
  r = 1
  c = 1
  if board[r][c] == ' ':
    return r, c
  
  r = 0 
  c = 0
  if board[r][c] == ' ' and board [1][1] == player:
    return r, c
  if board [r][c] == player and board [1][1] == player:
    r = 2
    c = 2
    if board[r][c] == ' ':
        return r, c
  
  r = 0 
  c = 2
  if board[r][c] == ' ' and board [1][1] == player:
    return r, c
  if board [r][c] == player and board [1][1] == player:
    r = 2
    c = 0
    if board[r][c] == ' ':
        return r, c

  r = 0 
  c = 1
  if board[r][c] == ' ' and board [1][1] == player:
    return r, c
  if board [r][c] == player and board [1][1] == player:
    r = 2
    c = 1
    if board[r][c] == ' ':
        return r, c

  r = 1 
  c = 0
  if board[r][c] == ' ' and board [1][1] == player:
    return r, c
  if board [r][c] == player and board [1][1] == player:
    r = 1
    c = 2
    if board[r][c] == ' ':
        return r, c    

  while board[r][c] != ' ':
    r = random.randint(0,2)
    c = random.randint(0,2)

  return r, c