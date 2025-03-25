team_name = 'Prum'
strategy_name = 'strafe'
strategy_description = 'check each spot to see which one will create a straight line'

def move(player, board, score):
    for r in range(3):
        for c in range(3):
            if board[r][c] == ' ':
                if c > 2:
                  c = 0
                  r = r + 1
                return r, c  # Return the first available move



