team_name = 'Prouty'
strategy_name = 'Prioritize and Complete'
strategy_description = 'The strategy prioritizes the middle spot, tries to complete a line (winning/blocking), and picks random spots if necessary.'

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])
  print(print_board)

import random

def move(player, board, score):
    
    if board[1][1] == ' ':
        return 1, 1 
    for row in range(3):
        if board[row].count(player) == 2 and board[row].count(' ') == 1:
            col = board[row].index(' ')  # Find the empty spot in the row
            return row, col
        
        col_vals = [board[i][row] for i in range(3)]  # Check the column
        if col_vals.count(player) == 2 and col_vals.count(' ') == 1:
            empty_row = col_vals.index(' ')  # Find the empty spot in the column
            return empty_row, row
    
    # Check diagonals for a chance to complete a line
    diagonal1 = [board[i][i] for i in range(3)]  # Top left to bottom right diagonal
    if diagonal1.count(player) == 2 and diagonal1.count(' ') == 1:
        empty_index = diagonal1.index(' ')
        return empty_index, empty_index
    
    diagonal2 = [board[i][2-i] for i in range(3)]  # Top right to bottom left diagonal
    if diagonal2.count(player) == 2 and diagonal2.count(' ') == 1:
        empty_index = diagonal2.index(' ')
        return empty_index, 2 - empty_index

    # Pick a random available spot if no winning/blocking move
    available_spots = [(row, col) for row in range(3) for col in range(3) if board[row][col] == ' ']
    return random.cho
    ice(available_spots)  # Pick a random available spot
