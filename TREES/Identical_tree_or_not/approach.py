class Node:
    def __init__(self,val):
        self.left = None 
        self.right = None 
        self.data = val 

def identical_or_not(root1,root2):
    
    if(root1 is None and root2 is None):
        return True
    
    if(root1 is None or root2 is None):
        return False
    
    return (identical_or_not(root1.left,root2.left) and 
            identical_or_not(root1.right,root2.right) and
            root1.data == root2.data )
    

root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)

root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)
    
res = identical_or_not(root1,root2)
print(res)