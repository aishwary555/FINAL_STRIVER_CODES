def next_great_elements(num1 , num2):
    
    st = []
    great_next_ele = {}
    for num in reversed(num2):
        
        while st and num >= st[-1]:
            st.pop()
        
        if(st):
            great_next_ele[num] = st[-1]
        else:
            great_next_ele[num] = -1

        st.append(num)
        
    return [great_next_ele[num] for num in num1]

nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(next_great_elements(nums1, nums2)) 
        