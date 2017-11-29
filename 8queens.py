from random import randint

maxValues=[]



def swap(a,b,c,d):
    board[a][b]=0
    board[c][d]=1

def findMax(board):
    maxValues.append(max(board[0]))
    maxValues.append(max(board[1]))
    maxValues.append(max(board[2]))
    maxValues.append(max(board[3]))
    maxValues.append(max(board[4]))
    maxValues.append(max(board[5]))
    maxValues.append(max(board[6]))
    maxValues.append(max(board[7]))
    return max(maxValues)

def printBoard(board1):
    print("  0, 1, 2, 3, 4, 5, 6, 7")
    print("0"+str(board1[0]))
    print("1"+str(board1[1]))
    print("2"+str(board1[2]))
    print("3"+str(board1[3]))
    print("4"+str(board1[4]))
    print("5"+str(board1[5]))
    print("6"+str(board1[6]))
    print("7"+str(board1[7]))

def findCoordinates(value,attackBoard):
    for i in range(0, 8):
        for k in range(0, 8):
            if(attackBoard[i][k]==value):
                return i,k

def findNearestFreeSpace(a,b,attackBoard):
    attacksOnMovableSquares = []
    for i in range(0, 8):
        for k in range(0, 8):
            if (((k - i) == (a - b) or (i + k) == (a + b)) and board[i][k] == 0 and i != b and k != a):
                attacksOnMovableSquares.append(attackBoard[i][k])
            elif (i == b and board[i][k] == 0 and k != a):
                attacksOnMovableSquares.append(attackBoard[i][k])
            elif (k == a and board[i][k] == 0 and i != b):
                attacksOnMovableSquares.append(attackBoard[i][k])
    for i in range(0, 8):
        for k in range(0, 8):
            if (((k - i) == (a - b) or (i + k) == (a + b)) and board[i][k] == 0 and i != b and k != a):
                if(attackBoard[i][k]==min(attacksOnMovableSquares)):
                    return i,k
            elif (i == b and board[i][k] == 0 and k != a):
                if (attackBoard[i][k] == min(attacksOnMovableSquares)):
                    return i, k
            elif (k == a and board[i][k] == 0 and i != b):
                if (attackBoard[i][k] == min(attacksOnMovableSquares)):
                    return i, k



def attacksOnSquare(b,a):
    ctr = 0
    for i in range(0, 8):
        for k in range(0, 8):
            if(((k-i)==(a-b) or (i+k)==(a+b)) and board[i][k]==1 and i!=b and k!=a ):
                ctr+=1
            elif(i==b and board[i][k]==1 and k!=a):
                ctr+=1
            elif(k==a and board[i][k]==1 and i!=b):
                ctr+=1
    return (ctr)

def findQueenCoordinate(queensX, queensY, attackBoard):
    queenValues = []
    for i in range(0,8):
         queenValues.append(attackBoard[queensX[i]][queensY[i]])
    for k in range(0,8):
         if (attackBoard[queensX[k]][queensY[k]]== max(queenValues)):
             return queensX[k],queensY[k]


board = [[] for _ in range(8)]

for i in range(0,8):
    for k in range(0,8):
        board[i].append(0)


for i in range(0,8):
    a=randint(0, 7)
    board[i][a]=1


def loop():
    printBoard(board)
    queensX = []
    queensY = []
    attackBoard = [[] for _ in range(8)]
    for i in range(0, 8):
        for k in range(0, 8):
            if (board[i][k] == 1):
                queensX.append(i)
                queensY.append(k)
    placedQueenCtr=0
    for i in range(0, 8):
        for k in range(0, 8):
            attackBoard[i].append(attacksOnSquare(i, k))
            if(attackBoard[i][k]==0):
                placedQueenCtr+=1
    if placedQueenCtr==8:
      return 1
    a, b = findQueenCoordinate(queensX,queensY,attackBoard)
    printBoard(attackBoard)




    a0, b0 = findNearestFreeSpace(a, b,attackBoard)
    board[a][b] = 0
    board[a0][b0] = 1

    printBoard(board)
    print("son")
    print("Yerlestirilebilen toplam queen sayisi:" +str(placedQueenCtr))
#for i in range(0,65):
 #   loop()
stopper=0
ctr=0
while (stopper!=1 and ctr<100):
      stopper=loop()
      ctr+=1
a=input()