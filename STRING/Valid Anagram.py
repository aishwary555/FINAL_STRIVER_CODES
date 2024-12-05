def isAnagram(s, t):
        
        freq = [0] * 26

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            freq[ord(s[i]) - ord('a')] += 1
            freq[ord(t[i]) - ord('a')] -= 1
        
        for i in freq:
            if i != 0:
                return False
        
        return True
        
s = "anagram"
t = "nagaram"
res = isAnagram(s,t)
print(res)