
def threeSum(nums): 
        st = set()
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if(nums[i]+nums[j]+nums[k] == 0):
                        temp = [nums[i],nums[j],nums[k]]
                        temp.sort()
                        st.add(tuple(temp))
        
        ans = [list(item) for item in st]
        return ans 
    
arr = [-1, 0, 1, 2, -1, -4]

ans = threeSum(arr)
for it in ans:
    print("[", end="")
    for i in it:
        print(i, end=" ")
    print("]", end=" ")
print("\n")