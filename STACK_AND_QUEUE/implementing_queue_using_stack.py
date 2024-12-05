class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    
    def push(self,x):
        self.s1.append(x)
        return x
    
    def pop(self):
        while self.s1:
            self.s2.append(self.s1.pop())
        return self.s2.pop()
    
    def peek(self):
        while self.s1:
            self.s2.append(self.s1.pop())
        return self.s2[-1]
    
    def empty(self):
        return len(self.s1) == 0 and len(self.s2) == 0

q = Queue()
print(q.push(1))
print(q.push(5))
print(q.push(8))
print(q.peek())
print(q.pop())
print(q.peek())
print(q.pop())
print(q.peek())