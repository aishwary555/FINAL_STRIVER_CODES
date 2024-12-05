
def findMedianSortedArrays(nums1, nums2):
        
        n1 = len(nums1)
        n2 = len(nums2)
        n = n1 + n2
        ind_1 = n//2
        ind_2 = ind_1 - 1
        median_1_ind , median_2_ind = -1 , -1
        count = 0
        i,j = 0,0
        while i<n1 and j<n2:
            if (nums1[i]<nums2[j]):
                if(count == ind_1):
                    median_1_ind = nums1[i]
                if(count == ind_2):
                    median_2_ind = nums1[i]
                count+= 1
                i = i+1
            else:
                if(count == ind_1):
                    median_1_ind = nums2[j]
                if(count == ind_2):
                    median_2_ind = nums2[j]
                count += 1
                j += 1

        while i<n1:
                if(count == ind_1):
                    median_1_ind = nums1[i]
                if(count == ind_2):
                    median_2_ind = nums1[i]
                count+= 1
                i = i+1

        while j<n2:
            if(count == ind_1):
                median_1_ind = nums2[j]
            if(count == ind_2):
                median_2_ind = nums2[j]
            count += 1
            j += 1
        
        if(n%2 ==1):
            return median_1_ind
        return (median_1_ind + median_2_ind)/2.0
            
a = [1,3, 4, 7, 10, 12]
b = [2, 3, 6, 15]
res = findMedianSortedArrays(a,b)
print(res)






        