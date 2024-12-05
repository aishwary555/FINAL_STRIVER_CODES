def removeDuplicates(nums):
    a = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[a]:
            a += 1
            nums[a] = nums[i]
    return a + 1

if __name__ == "__main__":
    arr = [1, 1, 2, 2, 2, 3, 3]
    k = removeDuplicates(arr)
    arr = arr[:k]  # Slicing the array to only keep the unique elements
    print(k)       # No. of elements present in the array  
    print("The array after removing duplicate elements is:")
    print(arr)
