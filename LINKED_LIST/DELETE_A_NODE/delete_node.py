class Node:
    def __init__(self,val,next = None):
        self.next = next
        self.data = val
        
        
def convert_arr_to_ll(arr):
        head = Node(arr[0])
        prev = head
        for i in range(1,len(arr)):
            temp = Node(arr[i])
            prev.next = temp
            prev = temp
        return head


def deleteNode(head ,val):
    temp = head 
    prev = None
    
    if(temp.data == val):
        head = temp.next
        temp = None
        return head
    
    while temp is not None:
        if(temp.data == val):
            prev.next = temp.next
            temp = None
            break
        prev = temp
        temp = temp.next
    return head
    
def print_ll(head):
    temp = head
    while temp is not None:
        print(temp.data)
        temp = temp.next
    print()
    

l1 = convert_arr_to_ll([2, 4, 8, 1])
print("Original list:")
print_ll(l1)

k = deleteNode(l1,8)
print("\nAfter deleting 1:")
print_ll(k)

k = deleteNode(l1,4)
print("\nAfter deleting 4:")
print_ll(k)