def previous_greater_ele(price):
    
    n = len(price)
    pge = [-1] * n 
    st = []
    ans = [0] *n
    
    for i in range(n):
    
        while st and st[-1][0] <= price[i]:
            st.pop()
    
        if(st):
            pge[i] = st[-1][0]
            ans[i] = i - st[-1][1]
        else:
            pge[i] = -1
            ans[i] = i+1 
        
        
        st.append((price[i] , i))
    return ans


s = [14,5,2,10,8]
res = previous_greater_ele(s)
print(res)
    
    
    