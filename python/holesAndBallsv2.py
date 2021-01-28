#Ball
#     \hn
#      \
#       \hn-2
#..
#
#..........\h1
H = [21,3,6] #h1,h2,...hn
B = [20,15,5,7,10,4,2,1,3,6,8]
cap = [i+1 for i in range(len(H))]
sol = [0 for i in B]
for i in range(len(B)):
    for j in range(len(H)-1,-1,-1):
        if B[i] <= H[j] and cap[j] > 0:
            #ball in
            sol[i] = j+1
            cap[j] -= 1
            break
print(sol)