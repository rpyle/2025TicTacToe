team_name = 'bowers'
strategy_name = 'center, , block and corner, lines '
strategy_description = 'Play the next o.'
import random 
def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])
  print(print_board)

def move(player, board, score):
  if player == 'X':
     other_player = 'O'
  else:
     other_player = "X"
     r = 1
     c = 1
  #if center is open
  if board[1][1] == ' ':
    r = 2
    c = 2
    if  board [1][1] ==  (player):
      if board [0][2] == ' ' or board [0][2] == player :
       r = 0
       c = 2
       if board [2][0] == ' ':
         r = 2 
         c = 0 
      if board [0][0] == ' ':
        r = 0
        c = 0 
        if board[2][2] == ' ':
          r = 2
          c = 2
  #if senter is not open
  else: 
    if board[0][0] == ' ':
      r = 0
      c = 0 
      if board[0][1] == ' ' or board[0][1] == (player)   and  board[0][2] == ' ' or board[0][2] == (player) :
        r=0
        c=1
        if board[0][2] == ' ':
          r=0
          c=2
      if board[1][0] == ' '  and board[2][0] == ' ':
        r=1
        c=0
        if board[2][0] == ' ':
          r=2
          c=2
    if board[2][2] == ' ':
      r = 2
      c = 2 
      if board[2][1] == ' ' and board[2][0] == ' ':
        r=2
        c=1
        if board[2][0] == ' ':
          r=2
          c=0
      if board[1][2] == ' ' and board[0][2] == ' ':
        r=1
        c=2
        if board[0][2] == ' ':
          r=0
          c=2
    
    
  return r, c
