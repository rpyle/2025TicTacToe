team_name = 'Wilson'
strategy_name = 'Corners than side'
strategy_description = 'Go to each corner that is availible than to each side'

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])
  print(print_board)

def move(player, board, score):
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    sides = [(0, 1), (1, 0), (1, 2), (2, 1)]
    
    corners = [(r, c) for r, c in corners if board[r][c] == ' ']
    if corners:
        return corners[0]  
    
    sides = [(r, c) for r, c in sides if board[r][c] == ' ']
    if sides:
        return sides[0]  
    

    if board[1][1] == ' ':
        return 1, 1
    

    
    return 0, 0 