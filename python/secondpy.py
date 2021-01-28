def winCheck(board,playerSymbol):
    flag = 1
    for i in range(len(board)):
        if board[i][i] != playerSymbol:
            flag = 0
    if flag:
        return 1
    flag = 1
    for i in range(len(board)):
        if board[i][len(board)-i-1] != playerSymbol:
            flag = 0
    if flag:
        return 1
    flag = 1
    for i in range(len(board)):
        for j in range(len(board)):
            if all(board[i][j] == playerSymbol):
                return 1
    for i in range(3):
        for j in range(3):
            if all(board[j][i]==playerSymbol):
                return 1
    return 0
board = [
        [1,1,1],
        [0,0,0],
        [0,0,0]
        ]

playerSymbol = 1
print(winCheck(board,playerSymbol))