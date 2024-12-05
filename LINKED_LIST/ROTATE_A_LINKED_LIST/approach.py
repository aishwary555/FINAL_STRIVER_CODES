class Node(object):
    def __init__(self, data1, next=None):
        self.data = data1
        self.next = next

def convert_arr_to_ll(arr):   
    head = Node(arr[0])
    prev = head
    for i in range(1,len(arr)):
        temp = Node(arr[i])
        prev.next = temp
        prev = temp
    return head

def kth_nodes(head,k):
    temp = head 
    while temp is not None and k > 0:
        k -= 1
        if(k == 0):
            break
        temp = temp.next
    return temp


def rotate_ll(head,k):
    tail = head
    count = 1
    while tail.next is not None:
        count += 1
        tail = tail.next
    
    if(k % count == 0):
        return head
    k = k % count
    
    kth_node = kth_nodes(head,count-k)
    tail.next = head
    head = kth_node.next
    
    kth_node.next = None
    return head

def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()
    
    
print("Original Linked List:", end=" ")
arr = [1,2,3,4,5]
a = convert_arr_to_ll(arr)
print_linked_list(a)
res = rotate_ll(a,2)
print("The Rotated List")
print_linked_list(res)