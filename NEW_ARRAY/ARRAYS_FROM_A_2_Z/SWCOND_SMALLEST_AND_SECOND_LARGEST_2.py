
def getElements(arr, n):
    if n == 0 or n == 1:
        print(-1, -1)  # edge case when only one element is present in array
        
    small = min(arr)
    large = max(arr)
 
    
    print(small)
    print(large)
    
    arr.remove(large)
    arr.remove(small)
    
    print(f"Second largest element {max(arr)}")
    print(f"Second smalles element {min(arr)}")
    
    
    
    




if __name__ == '__main__':
    arr = [1, 2, 4, 6, 7, 5]
    n = len(arr)
    getElements(arr, n)


