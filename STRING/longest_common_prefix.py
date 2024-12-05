def longestCommonPrefix(strs):
 
        pre = strs[0]

        for string in strs:
            while not string.startswith(pre):
                pre = pre[:-1]
        return pre 
    
strs = ["flower","flow","flight"]
res = longestCommonPrefix(strs)
print(res)