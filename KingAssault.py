import numpy as np


board = np.zeros((8,8))
wPieces = []
bPieces = []

#done
def validKnight(x,y,c):
    moves = []
    temp = []
    for i in range(-2,5,4):
        for j in range(-1,2,2):
            if 0 <= i + x <= 8 and 0 <= j + y <= 8:
                temp.append([i+x,j+y])
            if 0 <= i + y <= 8 and 0 <= j + x <= 8:
                temp.append([j+x,i+y])
    for i in temp[:]:
        if c and not(i in wPieces):
            moves.append(i)
        elif not(c) and not(i in bPieces):
            moves.append(i)
    print(moves)
    return moves[:]

#need add color
def validRook(x,y,c):
    moves = []
    for xl in range(x-1, -1,-1):
        if x == 0:
            break
        if [xl,y] in wPieces:
            break
        elif [xl,y] in bPieces:
            moves.append([xl,y])
            break
        else:
            moves.append([xl,y])
    for xr in range(x+1, 8):
        if x == 7:
            break
        if [xr,y] in wPieces:
            break
        elif [xr,y] in bPieces:
            moves.append([xr,y])
            break
        else:
            moves.append([xr,y])
    for yu in range(y-1, -1, -1):
        if y == 0:
            break
        if [x,yu] in wPieces:
            break
        elif [x,yu] in bPieces:
            moves.append([x,yu])
            break
        else:
            moves.append([x,yu])
    for yd in range(y+1, 8):
        if y == 7:
            break
        if [x,yd] in wPieces:
            break
        elif [x,yd] in bPieces:
            moves.append([x,yd])
            break
        else:
            moves.append([x,yd])
    return moves[:]

def validBishop():
    return 0

#need add color
def validPawn(x,y,c,d):
    moves = []
    if not([x,y-d] in wPieces):
        moves.append([x,y-d])
        if (y == 6 and d == 1) or (y == 1 and d == -1):
            moves.append([x,y-(d*2)])
    for i in range(-1, 2, 2):
        if [x+i,y-d] in wPieces:
            moves.append([x+i,y-d])
    return moves[:]

#need add color
def validKing(x,y,c):
    moves = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i != 0 or j != 0) and not([i+x,j+y] in wPieces):
                moves.append([i+x,j+y])
    return moves

def validQueen():
    return 0

wPieces.append([3,5])
bPieces.append([0,0])
moves = validKing(2,4,1)
for i in moves:
    board[i[0]][i[1]] = 1

print(board)
