arr = [[11,2,4],
       [4,5,6],
       [10,8,-12]]
N = 3

diag1 = 0
diag2 = 0
for i in range(N):
    for j in range(N):
        if i == j:
            diag1 += arr[i][j]
        if i+j == N-1:
            diag2 += arr[i][j]

        
print(abs(diag1-diag2))