def isIsomorphic(s, t):
            
        s_dict = {}
        t_dict = {}
        if(len(s) != len(t)):
            return False
        
        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]

            if(s_char in s_dict):
                if(s_dict[s_char] != t_char):
                    return False
            else:
                s_dict[s_char] = t_char


            if(t_char in t_dict):
                if(t_dict[t_char] != s_char):
                    return False
            else:
                t_dict[t_char] = s_char
        return True
    
s = "add"
t = "egg"
res = isIsomorphic(s,t)
print(res)
