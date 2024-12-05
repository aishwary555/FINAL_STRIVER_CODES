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

def reverse_ll(head):
    prev = None
    temp = head
    while temp is not None:
        front = temp.next
        temp.next = prev
        prev = temp 
        temp = front
    return prev

def check_palindrome(head):
    
    slow = head 
    fast = head 
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next 
    
    new_head = reverse_ll(slow.next)
    first = head
    second = new_head
    while(second is not None):
        if(first.data != second.data):
            reverse_ll(new_head)
            return False
        
        first = first.next
        second = second.next
    
    reverse_ll(new_head)    
    return True


def print_ll(head):
    temp = head
    while temp is not None:
        print(temp.data)
        temp = temp.next
    print()
    

l1 = convert_arr_to_ll([1,3,3,4,3,3,1])
print_ll(l1)
k = check_palindrome(l1)
print(k)