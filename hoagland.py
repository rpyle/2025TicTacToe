team_name = 'hoagland'
strategy_name = 'Corner'
strategy_description = 'Play the corner spot.'

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])
  print(print_board)
board = [[' ', ' ', ' '],
           [' ', ' ', ' '],
           [' ', ' ', ' ']]
'(0,1) (0,1) (0,2), (1,0) (1,2) (1,2), (2,0) (2,1) (2,2)'
priority_moves = [(1, 1),  # Center
                  (0, 0), (0, 2), (2, 0), (2, 2),  # Corners
                  (0, 1), (1, 0), (1, 2), (2, 1)]  # Edges

def move(player, board, score):

  for r, c in priority_moves:
    if board[r][c] == ' ':
      return r,c # Return the first empty spot based on the strategy

  return r, c