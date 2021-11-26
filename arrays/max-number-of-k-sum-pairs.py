"""
https://leetcode.com/problems/max-number-of-k-sum-pairs/
"""


#OWN

def maxOperations(nums, k):
    ans, index_map = 0, dict()
    for index, val in enumerate(nums):
        if k - val in index_map and index_map[k - val] > 0:
            index_map[k - val] -= 1
            ans += 1
        else:
            index_map[val] = index_map.get(val, 0) + 1
    return ans