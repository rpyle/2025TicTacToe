team_name = 'alcantara'
strategy_name = 'The Center Corner Capture'
strategy_description = 'Take center, corners, complete series'

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])
  print(print_board)

import random
corners = [[0,0] , [0,2], [2,0], [2,2]]
midpoints = [[0,1], [1,0], [1,2], [2,1]]

def move(player, board, score): 
 #New strat below  -  "The Center Corner"
  global corners
  r = 0
  c = 0

  if board[1][1] == ' ':
    r = 1
    c = 1
    return r, c
  
  #offense
  if player == "X":
  
    while corners != 0:
      choice = random(board)
      
      
      
      else:
        # TODO

  #defense - selects a spot at random; taken from file example2.py
  else:
    while board[r][c] != ' ':
      r = random.randint(0,2)
      c = random.randint(0,2)
  
  return r, c
