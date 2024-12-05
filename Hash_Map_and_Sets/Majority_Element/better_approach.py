def majorityElement(nums):

    hash = {}
    ans = -1
    key = -1

    for num in nums:
        if num in hash:
            hash[num] += 1
        else:
            hash[num] = 1
        
    for num,count in hash.items():
        if count > ans:
            ans = count
            key = num

    #print(hash)
    return key


arr = [2,2,1,1,1,2,2]
res = majorityElement(arr)
print(res)
