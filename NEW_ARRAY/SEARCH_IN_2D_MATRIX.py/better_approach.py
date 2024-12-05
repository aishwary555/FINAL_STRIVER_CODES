def binsearch(nums,target):
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

            if(matrix[i][0] <= target and target <= matrix[i][m-1]):
                return binsearch(matrix[i],target)
        return False

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
result = searchMatrix(matrix, 78)
print(result)
            
            
            
            
''' Leetcode :             

        class Solution(object):
    def binsearch(self,nums,target):
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

    def searchMatrix(self, matrix, target):
        
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):

            if(matrix[i][0] <= target and target <= matrix[i][m-1]):
                return self.binsearch(matrix[i],target)
        return False

sol = Solution()

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
result = sol.searchMatrix(matrix, 78)
print(result)
            

    
            
'''