"""
https://leetcode.com/problems/find-k-closest-elements/
"""

# discuss O(n)
def findClosestElements(arr, k, x):
	start, end, output = 0, len(arr) - 1, list()
	while end - start >= k:
		if abs(arr[start] - x) > abs(arr[end] - x):
			start += 1
		else:
			end -= 1
	for index in range(start, end + 1):
		output.append(arr[index])
	return output

# discuss log(n) + K
def findClosestElements(arr, k, x):
    lo, hi = 0, len(arr)-k
    while lo<hi:
        mid = (lo + hi)//2
        if x-arr[mid]>arr[mid+k]-x:
            lo = mid + 1
        else:
            hi = mid
    return arr[lo:lo+k]	


# def findClosestElements(arr, k, x):
# 	start, end, closest_index = 0, len(arr) - 1, None
# 	while start < end:
# 		mid = (start + end) // 2
# 		if arr[mid] == x:
# 			closest_index = mid
# 			break
# 		if x <= arr[start]:
# 			return arr[start:start+k]
# 		if x >= arr[end]:
# 			return arr[len(arr) - k:len(arr)]
# 		if arr[start] < x < arr[mid]:
# 			end = mid - 1
# 		else:
# 			start = mid + 1
# 	visited = [False] * len(arr)
# 	closest_index = start if closest_index is None else closest_index
# 	visited[closest_index] = True
# 	left, right = closest_index, closest_index + 1
# 	while left >= 0 and right < len(arr) and k > 0:
# 		if abs(arr[left] - x) <= abs(arr[right] - x):
# 			visited[left] = True
# 			left -= 1
# 		else:
# 			visited[right] = True			
# 			right += 1
# 		k -= 1
# 	s, e = 0, 0
# 	for index in range(len(visited)):
# 		if visited[index]:
# 			s = index
# 			break
# 	for index in range(len(visited) - 1, -1, -1):
# 		if visited[index]:
# 			e = index
# 			break	
# 	return arr[s:e+1]


print('Output', findClosestElements([-2,-1,1,2,3,4,5], 7, 3))
# print('Output', findClosestElements([1,1,1,10,10,10], 1, 9))
# print('Output', findClosestElements([1,2,3,4,5], 4, -1))
# print('Output', findClosestElements([1,2,3,4,5], 4, 3))