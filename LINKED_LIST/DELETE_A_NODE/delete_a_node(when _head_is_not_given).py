class Node(object):
    def __init__(self, x):
        self.data = x
        self.next = None
        
def convert_arr_to_ll(arr):
        head = Node(arr[0])
        prev = head
        for i in range(1,len(arr)):
            temp = Node(arr[i])
            prev.next = temp
            prev = temp
        return head

def deleteNode(node):
        
        node.data = node.next.data         #[4 -> 1 -> 1 -> 9]
        node.next = node.next.next       #[4 -> 1 -> 9]
        
        
def print_ll(head):
        temp = head
        while temp is not None:
            print(temp.data)
            temp = temp.next
        print() 

l1 = convert_arr_to_ll([2,4,8,1])
node = l1.next.next 
print_ll(l1)
k = deleteNode(node)
print_ll(l1)
    
    
        
        


        