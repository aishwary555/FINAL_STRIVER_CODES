'''from collections import Counter
def majorityElement(nums):
        
        n = len(nums)
        ls = []
        counter = Counter(nums)
        for num,count in counter.items():
            if(count > (n//3)):
                ls.append(num)
        return ls


arr = [2, 2, 1, 1, 1, 2, 2]
ans = majorityElement(arr)
print("The majority element is:", ans)           


'''




def majorityElement(nums):
        
        n = len(nums)
        ls = []
        dict = {}
        for i in nums:
            if i in dict:
                dict[i] += 1
            else :
                dict[i] = 1


        for num,count in dict.items():
            if(count > (n//3)):
                ls.append(num)
        
        print(dict)
        return ls  
                  

arr = [2, 2, 1, 1, 1, 2, 2]
ans = majorityElement(arr)
print("The majority element is:", ans)           




