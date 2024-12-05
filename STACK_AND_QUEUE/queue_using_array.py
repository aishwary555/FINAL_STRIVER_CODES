class Queue:
    def __init__(self):
        self.start = -1
        self.end = -1
        self.current_size = 0
        self.maxsize = 4
        self.arr = [0]*self.maxsize
    
    
    def push(self,x):
        if(self.current_size == self.maxsize):
            print("Queue is Full")
            exit(1)
            
        if(self.current_size == 0):            #self.current_size == 0 or self.end == -1  
            self.end = 0
            self.start = 0
        else:
            self.end = (self.end + 1)%self.maxsize
        
        self.arr[self.end] = x
        print("the element pushed is ",x)
        self.current_size += 1
    
    def pop(self):
        if(self.start == -1):
            print("Queue is empty ")
            exit(1)
        popped_element = self.arr[self.start]
        
        if(self.current_size == 1):                        # self.current_size == 1 (dont't do self.end == 0,then it wouldm't work properly because when element will come after taking rotation end = (end+1)%maxsize it would handle that scenario)
            self.end = -1
            self.start = -1
        else:
            self.start = (self.start + 1) % self.maxsize
        self.current_size -= 1
        print("element whihc is popped is ",popped_element)
        

    def top(self):
        if(self.start == -1):
            print("Queue is Empty")
            exit(1)
        return self.arr[self.start]
    
    def size(self):
        return self.current_size
    
    
if __name__ == "__main__":
    q = Queue()
    q.push(4)
    q.push(14)
    q.push(24)
    q.push(34)
    print("The peek of the queue before deleting any element", q.top())
    print("The size of the queue before deletion", q.size())
    q.pop()
    print("The peek of the queue after deleting an element", q.top())
    print("The size of the queue after deleting an element", q.size())
    q.pop()
    q.pop()
    q.push(99)
    q.push(88)
    q.pop()
    q.pop()
    print("The peek of the queue after deleting any element", q.top())
    
            
                          