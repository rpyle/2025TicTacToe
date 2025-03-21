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
    check = 0 # to make sure it doesn't check forever
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
    # print(strat_list)
    while ready == False and check != 10:
        s = random.randint(0,7) # pick one at random--if you detect a non-empty, non-player token in that line, switch over
        line = strat_list[s][0]+strat_list[s][1]+strat_list[s][2]
        # print(s)
        # print(line)
        detect = line.find(enemy)
        aim = line.find(" ")
        # print(detect)
        # print(aim)
        if detect == -1:
            # print("No opponent pieces found.")
            if aim != -1:
                # print("Location found!")
                ready = True
                check == 0
                r = rowfinder[s][aim]
                c = aim
                # print("Setting token at", r, c)
                return r, c
            else:
                # print("No empty spots. Switching strategies...")
                check += 1
        else:
            # print("Opponent found. Switching strategies...")
            check += 1
    if check == 10:
        # print("No available wins. Switching to Next Open...")
        while board[r][c] != ' ':
          c = c + 1
          if c > 2:
            c = 0
            r = r + 1
        return r, c
