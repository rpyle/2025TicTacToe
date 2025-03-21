team_name = 'alcantara'
strategy_name = 'The Center Corner Capture'
strategy_description = 'Take center, corners, midpoints'

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

  #takes center if unoccupied
  if board[1][1] == ' ':
    r = 1
    c = 1
    return r, c
  
  #offense
  if player == "X":
    while(r == 1) and (c == 1):
      taken_corner = 0
      
      if taken_corner == 4:
        while board[row][column] != " ":
          choice = random(midpoints)
          row = choice[0]
          column = choice[1]
        
        r = row
        c = column
        return r, c
        
        #take midpoints at random
        
      elif board[row][column] == ' ':
        choice = random(corners)
        row = choice[0]
        column = choice[1]
        
        r = row
        c = column
        return r, c
      else:
        taken_corner += 1

      


  #defense - selects a spot at random; taken from file example2.py
  else:
    while board[r][c] != ' ':
      r = random.randint(0,2)
      c = random.randint(0,2)
  
  return r, c

