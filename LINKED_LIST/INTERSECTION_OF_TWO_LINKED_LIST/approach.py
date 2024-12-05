class Node(object):
    def __init__(self, x):
        self.data = x
        self.next = None
        
def convert_arr_to_ll(arr):
        head = Node(arr[0])
        prev = head
        for i in range(1,len(arr)):
            temp = Node(arr[i])
            prev.next = temp
            prev = temp
        return head

def count_ll(head):
        temp = head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        return count

def getIntersectionNode(headA, headB):

    len_A = count_ll(headA)
    len_B = count_ll(headB)
    difference = len_A - len_B
        
    if (len_A > len_B):
        temp = headA
        for i in range(difference):
            temp = temp.next
        headA = temp
            
    else:
        temp = headB
        for _ in range(difference):
            temp = temp.next
        headB = temp
        
    t1 = headA
    t2 = headB
    while(t1 != t2):
        t1 = t1.next if t1 is not None else headB
        t2 = t2.next if t2 is not None else headA
    return t1

def print_ll(head):
        temp = head
        while temp is not None:
            print(temp.data)
            temp = temp.next
        print() 

# don't worry about code written below,that code is just to run the logic we have to give inputs,so we are creating the inputs here
#leave this part 


intersect = convert_arr_to_ll([8, 4, 5])

# Create listA: [4, 1] + [8, 4, 5]
listA = convert_arr_to_ll([4, 1])
temp = listA
while temp.next is not None:
    temp = temp.next
temp.next = intersect  # Connecting listA to the intersecting node

# Create listB: [5, 6, 1] + [8, 4, 5]
listB = convert_arr_to_ll([5, 6, 1])
temp = listB
while temp.next is not None:
    temp = temp.next
temp.next = intersect  # Connecting listB to the intersecting node

# Print both lists
print("List A:")
print_ll(listA)

print("List B:")
print_ll(listB)

# Find the intersection
intersection_node = getIntersectionNode(listA, listB)
if intersection_node:
    print(f"\nIntersected at '{intersection_node.data}'")
else:
    print("\nNo intersection found") 
    
                


        
        
                