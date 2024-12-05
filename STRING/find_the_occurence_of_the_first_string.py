def strStr(haystack, needle):
        
        if len(haystack) < len(needle):
            return -1
        
        i = 0
        while i < len(haystack):
            if(haystack[i:i+len(needle)] == needle):
                return i
            i = i+1
        return -1
needle = "but"
haystack = "sadbutsad"
res = strStr(haystack,needle)
print(res)
