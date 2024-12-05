from collections import Counter
def canConstruct(ransomNote, magazine):
        
    hash = Counter(magazine)

    for ch in ransomNote:
        if hash[ch] > 0 :
            hash[ch] -= 1 
        else:
            return False
    return True

ransomnote = "aa"
magazine = "aab"
res = canConstruct(ransomnote,magazine)
print(res)    