def rotate(arr,k):
	for j in range(k):
		temp = arr[0]
		for i in range(len(arr)-1):
			arr[i] = arr[i+1]
		arr[-1] = temp
	return arr

arr = [1,2,3]
queries = [0,1]