class TreeNode:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.data = val

def iterative_preorder(root):
    
    preorder = []
    
    if root is None:
        return preorder
    
    st = []
    st.append(root)
    
    while st:
        
        node = st.pop()
        preorder.append(node.data)
        
        if(node.right):
            st.append(node.right)
        
        if(node.left):
            st.append(node.left)
            
    return preorder

# Creating a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
            
# Getting the preorder traversal
result = iterative_preorder(root)

# Displaying the preorder traversal result
print("Preorder Traversal:", end=" ")
for val in result:
    print(val, end=" ")
print()
        
        
        
        
        
        
        