def previous_smaller_element(arr):
    pse = []
    for i in range (len(arr)):
        for j in range(i-1,-1,-1):
            if(arr[j] < arr[i]):
                pse.append(arr[j])
                break
        else:
            pse.append(-1)
    return pse

s = [4,5,2,10,8]
res = previous_smaller_element(s)
print(res)