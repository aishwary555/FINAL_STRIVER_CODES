class Solution:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.data = val
        self.diameter = 0 

    def height(self,root):
    
        if root is None:
            return 0 
        left_height = self.height(root.left)
        right_height = self.height(root.right)
    
        self.diameter = max(self.diameter,left_height+right_height)
        
        return 1+max(left_height,right_height)
    
    def dia(self,root):
        
        self.height(root)
        return self.diameter

root = Solution(1)
root.left = Solution(2)
root.right = Solution(3)
    
root.right.left = Solution(4)
root.right.right = Solution(7)
    
root.right.left.left = Solution(5)
root.right.left.left.left = Solution(6)
    
root.right.right.right = Solution(8)
root.right.right.right.right = Solution(9)


res = root.dia(root)
print(res)