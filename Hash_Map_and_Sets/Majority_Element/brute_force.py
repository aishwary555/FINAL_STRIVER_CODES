def majorityElement(nums):

    ans = []
    n = len(nums)
    for i in range(n):
        count = 0
        for j in range(n):
            if(nums[i] == nums[j]):
                count += 1 
        ans.append(count)
        
    max_count_index = ans.index(max(ans))
    #print(ans)
    return nums[max_count_index]

arr = [3,2,3,2,2,2,2,2,2,2,2,2]
res = majorityElement(arr)
print(res)