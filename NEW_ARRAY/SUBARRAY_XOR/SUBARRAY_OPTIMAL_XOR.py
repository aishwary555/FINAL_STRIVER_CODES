
def subarraysWithXorK(a,k):
    n = len(a) # size of the given array.
    xr = 0
    mpp = {} # declaring the dictionary.
    mpp[xr] = 1 # setting the value of 0.
    cnt = 0

    for i in range(n):
        # prefix XOR till index i:
        xr = xr ^ a[i]

        # By formula: x = xr^k:
        x = xr ^ k

        # add the occurrence of xr^k
        # to the count:
        cnt += mpp.get(x,0)

        # Insert the prefix xor till index i
        # into the dictionary:
        if(xr in mpp):
            mpp[xr] += 1
        else:
            mpp[xr] = 1

    return cnt


a = [4, 2, 2, 6, 4]
k = 6
ans = subarraysWithXorK(a, k)
print("The number of subarrays with XOR k is:", ans)


