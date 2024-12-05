def func(mid, n, m):
    ans = 1
    for i in range(n):  # Loop from 0 to n-1
        ans *= mid
    if ans > m:
        return 2
    if ans == m:
        return 1
    return 0
def NthRoot(n, m):
    low = 1
    high = m
    while low <= high:
        mid = (low + high) // 2
        midN = func(mid, n, m)
        if midN == 1:
            return mid
        elif midN == 0:
            low = mid + 1
        else:
            high = mid - 1
    return -1

n = 3
m = 1000
ans = NthRoot(n, m)
print("The answer is:", ans)