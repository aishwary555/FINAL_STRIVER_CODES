class Node:
    def __init__(self,val):
        self.data = val 
        self.left = None
        self.right = None 

def is_leaf(root):
    return not root.left and not root.right 

def left_boundary(root,res):
    
    curr = root.left
    while curr:
        
        if(not is_leaf(curr)):
            res.append(curr.data)
        if(curr.left):
            curr = curr.left
        else:
            curr = curr.right

def right_boundary(root,res):
    
    temp = []
    curr = root.right
    while curr:
        
        if(not is_leaf(curr)):
            temp.append(curr.data)
        if(curr.right):
            curr = curr.right
        else:
            curr = curr.left
        
    for i in range(len(temp)-1,-1,-1):
        res.append(temp[i])

def add_leaf_node(root,res):
    
    if root is None:
        return 
    if is_leaf(root):
        res.append(root.data)
    
    add_leaf_node(root.left,res)
    add_leaf_node(root.right,res)

def boundary_traversal(root):
    res = []
    if not is_leaf(root):
        res.append(root.data)
    left_boundary(root,res)
    add_leaf_node(root,res)
    right_boundary(root,res)
    
    return res

# Creating a sample binary tree
root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.left.left.right = Node(4)
root.left.left.left = Node(12)
root.left.left.right.left = Node(5)
root.left.left.right.right = Node(6)

root.right = Node(7)
root.right.right = Node(8)
root.right.right.left = Node(9)
root.right.right.left.right = Node(11)
root.right.right.left.left = Node(10)

result = boundary_traversal(root)
print(result)    