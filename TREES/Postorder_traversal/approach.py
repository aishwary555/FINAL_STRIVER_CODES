class Node:
    def __init__(self,val,lefts = None,rights = None):
        self.left = lefts
        self.right = rights
        self.data = val
        
def postorder(root,arr):
    
    if root is None:
        return 
    
    postorder(root.left,arr)
    postorder(root.right,arr)
    arr.append(root.data)

def post_order(root):
    arr = []
    postorder(root,arr)
    return arr

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

res = post_order(root)


for val in res: 
    print(val , end = " ")
print()