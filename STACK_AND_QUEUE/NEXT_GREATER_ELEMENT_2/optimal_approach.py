def next_great_ele(nums):
    
    n = len(nums)
    nge = [-1] *n
    st = []
    for i in range(2*n-1,-1,-1):
        while(st and  nums[i%n] >= st[-1]):
            st.pop()
            
        if(i<n):
            if(st):
                nge[i] = st[-1]
            else:
                nge[i] = -1
        st.append(nums[i%n])
    return nge

nums = [1,2,3,4,3]
res = next_great_ele(nums)
print(res)