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

def check_palindrom(head):
    temp = head 
    st = []
    while temp is not None :
        st.append(temp.data)
        temp = temp.next 
        
    temp = head
    while temp is not None:
        if(temp.data != st.pop()):
            return False
        temp = temp.next
    return True

def print_ll(head):
    temp = head
    while temp is not None:
        print(temp.data)
        temp = temp.next
    print()

l1 = convert_arr_to_ll([1,2,2,1])
print_ll(l1)
k = check_palindrom(l1)
print(k)