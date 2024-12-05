def findMedianSortedArrays(nums1, nums2 , b):
        
        n1 = len(nums1)
        n2 = len(nums2)
        n = n1 + n2
        k = b - 1
        ele = -1
        count = 0
        i,j = 0,0
        while i<n1 and j<n2:
            if (nums1[i]<nums2[j]):
                if(count == k):
                    ele = nums1[i]
                count+= 1
                i = i+1
            else:
                if(count == k):
                    ele = nums2[j]
                
                count += 1
                j += 1

        while i<n1:
                if(count == k):
                    ele = nums1[i]
                count+= 1
                i = i+1

        while j<n2:
            if(count == k):
                ele = nums2[j]
            count += 1
            j += 1
        
        return ele 
            
a = [1,3, 4, 7, 10, 12]
b = [2, 3, 6, 15]
res = findMedianSortedArrays(a,b,10)
print(res)






        