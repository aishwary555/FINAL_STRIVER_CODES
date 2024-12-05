def singleNonDuplicate(arr):
    n = len(arr)  # Size of the array
    if n == 1:
        return arr[0]

    for i in range(n):
        # Check for first index
        if i == 0:
            if arr[i] != arr[i + 1]:
                return arr[i]
        # Check for last index
        elif i == n - 1:
            if arr[i] != arr[i - 1]:
                return arr[i]
        else:
            if arr[i] != arr[i - 1] and arr[i] != arr[i + 1]:
                return arr[i]

    # Dummy return statement
    return -1

arr = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
ans = singleNonDuplicate(arr)
print("The single element is:", ans)

