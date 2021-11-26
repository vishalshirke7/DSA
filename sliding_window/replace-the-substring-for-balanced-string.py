"""
https://leetcode.com/problems/replace-the-substring-for-balanced-string/

https://leetcode.com/problems/replace-the-substring-for-balanced-string/discuss/409017/JAVA-Sliding-Window-Solution-with-Explanation
"""



def balancedString(s):
	ans, char_map = 0, dict()
	for char in s:
		char_map[char] = char_map.get(char, 0) + 1
	target = len(s) // 4
	print(char_map, target)	
	for char, count in char_map.items():
		if count > target:
			ans += count - target
	return ans



# print('Output', balancedString("QWER"))
# print('Output', balancedString("QQWE"))
# print('Output', balancedString("QQQW"))
# print('Output', balancedString("QQQQ"))
print('Output', balancedString("WWEQERQWQWWRWWERQWEQ"))