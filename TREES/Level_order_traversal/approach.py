from collections import deque

class TreeNode:
    def __init__(self,val = 0):
        self.left = None
        self.right = None
        self.data = val

def level_order(root):
    
    ans = []
    if not root:
        return ans\
    
    q = deque()
    q.append(root)
    
    while q:
        
        size = len(q)
        level = []
        
        for i in range(size):
            node = q.popleft()
            level.append(node.data)
            
            if(node.left):
                q.append(node.left)
            if(node.right):
                q.append(node.right)
            
        ans.append(level)
    return ans

def printList(lst):
    # Iterate through the
    # list and print each element
    for num in lst:
        print(num, end=" ")
    print()

# Creating a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

res = level_order(root)

for level in res:
    printList(level)