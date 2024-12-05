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

def add_two_ll(head1,head2):
    
    dummy_node = Node(-1)
    temp = dummy_node
    carry = 0
    h1 = head1
    h2 = head2
    while(h1 != None or h2 != None) :
        sum = 0 
        if(h1 != None):
            sum += h1.data
            h1 = h1.next
        if(h2 != None):
            sum += h2.data
            h2 = h2.next
    
        sum += carry
        carry = sum//10
        new_node = Node(sum%10)
        temp.next = new_node
        temp = new_node
    if carry > 0:
        temp.next = Node(carry)
        
    
    return dummy_node.next

def print_ll(head):
    temp = head
    while temp is not None:
        print(temp.data)
        temp = temp.next
    print()

l1 = convert_arr_to_ll([2,4,8,1])
l2 = convert_arr_to_ll([1,3,3,6,1,1])
print_ll(l1)
print_ll(l2)
res = add_two_ll(l1,l2)
print_ll(res)
    
    