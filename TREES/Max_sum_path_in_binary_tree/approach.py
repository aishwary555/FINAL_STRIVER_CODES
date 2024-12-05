class Tree:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.data = val

def find_maxpath_sum(root,maxi):
    
    if root is None:
        return 0 
    
    left_Max = max(0,find_maxpath_sum(root.left,maxi))
    right_Max = max(0,find_maxpath_sum(root.right,maxi))
    
    maxi[0] = max(maxi[0], left_Max+right_Max+root.data)
    
    return max(left_Max,right_Max) + root.data

def maxpath_sum(root):
    maxi = [float('-inf')]
    find_maxpath_sum(root,maxi)
    return maxi[0]

root = Tree(-10)
root.left = Tree(9)
root.right = Tree(20)
root.right.left = Tree(15)
root.right.right = Tree(7)

res = maxpath_sum(root)
print(res)
