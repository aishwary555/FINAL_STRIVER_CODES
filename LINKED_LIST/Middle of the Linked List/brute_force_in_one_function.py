class Node:
    def __init__(self , data1 , next_node = None):
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
        
        
def counts(head):
    cnt = 0
    temp = head
    while temp is not None:
        cnt+=1
        temp = temp.next
    
    temp = head
    mid = (cnt//2)+1
    while temp is not None:
        mid -= 1
        if mid == 0:
            break
        temp = temp.next
    return temp 



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
mid_ele = counts(a)

# Print the reversed linked list
print("Middle Element of the Linked List:", end=" ")
print_linked_list(mid_ele)
