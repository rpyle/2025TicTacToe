team_name = 'alcantara'
strategy_name = 'The Center Corner Capture'
strategy_description = 'Capture center, take corners, complete the lines... or tie  >:) '

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])
  print(print_board)

import random

def move(player, board, score): 
 #New strat below  -  "The Center Corner"
  corners = [
    [0,0] , [0,2], [2,0], [2,2]
             ]

  r = 0
  c = 0

  #takes the center if available
  if board[1][1] == ' ':
    r = 1
    c = 1
    return r, c
  
  #offense
  if player == "X":
    #fill the gaps
    #TODO?
    
    
    #play the corners
    corners_index = 0
    while (corners_index != 4):
      location = corners[corners_index]
      row_choice = location[0]
      column_choice = location[1]
      corners_index += 1
      
      
      if board[row_choice][column_choice] == ' ':
        r = row_choice
        c = column_choice
        return r, c


  #This randomly selects an open spot
    while board[r][c] != ' ':
      r = random.randint(0,2)
      c = random.randint(0,2)
  
  return r, c
