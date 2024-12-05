def maxDepth(s):
        
        stk = []
        ans = 0 
        for x in s:
            if x == '(' :
                stk.append(x)
            elif (x == ')') and stk and stk[-1] == '(':
                ans = max(ans,len(stk))
                stk.pop()
        return ans

s = "(1) + ((2)) + (((3)))"
res = maxDepth(s)
print(res)