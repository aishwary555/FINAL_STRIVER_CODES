class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
        
def depth_of_binary_tree(root):
    
    if root is None:
        return 0 
    left_depth = depth_of_binary_tree(root.left)
    right_depth = depth_of_binary_tree(root.right)
    return max(left_depth,right_depth)+1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(9)
root.left.right.right.left = Node(100)

res = depth_of_binary_tree(root)
print(res)
    