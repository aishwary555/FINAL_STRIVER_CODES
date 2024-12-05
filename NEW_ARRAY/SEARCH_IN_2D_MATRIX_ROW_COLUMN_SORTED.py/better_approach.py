def searchElement(nums,target):
        low = 0 
        high = len(nums)-1
        while low <= high :
            mid = (low+high)//2
            if nums[mid] == target :
                return True
            elif nums[mid] < target:
                low = mid+1
            else:
                high = mid-1
        return False

def searchMatrix(matrix, target):
        
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):

            flag = searchElement(matrix[i],target)
            if flag:
                return True
        return False



matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]

result = searchMatrix(matrix, 22)
print(result)
            

    
            