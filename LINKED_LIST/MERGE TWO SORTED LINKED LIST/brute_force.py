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

def merge_two_sorted_ll_into_arr(head1,head2):
    arr = []
    temp1 = head1
    temp2 = head2
    while temp1 is not None:
       arr.append(temp1.data)
       temp1 = temp1.next
       
    while temp2 is not None : 
        arr.append(temp2.data)
        temp2 = temp2.next
    arr.sort()
    return arr

def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()

l1 = convert_arr_to_ll([2,4,8,10])
l2 = convert_arr_to_ll([1,3,3,6,11,14])
print_linked_list(l1)
print_linked_list(l2)
res = merge_two_sorted_ll_into_arr(l1,l2)
result = convert_arr_to_ll(res)
print_linked_list(result)