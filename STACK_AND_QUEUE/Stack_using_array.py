class Stack:
    def __init__(self):
        self.top = -1
        self.size = 1000
        self.arr = [0]*self.size
    
    def push(self,x):
        self.top += 1
        self.arr[self.top] = x
    
    def pop(self):
        x = self.arr[self.top]
        self.top -= 1
        return x
    
    def Top_Element(self):
        return self.arr[self.top]
    
    def Size_of_Stack(self):
        return self.top + 1

# Directly creating an instance of Stack and calling methods
s = Stack()
s.push(6)
s.push(3)
s.push(7)
# stk :-> [6,3,7] 
print("Top of stack is before deleting any element", s.Top_Element())
print("Size of stack before deleting any element", s.Size_of_Stack())
print("The element deleted is", s.pop())
print("Size of stack after deleting an element", s.Size_of_Stack())
print("Top of stack after deleting an element", s.Top_Element())
        
    
     
        