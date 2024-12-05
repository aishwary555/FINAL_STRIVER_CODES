def previous_smaller_ele(arr):
    
    st = []
    n = len(arr)
    pse = [-1]*n
    
    for i in range(len(arr)):
        
        while st and st[-1] >= arr[i]:
            st.pop()
        
        if st :
            pse[i] = st[-1]
        else:
            pse[i] = -1
        
        st.append(arr[i])
    return pse

s = [4,5,2,10,8]
res = previous_smaller_ele(s)
print(res)
        
        
        
         