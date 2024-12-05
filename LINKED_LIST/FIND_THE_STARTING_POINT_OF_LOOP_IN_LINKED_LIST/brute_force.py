class Node:
    def __init__(self ,data,next_node=None):
        self.data = data
        self.next = next_node

def find_first_node_of_loop(head):
    temp = head 
    dict_node = {}
    while temp is not None:
        if(temp in dict_node):
            return temp
        dict_node[temp] = 1
        temp = temp.next 
    return None

if __name__ == "__main__":
    # Create a sample linked list with
    # a loop for testing
    head = Node(1)
    second = Node(2)
    third = Node(88)
    fourth = Node(4)
    fifth = Node(5)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    # Create a loop
    fifth.next = third

k = find_first_node_of_loop(head)
print(k.data)
