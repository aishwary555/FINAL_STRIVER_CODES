from collections import deque
class MyStack(object):

    def __init__(self):
        self.dq = deque()
        

    def push(self, x):
        
        self.dq.append(x) 


    def pop(self):
        
        x = self.dq.pop()
        return x
        

    def top(self):
        
        return self.dq[-1]
        

    def empty(self):
        
        return len(self.dq) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()