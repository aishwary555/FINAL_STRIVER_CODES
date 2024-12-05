def frequencySort(s):
        
        freq_dict = {}
        for i in range(len(s)):
            if(s[i] in freq_dict):
                freq_dict[s[i]] += 1
            else:
                freq_dict[s[i]] = 1
        
        sorted_chars = sorted(freq_dict.keys(),key = lambda x:freq_dict[x],reverse=True)
        result = []
        for char in sorted_chars:
            result.append(char*freq_dict[char])

        return ''.join(result)
    
a = "treesssssss"
res = frequencySort(a)
print(res)
        