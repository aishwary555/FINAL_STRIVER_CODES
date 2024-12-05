from collections import deque

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def iterative_dq_binarytree(root):
    
    if root is None:
        return 0

    dq = deque()
    dq.append((root,1))
    max_depth = 0 
    
    while dq:
        node,depth = dq.popleft()
        max_depth = max(max_depth,depth)
        if(node.left):
            dq.append((node.left,depth+1))
        if(node.right):
            dq.append((node.right,depth+1))
    return max_depth

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(9)
root.left.right.right.left = Node(100)

res = iterative_dq_binarytree(root)
print(res)