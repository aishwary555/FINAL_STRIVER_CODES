class Node:
    def __init__(self, data1 ,next_node = None):
        self.data = data1
        self.next = next_node

def convert_arr_to_ll(arr):
    head = Node(arr[0])
    prev = head
    for i in range(1,len(arr)):
        temp = Node(arr[i])
        prev.next = temp
        prev = temp
    return head  

def merger_two_ll(head1,head2):
    
    dummy_node = Node(-1)
    temp = dummy_node
    h1 = head1
    h2 = head2
    
    while h1 is not None and h2 is not None :
        if(h1.data <= h2.data):
            temp.next = h1
            h1 = h1.next
        else:
            temp.next = h2
            h2 = h2.next
        temp = temp.next
    
#    while h1 is not None:
#        temp.next = h1
#        h1 = h1.next
#        temp = temp.next
#    while h2 is not None:
#        temp.next = h2
#        h2 = h2.next
#        temp = temp.next
    
    if h1 is not None:
        temp.next = h1  # Attach all remaining nodes from h1
    else:
        temp.next = h2  # Attach all remaining nodes from h2
    return dummy_node.next
    
def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()

l1 = convert_arr_to_ll([2,4,8,10])
l2 = convert_arr_to_ll([1,3,3,6,11,14])
print_linked_list(l1)
print_linked_list(l2)
res = merger_two_ll(l1,l2)
print_linked_list(res)