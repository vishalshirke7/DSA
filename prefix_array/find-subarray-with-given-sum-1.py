"""
https://www.geeksforgeeks.org/find-subarray-with-given-sum/
positive integers

"""

def subArraySum(arr, n, s):
   ans = [-1]
   if n == 1:
       return ans
   left, right, cur_sum = 0, 1, arr[0]
   while right <= n:
   		while cur_sum > s:
   			cur_sum = cur_sum - arr[left]
   			left += 1
   		if cur_sum == s:
   			return [left + 1, right]
   		if right < n:
   			cur_sum += arr[right]
   		right += 1
   return ans

# print('Output', subArraySum([1,2,3,7,5], 5, 12))
print('Output', subArraySum([1,2,3,4,5,6,7,8,9,10], 10, 15))

