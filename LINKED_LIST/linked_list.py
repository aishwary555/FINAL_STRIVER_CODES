class Node:
    def __init__(self, data,next_node = None):
        self.data = data
        self.next = next_node

def convert_arr_to_sll(arr):
    # Create the head node with the first element of the array
    head = Node(arr[0])
    prev = head
    
    # Iterate through the rest of the array to create and link nodes
    for i in range(1, len(arr)):
        temp = Node(arr[i])
        prev.next = temp
        prev = temp
    
    return head

def print_sll(head):
    while head is not None:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

# Example usage
arr = [1, 2, 3]
head = convert_arr_to_sll(arr)
print("Singly Linked List:")
print_sll(head)
