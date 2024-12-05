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

def delete_nth_node_from_end(head,N):
    
    cnt = 0
    temp = head
    while temp is not None:
        cnt+=1
        temp = temp.next
    
    if(cnt == N):
        newhead = head.next
        head = None
        return newhead
    
    else:
        res = cnt - N
        temp = head
        while temp is not None:
            res = res - 1
            if(res == 0):
                break
            temp = temp.next
        
        del_node = temp.next
        del_node = None
        temp.next = temp.next.next
    
    return head
        
        

def print_ll(head):
    temp = head
    while temp is not None:
        print(temp.data)
        temp = temp.next
    print()

l1 = convert_arr_to_ll([2,4,8,1])
print_ll(l1)
k = delete_nth_node_from_end(l1,1)
print_ll(k)