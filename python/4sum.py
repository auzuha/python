arr = [1,2,3,4,5,6,7,8,9,10]
sum4 = 10;
map=[]
ct = 0
for i in range(len(arr)-3):
    sum = 0
    for j in range(i,i+4):
        sum += arr[j]
    if sum == sum4:
        #map.append([])
        map.append(arr[i:i+4])
        ct+=1
print(map)