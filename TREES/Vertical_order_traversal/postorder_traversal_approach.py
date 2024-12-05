from collections import defaultdict

class Node:
    def __init__(self,val):
        self.data = val
        self.left = None 
        self.right = None

nodes = defaultdict(lambda: defaultdict(lambda: set()))

def postorder_treaversal(root,x,y):
    
    if root is None:
        return 
    
    postorder_treaversal(root.left,x-1,y+1)
    postorder_treaversal(root.right,x+1,y+1)
    nodes[x][y].add(root.data)
    
def vertical_order_traversal(root):
    
    postorder_treaversal(root,0,0)
    
    ans = []
    for x , y_vals in sorted(nodes.items()):
        col = []
        for y,values in sorted(y_vals.items()):
            col.extend(sorted(values))
        ans.append(col)
    
    return ans
 
def printResult(result):
    for level in result:
        for node in level:
            print(node, end=" ")
        print()
    print() 

        
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(10)
root.left.left.right = Node(5)
root.left.left.right.right = Node(6)
root.right = Node(3)
root.right.right = Node(10)
root.right.left = Node(9)

result = vertical_order_traversal(root)
printResult(result)
