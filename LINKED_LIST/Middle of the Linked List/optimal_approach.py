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

def mid_ll(head):
    slow = head
    fast = head
    while fast!=None and fast.next!=None:
        slow = slow.next
        fast = fast.next.next
    return slow 

def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()


# Print the original linked list
print("Original Linked List:", end=" ")
a = convert_arr_to_ll([1,2,3,4,5])
print_linked_list(a)

# Reverse the linked list
mid_ele = mid_ll(a)

# Print the reversed linked list
print("Middle Element of the Linked List:", end=" ")
print_linked_list(mid_ele)