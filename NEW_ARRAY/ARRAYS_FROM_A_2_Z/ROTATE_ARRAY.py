def rotate(arr):
    
    temp = [0] * len(arr) 
    for i in range(1,len(arr)):
        temp[i-1] = arr[i]
    temp[len(arr)-1] = arr[0]
    
    for i in range(len(temp)):
        print(temp[i])

arr = [1,2,3,4,5]
k = rotate(arr)

        