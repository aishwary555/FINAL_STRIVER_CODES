def next_smaller_ele(nums):
    
    n = len(nums)
    st = []
    sme = [0] * n
    for i in range(n-1,-1,-1):
        
        while(st and nums[i] <= st[-1]):
            st.pop()
            
        if(st):
            sme[i] = st[-1]
        else: 
            sme[i] = -1
        
        st.append(nums[i])
    return sme


s = [9,8,5,0,6,2]
res = next_smaller_ele(s)
print(res)