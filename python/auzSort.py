def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

arr = [5,4,3,2,1]
for i in range(len(arr)):    
    for j in range(i+1,len(arr)):
        if arr[j] < arr[i]:
            swap(arr,i,j)
    print(arr)
