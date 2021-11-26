"""
https://leetcode.com/problems/top-k-frequent-elements/
"""

#OWN O(n log n)

def topKFrequent(nums, k):
    count_map = dict()
    for val in nums:
        count_map[val] = count_map.get(val, 0) + 1
    count_map = sorted(count_map.items(), key=lambda x:x[1], reverse=True)
    ans = list()
    for cn in range(k):
        ans.append(count_map[cn][0])
    return ans


# O(n) Bucket Sort
def topKFrequent(nums, k):
    count_map = dict()
    for val in nums:
        count_map[val] = count_map.get(val, 0) + 1
    buckets = [[] for bucket in range(len(nums) + 1)]
    for number, count in count_map.items():
    	buckets[count].append(number)
    consolidated = list()
    for bucket in range(len(nums), -1, -1):
    	consolidated += buckets[bucket]
    return consolidated[:k]


print('Output', topKFrequent([1,1,1,2,2,3], 2))   
# print('Output', topKFrequent([1], 1))    