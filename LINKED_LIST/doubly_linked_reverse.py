class Node:
    def __init__(self ,data,next_node=None ,back_node = None):
        self.data = data
        self.next = next_node
        self.back = back_node

def conver_arr_to_dll(arr):
    
    head = Node(arr[0])
    prev = head
    
    for i in range(1,len(arr)):
        temp = Node(arr[i],None,prev)
        prev.next = temp
        prev = temp 
    return head 

def print_dll(head):
    while head is not None:
        print(head.data)
        head = head.next
    print()

def reverse_dll(head):
    if head is None or head.next is None:
        return head

    st = []
    temp = head
    while temp is not None:
        st.append(temp.data)
        temp = temp.next
        
    temp = head
    while temp is not None:
        temp.data = st.pop()
        temp = temp.next
        
    return head

arr = [1,2,3,4,5]
head = conver_arr_to_dll(arr)
print("Doubly Linked List Initially : ")
print_dll(head)
print("After Reversing the Doubly Linked List : ")
reverse_dll(head)
print_dll(head)
