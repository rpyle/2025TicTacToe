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
corners = [[0,0] , [0,2], [2,0], [2,2]]
def corner_selection():
  global corners
  choice = random.randint(len(corners))
  if board(corners[choice][1],corners[choice][2]) == ' ':
    append.corners(choice)

spaces = [
          [0,0], [0,1], [0,2],

          [1,0], [1,1], [1,2],

          [2,0], [2,1], [2,2],
]
def move(player, board, score): 
 #New strat below  -  "The Center Corner"
  r = 0
  c = 0

  if board[1][1] == ' ':
    r = 1
    c = 1
    return r, c
  
  #offense
  if 
  #TODO

  #defense
  else:
    #This randomly selects an opem spot
    while board[r][c] != ' ':
    r = random.randint(0,2)
    c = random.randint(0,2)
  
  return r, c