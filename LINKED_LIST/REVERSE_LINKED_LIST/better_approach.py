# Definition for singly-linked list.
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

def reverseList(head):
        
    temp = head
    prev = None

    while temp is not None:
        front = temp.next
        temp.next = prev
        prev = temp 
        temp = front
    return prev
    
def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()
    
print("Original Linked List:", end=" ")
arr = [1,3,2,4]
a = convert_arr_to_ll(arr)
print_linked_list(a)
print("Reversed Linked List:", end=" ")
b = reverseList(a)
print_linked_list(b)
