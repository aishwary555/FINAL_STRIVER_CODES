from collections import deque

class Stack:
    
    def __init__(self):
        self.st = deque()
        self.min_stack = deque()

    def push(self, val):
        self.st.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        

    def pop(self):

        x = self.st.pop()
        if x == self.min_stack[-1]:
            self.min_stack.pop()
        return x

    def top(self):
        
        a = self.st[-1]
        return a 

    def getMin(self):
        
        if self.min_stack :
            return self.min_stack[-1]
        return -1
        

obj = Stack()

obj.push(1)
obj.push(2)
obj.push(4)
print(obj.pop())
print(obj.getMin())
