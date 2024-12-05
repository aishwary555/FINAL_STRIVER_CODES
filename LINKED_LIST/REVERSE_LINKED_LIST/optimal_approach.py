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


def reverse_linked_list(head):

    if head is None or head.next is None:
        return head
    
    # Recursive step:
    new_head = reverse_linked_list(head.next)
    front = head.next
    front.next = head
    head.next = None
    return new_head

def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()


# Print the original linked list
print("Original Linked List:", end=" ")
a = convert_arr_to_ll([1,2,3,4])
print_linked_list(a)

# Reverse the linked list
reversed_ll = reverse_linked_list(a)

# Print the reversed linked list
print("Reversed Linked List:", end=" ")
print_linked_list(reversed_ll)


