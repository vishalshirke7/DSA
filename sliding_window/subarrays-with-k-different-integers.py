"""
https://leetcode.com/problems/subarrays-with-k-different-integers/
https://www.interviewbit.com/problems/subarrays-with-distinct-integers/
"""


def subarraysWithKDistinct(nums, k):
		def atMostK(k):
			start = ans = 0
			count_map = dict()
			for index in range(len(nums)):	
				if count_map.get(nums[index], 0) == 0:
					k -= 1
				count_map[nums[index]] = count_map.get(nums[index], 0) + 1
				while k < 0:
					count_map[nums[start]] -= 1
					if count_map[nums[start]] == 0:
						k += 1
					start += 1
				ans += index - start + 1
			return ans
		return atMostK(k) - atMostK(k - 1)



print('Output', subarraysWithKDistinct([1,2,1,2,3], 2))
print('Output', subarraysWithKDistinct([1,2,1,3,4], 3))

"""
    def subarraysWithKDistinct(self, A: 'List[int]', K: 'int') -> 'int':
        freq = {}
        start = 0
        start_k = 0
        res = 0
        for i, x in enumerate(A):
            freq[x] = freq.get(x, 0) + 1
            if len(freq) == K + 1:
                # remove the distinct at start_k, move start_k, start
                del freq[A[start_k]]
                start_k += 1
                start = start_k
            if len(freq) == K:
                # update start_k and res (Notice: K >= 1)
                while freq[A[start_k]] > 1:
                    freq[A[start_k]] -= 1
                    start_k += 1
                res += start_k - start + 1
        return res

"""        