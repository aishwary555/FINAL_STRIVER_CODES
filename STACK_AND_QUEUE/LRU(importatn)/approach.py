class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRU:
    def __init__(self,capacity):
        self.cap = capacity
        self.cache = {}
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_node(self,node):
        
        temp = self.head.next
        node.next = temp
        temp.prev = node
        self.head.next = node
        node.prev = self.head
        
    def remove_node(self,node):
        
        temp = node.prev
        next_node = node.next
        temp.next = next_node
        next_node.prev = temp
    
    def get(self,key):
        if key in self.cache:
            node = self.cache[key]
            data = node.val
            self.remove_node(node)
            self.add_node(node)
            return data
        return -1
    
    def put(self,key,val):
        
        if(key in self.cache):
            node = self.cache[key]
            self.remove_node(node)
            del self.cache[key]
            
        if(len(self.cache) == self.cap):
            node = self.tail.prev
            self.remove_node(node)
            del self.cache[node.key]
        
        new_node = Node(key,val)
        self.add_node(new_node)
        self.cache[key] = new_node


lru = LRU(2)

lru.put(1, 6)  
lru.put(2, 7)  

print(lru.get(1))

lru.put(3, 8)  

print(lru.get(2))  

lru.put(4, 4)  

print(lru.get(1))  
print(lru.get(3))  
print(lru.get(4))  
        
            
                    
        
        
        