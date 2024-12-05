class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.data = val

def check_balanced_BT(root):
    
    if root is None:
        return True
    
    left_height = find_depth(root.left)
    right_height = find_depth(root.right)
    
    if abs(left_height - right_height) > 1:
        return False
    root_left = check_balanced_BT(root.left)
    root_right = check_balanced_BT(root.right)
    return root_left and root_right
 
def find_depth(root):
    if root is None:
        return 0
    left_depth = find_depth(root.left)
    right_depth = find_depth(root.right)
    return max(left_depth,right_depth)+1


# Creating a sample binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
root.right.left = Node(7) 

res = check_balanced_BT(root)
print(res)