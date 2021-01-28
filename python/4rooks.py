board = []
for i in range(4):
    board.append([])
    for j in range(4):
        board[i].append(0)
def isAttacked(board,x,y,n):
    if n==0:
        print(board)
        print()
        return
    for i in range(4):
        if board[x][i] == 1:
            return True
        if board[i][y] == 1:
            return True
    return False
n=4

for i in range(4):
    for j in range(4):
        if not(isAttacked(board,i,j,n)):
            board[i][j] = 1
            n -= 1
            #continue
        else:
            board[i][j] = 0