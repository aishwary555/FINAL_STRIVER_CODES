def largestRectangleArea(heights):
        
        st = [-1]
        ans = 0 
        heights.append(0)

        for i in range(len(heights)):
            
            while( heights[i] < heights[st[-1]] ):
                
                h = heights[st.pop()]
                w = i - st[-1] - 1
                ans = max (w*h,ans)
            st.append(i)
        return ans 

heights = [2,1,5,6,2,3]
res = largestRectangleArea(heights)
print(res)




#st = [-1]: Acts as a sentinel value. It simplifies width calculations when popping from the stack because -1 represents the index before the first bar,
# allowing the width to be correctly computed for rectangles starting from the beginning.

#By appending a 0 to the heights, we're artificially adding a very short bar at the end of the histogram.
#Since 0 is smaller than any other height, it forces the algorithm to pop all remaining bars from the stack, ensuring that the areas for all bars are computed.
