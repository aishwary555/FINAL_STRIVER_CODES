from collections import defaultdict
def max_balloons(text):
    
    dict = defaultdict(int)
    balloon = "balloon"
    
    for ch in text:
        if ch in balloon:
            dict[ch] += 1 

    if any(c not in dict for c in balloon):
        return 0
    else:
        return min(dict['b'],dict['a'],dict['l']//2 , dict['o']//2 ,dict['n'])

text = "loonbalxballpoon"
res = max_balloons(text)
print(res)