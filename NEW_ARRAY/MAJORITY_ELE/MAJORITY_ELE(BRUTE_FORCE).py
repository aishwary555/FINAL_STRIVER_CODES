def majorityElement(nums):
        ls = []
        n = len(nums)
        for i in range(n):
            if(len(ls) == 0 or ls[0]!=nums[i]):
                count = 0
                for j in range(n):
                    if(nums[j] == nums[i]):
                        count+=1
                
                if count > (n//3):
                    ls.append(nums[i])

            if(len(ls) == 2):
                break
        return ls

            

arr = [2, 2, 1, 1, 1, 2, 2]
ans = majorityElement(arr)
print("The majority element is:", ans)