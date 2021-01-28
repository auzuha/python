H = [21,3,6][::-1]
B = [20,15,5,7,10,4,2,1,3,6,8]
cap = [i for i in range(len(H),0,-1)]
sol = [0 for i in range(len(B))];
for i in range(len(B)):
    for j in range(len(H)):
        if (B[i] <= H[j]) and (cap[j] > 0):
            #ball in
            #print("in")
            cap[j] -= 1
            sol[i] = len(H) - j
            break
print(sol)