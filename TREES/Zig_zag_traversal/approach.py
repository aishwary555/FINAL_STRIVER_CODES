from collections import deque

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val

def zig_zag(root):
    
    ans = []
    
    if not root:
        return ans
    
    q = deque()
    q.append(root)
    flag = 0  # 0 means left-to-right, 1 means right-to-left
    
    while q:
        size = len(q)
        level = []
        
        for i in range(size):
            if flag == 0:
                node = q.popleft()
                level.append(node.data)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            else:
                node = q.pop()
                level.append(node.data)
                if node.right:
                    q.appendleft(node.right)
                if node.left:
                    q.appendleft(node.left)
        
        ans.append(level)
        # Toggle flag for the next level
        flag = 1 - flag
    
    return ans

# Creating a sample binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

res = zig_zag(root)
print(res)
