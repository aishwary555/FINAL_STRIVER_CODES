class stockspanner:
    def __init__(self):
        self.stack = []
        self.index = 0
        
    def next(self,price):
        
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
            
        if self.stack:
            span = self.index - self.stack[-1][1]
        else:
            span = self.index + 1
            
        self.stack.append((price,self.index))
        
        self.index += 1
        
        return span
    
# Create an instance of StockSpanner
spanner = stockspanner()

# Pass individual prices and calculate spans
print(spanner.next(14))  
print(spanner.next(5))   
print(spanner.next(2))   
print(spanner.next(10))   
print(spanner.next(8))   

            
        