"""
https://leetcode.com/problems/largest-rectangle-in-histogram/
"""
"""
public static int largestRectangleArea(int[] height) {
    if (height == null || height.length == 0) {
        return 0;
    }
    int[] lessFromLeft = new int[height.length]; // idx of the first bar the left that is lower than current
    int[] lessFromRight = new int[height.length]; // idx of the first bar the right that is lower than current
    lessFromRight[height.length - 1] = height.length;
    lessFromLeft[0] = -1;

    for (int i = 1; i < height.length; i++) {
        int p = i - 1;

        while (p >= 0 && height[p] >= height[i]) {
            p = lessFromLeft[p];
        }
        lessFromLeft[i] = p;
    }

    for (int i = height.length - 2; i >= 0; i--) {
        int p = i + 1;

        while (p < height.length && height[p] >= height[i]) {
            p = lessFromRight[p];
        }
        lessFromRight[i] = p;
    }

    int maxArea = 0;
    for (int i = 0; i < height.length; i++) {
        maxArea = Math.max(maxArea, height[i] * (lessFromRight[i] - lessFromLeft[i] - 1));
    }

    return maxArea;
}
"""

def largestRectangleArea(heights):
    max_area = 0
    left_max, right_max = [1] * len(heights), [1] * len(heights)
    for index in range(len(heights)):
        prev = index - 1
        while prev >=0:
            if heights[prev] >= heights[index]:
                left_max[index] += left_max[prev]
                prev -= left_max[prev]
            else:
                break
    for index in range(len(heights) - 1, -1, -1):
        prev = index + 1
        while prev < len(heights):
            if heights[prev] >= heights[index]:
                right_max[index] += right_max[prev]
                prev += right_max[prev]
            else:
                break
    for index in range(len(heights)):
        max_area = max(max_area, heights[index] * (right_max[index] + left_max[index] - 1))
    return max_area


print('Output', largestRectangleArea([2,1,5,6,2,3]))


    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = [1]*n
        right = [1]*n
        
        for i in range(1,n):
            j = i - 1
            while j>=0 and heights[j] >= heights[i]:
                j -= left[j]
            left[i] = i - j
             
        for i in range(n-2,-1,-1):
            j = i + 1
            while j < len(heights) and heights[i] <= heights[j]:
                j += right[j] 
            right[i] = j - i
            
        res = 0
        for i in range(n):
            res = max(res,heights[i]*(left[i]+right[i]-1))
                
        return res