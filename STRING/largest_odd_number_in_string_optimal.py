def largestOddNumber(num):

        n = len(num)
        ans = n-1
        while(ans >= 0 and int(num[ans])%2 == 0):
            ans -= 1
        
        if ans < 0:
            return ""

        return num[:ans+1]

input = "32148"
result = largestOddNumber(input)
print(result)
        
            
        

        