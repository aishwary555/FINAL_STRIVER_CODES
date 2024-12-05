class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

def convert_arr_to_ll(arr):
    head = Node(arr[0])
    prev = head
    for i in range(1,len(arr)):
        temp = Node(arr[i])
        prev.next = temp
        prev = temp
    return head

def delete_n_th_node_from_end(head , N):
    
    slow = head
    fast = head

    for _ in range(N):
        fast = fast.next 
    
    while fast is None:
        return head.next
    
    while fast.next is not None:
        slow = slow.next 
        fast = fast.next
         
    del_node = slow.next
    slow.next = slow.next.next 
    del_node = None
    
    return head

def print_ll(head):
    temp = head
    while temp is not None:
        print(temp.data)
        temp = temp.next
    print()


l1 = convert_arr_to_ll([2,4,8,1])
print_ll(l1)
k = delete_n_th_node_from_end(l1,4)
print_ll(k)
    









def print_ll(head):
    temp = head
    while temp is not None:
        print(temp.data)
        temp = temp.next
    print()
    