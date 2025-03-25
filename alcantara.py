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
  
  # corners are open?
  top_left = False
  top_right = False
  bottom_left = False
  bottom_right = False
  
  if board[0][0] == player:
    top_left = True
  if board[0][2] == player:
    top_right = True
  if board[2][0] == player:
    bottom_left = True
  if board[2][2] == player:
    bottom_right = True
  
  #fill the gaps (vert, horiz)
  if (top_left) and (top_right) and (board[0][1]):
    r = 0
    c = 1
    return r, c
  elif (top_left) and (bottom_left) and (board[1][0]):
    r = 1
    c = 0
    return r, c
  elif (bottom_right) and (bottom_left) and (board[2][1]):
    r = 2
    c = 1
    return r, c
  elif (bottom_right) and (top_right) and (board[1][2]):
    r = 1
    c = 2
    return r, c
  
  
  #play the corners
  index_corners = 0
  while (index_corners != 4):
    location = corners[index_corners]
    row_choice = location[0]
    column_choice = location[1]
    index_corners += 1
    
    
    if board[row_choice][column_choice] == ' ':
      r = row_choice
      c = column_choice
      return r, c


  # this is example0.py, it serves as a backup
    r = 0
    c = 0
  while board[r][c] != ' ':
    c = c + 1
    if c > 2:
      c = 0
      r = r + 1
  
  return r, c
