class TreeNode:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.data = val

def iterative_postorder(root):
    
    ans = []
    st1 = []
    st2 = []
    
    st1.append(root)
    
    while st1:
        
        node = st1.pop()
        st2.append(node)

        if(node.left):
            st1.append(node.left)
        if(node.right):
            st1.append(node.right)   
        
    while st2:
        des = st2.pop()
        ans.append(des.data)
    return ans

# Creating a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
            
# Getting the preorder traversal
result = iterative_postorder(root)

# Displaying the preorder traversal result
print("Postorder Traversal:", end=" ")
for val in result:
    print(val, end=" ")
print()
        
        
        
        
        
        
        