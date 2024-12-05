class Solution:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.data = val

def height(root,diameter):
    
    if root is None:
        return 0
    
    left = height(root.left,diameter)
    right = height(root.right,diameter)
    
    diameter[0] = max(diameter[0] , left+right) 
    
    return 1+max(left,right)

def dia(root):
    diameter = [0]
    height(root,diameter)
    return diameter[0]

root = Solution(1)
root.left = Solution(2)
root.right = Solution(3)
    
root.right.left = Solution(4)
root.right.right = Solution(7)
    
root.right.left.left = Solution(5)
root.right.left.left.left = Solution(6)
    
root.right.right.right = Solution(8)
root.right.right.right.right = Solution(9)

res = dia(root)
print(res)
