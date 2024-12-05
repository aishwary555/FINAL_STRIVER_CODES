class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

def detect_loop(head):
    
    slow = head 
    fast = head
    while fast is not None and fast.next is not None:
         
        slow = slow.next 
        fast = fast.next.next 
        if(slow == fast):
            return True
         
    return False


if __name__ == "__main__":
    # Create a sample linked list with
    # a loop for testing
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    # Create a loop
    fifth.next = third

k = detect_loop(head)
print(k)