from collections import deque
class MyQueue(object):

    def __init__(self):
        self.dq = deque()

    def push(self, x):
        self.dq.append(x)
        

    def pop(self):
        x = self.dq.popleft()
        return x

    def peek(self):
        return self.dq[0]
        

    def empty(self):
        return len(self.dq) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()