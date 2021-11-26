"""
https://leetcode.com/problems/fruit-into-baskets/
"""



def totalFruit(fruits):
	start, ans, baskets = 0, 0, 2
	occur_map = {}
	for end, val in enumerate(fruits):
		occur_map[val] = occur_map.get(val, 0) + 1
		while len(occur_map) > 2:
			occur_map[fruits[start]] -= 1
			if not occur_map[fruits[start]]:
				del occur_map[fruits[start]]
			start += 1
		ans = max(ans, end - start + 1)
	return ans


print('Output', totalFruit([3,3,3,1,2,1,1,2,3,3,4]))