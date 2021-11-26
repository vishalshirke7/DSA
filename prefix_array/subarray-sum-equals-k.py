"""https://practice.geeksforgeeks.org/problems/subarray-with-0-sum-1587115621/1#"""

    def subArrayExists(self,arr,n):
        ##Your code here
        #Return true or false
        sum_map = dict()
        prefix_sum = 0
        for val in arr:
            prefix_sum += val
            if prefix_sum ==0 or prefix_sum in sum_map:
                return True
            sum_map[prefix_sum] = 1
        return False


"""https://www.geeksforgeeks.org/find-the-largest-subarray-with-0-sum/"""
def maxLen(n, arr):
	sum_map = dict()
    prefix_sum = max_len = 0
    for index in range(n):
        prefix_sum += arr[index]
        if arr[index] is 0 and max_len is 0:
        	max_len = 1
        if prefix_sum is 0:
        	max_len = index + 1
        if prefix_sum in sum_map:
            max_len = max(max_len, index - sum_map[prefix_sum])
        else:
        	sum_map[prefix_sum] = index
    return max_len
