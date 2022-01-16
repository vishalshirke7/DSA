""""
https://leetcode.com/problems/trapping-rain-water/
https://www.interviewbit.com/old/problems/rain-water-trapped/
"""

# TWO Pointer
# 1
def trap(height):
	start, end, output = 0, len(height) - 1, 0
	left_max, right_max = 0, 0
	while start < end:
		if height[start] < height[end]:
			if height[start] < left_max:
				output += left_max - height[start]
			else:
				left_max = height[start]
			start += 1				
		else:
			if height[end] < right_max:
				output += right_max - height[end]
			else:
				right_max = height[end]
			end -= 1				
	return output

print('Output', trap([0,1,0,2,1,0,1,3,2,1,2,1]))	


#STACK
# 2
def maxWater(height):
	ans, stack = 0, []
	for index in range(len(height)):
		while(len(stack) != 0 and (height[stack[-1]] < height[index])):
			top_height = height[stack[-1]]
			stack.pop()
			if(len(stack) == 0):
				break
			distance = index - stack[-1] - 1
			min_height = min(height[stack[-1]], height[index]) - top_height
			ans += distance * min_height
		stack.append(index)
	return ans

arr=[ 0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(maxWater(arr))


# 3
def findWater(arr, n):
	left, right, water = [0]*n, [0]*n, 0
	left[0] = arr[0]
	for i in range( 1, n):
		left[i] = max(left[i-1], arr[i])
	right[n-1] = arr[n-1]
	for i in range(n-2, -1, -1):
		right[i] = max(right[i + 1], arr[i])
	for i in range(0, n):
		water += min(left[i], right[i]) - arr[i]
	return water

print("Maximum water that can be accumulated is", findWater([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 12))


#4 - Optimized version of 3 is 1 