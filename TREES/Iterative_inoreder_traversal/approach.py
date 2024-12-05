class Node:
    def __init__(self,val):
        self.data = val 
        self.right = None 
        self.left = None

def inorder(root):
    
    ans = []
    st = []
    current = root
    
    while st or current is not None:
        
        while current is not None:
            st.append(current)
            current = current.left
        
        current = st.pop()
        ans.append(current.data)
        
        current = current.right
        
    return ans

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

res = inorder(root)


for val in res: 
    print(val , end = " ")
print()
    