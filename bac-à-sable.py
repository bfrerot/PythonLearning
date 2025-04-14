EMPTY = "-"
BROOK = "BROOK"
BPAWN = "BPAWN"
BKNIGHT = "BKNIGHT"
BBISHOP = "BBISHOP"
BQUEEN = "BQUEEN"
BKING = "BKING"
board = []
for i in range(8):
    row = [EMPTY for i in range(8)]
    print(row)
    board.append(row)
print()
print("Now let's place the the pieces")
# THE BLACKS
board[0][0] = board[0][7] = BROOK
board[0][1] = board[0][6] = BKNIGHT
board[0][2] = board[0][5] = BBISHOP
board[0][3] = BQUEEN
board[0][4] = BKING
board[1] = [BPAWN] * 8
# THE WHITES
board[7][0] = board[7][7] = BROOK
board[7][1] = board[7][6] = BKNIGHT
board[7][2] = board[7][5] = BBISHOP
board[7][3] = BQUEEN
board[7][4] = BKING
board[6] = [BPAWN] * 8

for row in board:
    print(row)