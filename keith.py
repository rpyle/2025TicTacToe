import random
team_name = 'keith'
strategy_name = 'Reference'
strategy_description = 'Check all combos for wincon; otherwise, Next Open.'

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])
  print(print_board)
 
def move(player, board, score):
    r = 0
    c = 0
    ready = False
    if player == "X":
        enemy = "O"
    else:
        enemy = "X"
    s = 0
    strat_list = [[board[0][0],board[0][1],board[0][2]], # 0 north
                  [board[0][2],board[1][2],board[2][2]], # 1 east
                  [board[2][0],board[2][1],board[2][2]], # 2 south
                  [board[0][0],board[1][0],board[2][0]], # 3 west
                  [board[0][1],board[1][1],board[2][1]], # 4 vertical
                  [board[1][0],board[1][1],board[1][2]], # 5 horizontal
                  [board[0][0],board[1][1],board[2][2]], # 6 dexter
                  [board[0][2],board[1][1],board[2][0]]] # 7 sinister
    rowfinder = [[0,0,0],
                 [0,1,2],
                 [2,2,2],
                 [0,1,2],
                 [0,1,2],
                 [1,1,1],
                 [0,1,2],
                 [0,1,2]]
    while ready == False and s != 7:
        line = strat_list[s][0]+strat_list[s][1]+strat_list[s][2]
        detect = line.find(enemy)
        aim = line.find(" ")
        if detect == -1:
            if aim != -1:
                ready = True
                s = 0
                r = rowfinder[s][aim]
                c = aim
                return r, c
            else:
                s += 1
        else:
            s += 1
    if s == 7:
        while board[r][c] != ' ':
          c = c + 1
          if c > 2:
            c = 0
            r = r + 1
        return r, c