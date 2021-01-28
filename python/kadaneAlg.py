def kadane(arr):
    gmax = 0
    lmax = 0
    for i in range(len(arr)):
        lmax += arr[i]
        if lmax > gmax:
            gmax = lmax
        if lmax < 0:
            lmax = 0
    return gmax

print(kadane([1,2,3,4,5]))
