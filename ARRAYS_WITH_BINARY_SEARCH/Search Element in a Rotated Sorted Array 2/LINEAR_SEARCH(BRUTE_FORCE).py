
def search(arr , k):
    n = len(arr)
    for i in range(n):
        if arr[i] == k:
            return i
    return -1


arr = [7, 8, 9, 1, 2, 3, 4, 5, 6]
k = 1
ans = search(arr , k)
if ans == -1:
    print("Target is not present.")
else:
    print("The index is:", ans)


