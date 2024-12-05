class Node:
    def __init__(self,val):
        self.data = val 
        self.right = None 
        self.left = None

root = Node(1)

# Creating left and right child nodes for the root node
root.left = Node(2)
root.right = Node(3)
    
# Creating a right child node for the left child node of the root
root.left.right = Node(5)
    
# Example: Print the data in the tree structure
print(f"Root: {root.data}")
print(f"Left Child of Root: {root.left.data}")
print(f"Right Child of Root: {root.right.data}")
print(f"Right Child of Left Child: {root.left.right.data}")