"""
https://leetcode.com/problems/maximum-erasure-value/
"""

"""
    def maximumUniqueSubarray(self, nums):
        beg, end, S, n, sm = 0, 0, set(), len(nums), 0
        ans = 0
        while end < n:
            if nums[end] not in S:
                sm += nums[end]
                S.add(nums[end])
                end += 1
                ans = max(ans, sm)
            else:
                sm -= nums[beg]
                S.remove(nums[beg])
                beg += 1
        
        return ans 

"""        


#OWN
def maximumUniqueSubarray(nums):
	start, total, ans, char_map = 0, 0, 0, dict()
	for end in range(len(nums)):
		char_map[nums[end]] = char_map.get(nums[end], 0) + 1
		total += nums[end]
		while char_map[nums[end]] > 1:
			char_map[nums[start]] -= 1
			total -= nums[start]
			start += 1
		ans = max(ans, total)
	return ans




print('Output', maximumUniqueSubarray([4,2,4,5,6]))	
print('Output', maximumUniqueSubarray([5,2,1,2,5,2,1,2,5]))	