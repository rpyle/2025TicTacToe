team_name = 'Fialkowski'
strategy_name = 'corner fill then win'
strategy_description = 'Places in three corners first, then chooses an open edge on the 4th turn.'

def print_board(board):
    print(board[0][0] + '|' + board[0][1] + '|' + board[0][2])
    print('-+-+-')
    print(board[1][0] + '|' + board[1][1] + '|' + board[1][2])
    print('-+-+-')
    print(board[2][0] + '|' + board[2][1] + '|' + board[2][2])

def move(player, board, score):
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    edges   = [(0, 1), (1, 0), (1, 2), (2, 1)]
    
    moves_made = 0
    for r in range(3):
        for c in range(3):
            if board[r][c] == player:
                moves_made += 1
    
    if moves_made < 3:
        for (r, c) in corners:
            if board[r][c] == ' ':
                return (r, c)
    
    if moves_made == 3:
        Winning_lines = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)]
        ]
        for line in Winning_lines:
            spot_in_winning_line = 0
            winning_spot = None #no value in spot then snipe it 
            for (r, c) in line:
                if board[r][c] == player:
                    spot_in_winning_line += 1
                elif board[r][c] == ' ':
                    winning_spot = (r, c)
            if spot_in_winning_line == 2 and winning_spot is not None:
                return winning_spot
        
        # if winning spots are blocked. 
        for (r, c) in edges:
             if spot_in_winning_line == 2 and winning_spot is not None:
                return winning_spot
    return(1,1)

 