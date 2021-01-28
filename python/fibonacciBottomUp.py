a = [1,1]
n=5
def fibBottomUp(n,a):
    for i in range(n-2):
        t = a[0] + a[1]
        a[0] = a[1]
        a[1] = t
    print(a[1])
fibBottomUp(n,a)