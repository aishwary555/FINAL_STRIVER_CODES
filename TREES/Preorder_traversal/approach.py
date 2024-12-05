class Node:
    def __init__(self,val,lefts = None,rights = None):
        self.left = lefts
        self.right = rights
        self.data = val
        
def preorder(root,arr):
    
    if root is None:
        return 
    
    arr.append(root.data)
    preorder(root.left,arr)
    preorder(root.right,arr)
    

def pre_order(root):
    arr = []
    preorder(root,arr)
    return arr

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

res = pre_order(root)


for val in res: 
    print(val , end = " ")
print()