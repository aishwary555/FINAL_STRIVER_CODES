def max_balloons(text):
    
    dict = {'b':0,'a':0,'l':0,'o':0,'n':0}
    balloon = "balloon"
    
    for ch in text:
        if ch in balloon:
            dict[ch] += 1 

    return min(dict['b'],dict['a'],dict['l']//2 , dict['o']//2 ,dict['n'])

text = "balloon"
res = max_balloons(text)
print(res)