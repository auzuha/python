
board = [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
        ]

def printSol(board):
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j],end=" ")
        print()
def isAttacked(board,i,j):
    #PROBLEM IN DIAGONAL ATTACK, DEMONSTRATED IN CURRENT BOARD STATE
    n = len(board);
    for k in range(n):
        if board[i][k] == 1:
            return True
        if board[k][j] == 1:
            return True
    for k in range(len(board)):
        for l in range(len(board)):
            if (k+l==i+j) or (k-l==i-j):
                if board[k][l] == 1:
                    return True
                    
    return False
    
def NQUEENS(N):
    global board
    global solncount
    if N == 0:
        return True
    for i in range(len(board)):
        for j  in range(len(board)):
            if not(isAttacked(board,i,j)):
                board[i][j] = 1;
                if NQUEENS(N-1):
                    return True
                board[i][j] = 0
    return False

ans = NQUEENS(4)
if ans:
    printSol(board)
else:
    print(False)