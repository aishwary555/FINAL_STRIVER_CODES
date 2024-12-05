from collections import Counter
def isAnagram(s,t):
        if len(s) != len(t):
            return False

        s_dict = Counter(s)
        t_dict = Counter(t)

        if(s_dict == t_dict):
            return True
        return False

s = "anagram"
t = "nagaram"
res = isAnagram(s,t)
print(res)