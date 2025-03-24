import random
team_name = 'Witucki'
strategy_name = 'corners then next opean'
strategy_description = 'It will play the corners then the next opean from the begining of the board, or it will play the first boxes then the corners'

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])
  print(print_board)

def move(player, board, score):
   
   
    corners = [(0,0), (0,2), (2,0), (2,2)]
    corners = [(r,c) for r, c in corners if board [r][c] == ""]
    if corners:
        return corners[0]
    r =0
    c =0
    while board[r][c] != ' ':
      c = c + 1
      if c > 2:
        c = 0
        r = r + 1
   
   


   
 
    return r, c
