class Node:
    def __init__(self,val):
        self.data = val 
        self.right = None 
        self.left = None


def inorder(root,arr):
    
    if root is None:
        return 
    
    inorder(root.left,arr)
    
    arr.append(root.data)
    
    inorder(root.right,arr)
    
def in_order(root):
    
    arr = []
    inorder(root,arr)
    return arr

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.right = Node(6)
root.left.left.right.left = Node(7)

res = in_order(root)


for val in res: 
    print(val , end = " ")
print()
    
    