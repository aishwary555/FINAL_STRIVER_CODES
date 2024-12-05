class StockSpanner(object):

    def __init__(self):
        self.stock = []

    def next(self, price):
        self.stock.append(price)
        count = 0
        for i in range(len(self.stock)-1,-1,-1):
            if self.stock[i] <= price:
                count+=1
            else:
                break
        return count

obj = StockSpanner()
print(obj.next(100))
print(obj.next(80))
print(obj.next(60))
print(obj.next(70))
print(obj.next(60))
print(obj.next(75))
print(obj.next(85))

