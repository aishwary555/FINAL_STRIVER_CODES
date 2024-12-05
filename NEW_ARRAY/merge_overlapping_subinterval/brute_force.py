def mergeoverlapping_subinterval(arr):
    
    n = len(arr)
    ans = []
    arr.sort()
    
    for i in range(n):
        start = arr[i][0] 
        end = arr[i][1]
        
        if(ans and end <= ans[-1][1]):
            continue
        
        for j in range(i+1,n):
            if(arr[j][0] <= end):
                end = max(end,arr[j][1])
            else:
                break
        ans.append([start,end])
    
    return ans


arr = [[1, 3], [8, 10], [2, 6], [15, 18]]
ans = mergeoverlapping_subinterval(arr)
print("The merged intervals are:")
for it in ans:
    print(f"[{it[0]}, {it[1]}]", end=" ")
print()
        
        