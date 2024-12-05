def pse(arr):
    
    n = len(arr)
    st = []
    pse = [0] * n
    for i in range(n):
        
        while st and arr[st[-1]] > arr[i] :
            st.pop()
        
        if(st):
            pse[i] = st[-1]
        else:
            pse[i] = -1
        
        st.append(i)
    return pse

def nse(arr):
    
    n = len(arr)
    nse = [0] * n
    st = []
    
    for i in range (n-1,-1,-1):
        
        while st and arr[st[-1]] >= arr[i] :
            st.pop()
        
        if(st):
            nse[i] = st[-1]
        else:
            nse[i] = n
        st.append(i)
        
    return nse   

def pge(arr):
    
    n = len(arr)
    st = []
    pge = [0] * n
    for i in range(n):
        
        while st and arr[st[-1]] < arr[i] :
            st.pop()
        
        if(st):
            pge[i] = st[-1]
        else:
            pge[i] = -1
        
        st.append(i)
    return pge

def nge(arr):
    
    n = len(arr)
    nge = [0] * n
    st = []
    
    for i in range (n-1,-1,-1):
        
        while st and arr[st[-1]] <= arr[i] :
            st.pop()
        
        if(st):
            nge[i] = st[-1]
        else:
            nge[i] = n
        st.append(i)
        
    return nge 

def subarray_ranges(arr):
    
    pse_ele = pse(arr)
    nse_ele = nse(arr)
    n = len(arr)
    MOD = 10**9 + 7
    sum_of_subarray_min = 0
    pge_ele = pge(arr)
    nge_ele = nge(arr)
    sum_of_subarray_max = 0
    
    for i in range(n):
        left = i - pse_ele[i]
        right = nse_ele[i] - i
        sum_of_subarray_min += (left*right)*arr[i]
        #sum_of_subarray_min %= MOD
        
        lefti = i - pge_ele[i]
        righti = nge_ele[i] - i
        sum_of_subarray_max += (lefti*righti)*arr[i]
        #sum_of_subarray_max %= MOD
        
    result = sum_of_subarray_max - sum_of_subarray_min
    
    return result

arr = [1,4,3,2]
res = subarray_ranges(arr)
print(res)
        

    
        
        
        