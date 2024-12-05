
def threeSum( nums):
        
        n = len(nums)
        st = set()
        for i in range(n):
            hashset = set()
            for j in range(i+1,n):
                third = -(nums[i] + nums[j])
                if third in hashset:
                    res = [nums[i],nums[j],third]
                    res.sort()
                    st.add(tuple(res))

                hashset.add(nums[j])    
                
                
                
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