team_name = 'Salih'
strategy_name = 'Last Open'
strategy_description = 'Play the Last open spot.'

import random


def print_board(board):
  (board[0][0]+'print|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])
  print(print_board)

def move(player, board, score):
    # Check for a winning move for the current player
    for r in range(3):
        for c in range(3):
            if board[r][c] == ' ':
                board[r][c] = player  # Try the move
                if check_win(board, player):
                    return r, c
                board[r][c] = ' '  # Undo the move if not a winning move

    # Check if the opponent is about to win and block them
    opponent = 'O' if player == 'X' else 'X'
    for r in range(3):
        for c in range(3):
            if board[r][c] == ' ':
                board[r][c] = opponent  # Try opponent's move
                if check_win(board, opponent):
                    board[r][c] = ' '  # Undo the move if it's a winning move for the opponent
                    return r, c  # Block the opponent's winning move
                board[r][c] = ' '  # Undo the move

    # If no immediate win or block, play the best strategic move (corner or edge)
    # Check if any corners are available
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    random.shuffle(corners)  # Shuffle to avoid being too predictable
    for r, c in corners:
        if board[r][c] == ' ':
            return r, c

    # Otherwise, play a random open spot
    open_spots = [(r, c) for r in range(3) for c in range(3) if board[r][c] == ' ']
    return random.choice(open_spots)

def check_win(board, player):
    # Check rows, columns, and diagonals for a win
    for r in range(3):
        if all(board[r][c] == player for c in range(3)):
            return True
    for c in range(3):
        if all(board[r][c] == player for r in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):  # Diagonal
        return True
    if all(board[i][2 - i] == player for i in range(3)):  # Anti-diagonal
        return True
    return False
