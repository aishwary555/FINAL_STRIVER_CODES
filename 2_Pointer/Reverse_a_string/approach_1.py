def reverseString(s):
        
    res = []
    for i in range(len(s) - 1, -1 , -1):
        res.append(s[i])
    return res

s = ["h","e","l","l","o"]
res = reverseString(s)
print(res)