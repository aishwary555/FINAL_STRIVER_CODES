class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def depth_of_binary_tree(root):
    
    if root is None:
        return 
    
    max_depth = 0
    st = []
    st.append((root,1))
    
    while st:
        node,depth = st.pop()
        if node:
            max_depth = max(max_depth,depth)
            if(node.left):
                st.append((node.left,depth+1))
            if(node.right):
                st.append((node.right,depth+1))
    return max_depth
            
    

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(9)
root.left.right.right.left = Node(100)

res = depth_of_binary_tree(root)
print(res)
    

        