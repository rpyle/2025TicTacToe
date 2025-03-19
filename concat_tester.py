import random as r
test_board = [['X', 'O', ' '],
              [' ', ' ', 'O'],
              ['X', ' ', 'X']]
#north = test_board[0][0]+test_board[1][0]+test_board[2][0]
#east = test_board[2][0]+test_board[2][1]+test_board[2][1]
#south = test_board[2][0]+test_board[2][1]+test_board[2][1]
#west = test_board[0][0]+test_board[0][1]+test_board[0][1]
#vertical = test_board[0][1]+test_board[1][1]+test_board[2][1]
#horizontal = test_board[1][0]+test_board[1][1]+test_board[1][2]
#dexter = test_board[0][0]+test_board[1][1]+test_board[2][2]
#sinister = test_board[2][0]+test_board[1][1]+test_board[0][2]
def placeholder(player, board, score):
    ready = False
    if player == "X":
        enemy = "O"
    else:
        enemy = "X"
    check = 0 # to make sure it doesn't check forever
    strat_list = [[board[0][0],board[1][0],board[2][0]], # 0 north
                  [board[2][0],board[2][1],board[2][1]], # 1 east
                  [board[2][0],board[2][1],board[2][1]], # 2 south
                  [board[0][0],board[0][1],board[0][1]], # 3 west
                  [board[0][1],board[1][1],board[2][1]], # 4 vertical
                  [board[1][0],board[1][1],board[1][2]], # 5 horizontal
                  [board[0][0],board[1][1],board[2][2]], # 6 dexter
                  [board[2][0],board[1][1],board[0][2]]] # 7 sinister
    rowfinder = 0
    while ready == False and check != 7:
        s = r.randint(0,7) # pick one at random--if you detect a non-empty, non-player token in that line, switch over
        line = strat_list[s][0]+strat_list[s][1]+strat_list[s][2]
        print(s)
        print(line)
        detect = line.find(enemy)
        aim = line.find(" ")
        print(detect)
        print(aim)
        if detect == -1:
            print("No opponent pieces found.")
            if aim != -1:
                print("Location found!")
                ready = True
            else:
                print("No empty spots. Switching strategies...")
        else:
            print("Opponent found. Switching strategies...")
            check += 1
    if check == 7:
        print("No available wins. Switching to random...")
placeholder('X',test_board,0)