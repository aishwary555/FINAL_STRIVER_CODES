# can only be done by pre order approach (not by postorder or inorder) 
# because it takes first root then left and right

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.data = val 

def recursion_left(root,res,level):
    
    if root is None:
        return

    if(len(res) == level):
        res.append(root.data)
        
    recursion_left(root.left,res,level+1)
    recursion_left(root.right,res,level+1)
    
def recursion_right(root,res,level):
    
    if root is None:
        return 

    if(len(res) == level):
        res.append(root.data)
        
    recursion_right(root.right,res,level+1)
    recursion_right(root.left,res,level+1)
    
def leftside_view(root):
    res = []
    recursion_left(root,res,0)
    return res 

def rightside_view(root):
    res = []
    recursion_right(root,res,0)
    return res


        
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(10)
root.left.left.right = Node(5)
root.left.left.right.right = Node(6)
root.left.left.right.right.left = Node(9)
root.right = Node(3)
root.right.right = Node(10)


result = leftside_view(root)
result1 = rightside_view(root)

print(result)
print(result1)
    