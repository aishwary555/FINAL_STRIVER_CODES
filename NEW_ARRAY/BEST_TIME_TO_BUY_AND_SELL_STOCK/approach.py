def maxProfit(prices):
        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                currentProfit=prices[right] - prices[left]
                max_profit = max(max_profit, currentProfit)   
            else:
                left = right
            right += 1
        return max_profit
    
prices = [7,1,5,3,6,4]
res = maxProfit(prices)
print(res)
