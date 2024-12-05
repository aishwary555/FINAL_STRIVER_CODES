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


def sum_of_minimum_of_sub_array(arr):
    
    pse_ele = pse(arr)
    nse_ele = nse(arr)
    
    sum = 0
    n = len(arr)
    MOD = 10**9 + 7  # To prevent overflow issues

    
    for i in range(n):
        left = i - pse_ele[i]
        right = nse_ele[i] - i
        sum += (left*right)*arr[i]
        sum %= MOD  # Ensure result does not overflow
    return sum

arr = [3,1,2,4]
res = sum_of_minimum_of_sub_array(arr)
print(res)